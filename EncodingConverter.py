import codecs
import re
import tkinter as tk
from tkinter import Tk, Label, Button, W, E, DISABLED, NORMAL
from tkinter.filedialog import askopenfilename

class Application(tk.Frame):
    fileName = ""
    myText = ""

    def __init__(self, master=None):
        super().__init__(master)
        self.pack(pady=3)
        self.create_widgets()

    def create_widgets(self):
        root.title("Encoding Converter")
        root.minsize(300,127)
        
        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        positionRight = int(root.winfo_screenwidth()/2 - windowWidth/1.3)
        positionDown = int(root.winfo_screenheight()/2 - windowHeight)
        root.geometry("+{}+{}".format(positionRight, positionDown))

        self.button1 = tk.Button(self)
        self.button1["text"] = "FILE"
        self.button1["command"] = self.openFileDialog
        self.button1["width"] = 30

        self.label1 = tk.Label(self)
        self.label1["text"] = "Choose file to convert!"

        self.button2 = tk.Button(self)
        self.button2["text"] = "CONVERT"
        self.button2["command"] = self.convertFile
        self.button2["state"] = DISABLED
        self.button2["width"] = 30

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit["width"] = 30

        self.label2 = tk.Label(self)
        self.label2["text"] = ""

        self.button1.grid(row=1, column=0, sticky=W+E)
        self.label1.grid(row=2, column=0, sticky=W+E)
        self.button2.grid(row=3, column=0, sticky=W+E)
        self.label2.grid(row=4, column=0, sticky=W+E)
        self.quit.grid(row=5, column=0, sticky=W+E)

    def openFileDialog(self):
        name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                               filetypes =(("Text File", "*.csv"),("All Files","*.*")),
                               title = "Choose a file."
                               )
        #print (name)
        #Using try in case user types in unknown file or closes without choosing a file.
        try:
            with open(name,'r', encoding="utf8") as UseFile:
                UseFile.read()
                #print(UseFile.read())
            self.button2["state"] = NORMAL
            self.fileName = name
            self.label1["text"] = "File: " + self.fileName
        except:
            #print("No file exists")
            self.label1["text"] = "Error reading file!"

    def convertFile(self):
        with open(self.fileName, "r", encoding="utf8") as f:
            self.myText = f.read() # read everything in the file
            self.myText = self.myText.replace(';', ',')
            self.myText = re.sub(' +',' ',self.myText)
            self.myText = re.sub(',+',',',self.myText)
            self.myText = self.myText.replace(' ,', ',')
            self.myText = self.myText.replace('\n,\n', '\n')
            self.myText = self.myText.replace('\n', '\r\n')
            self.myText = self.myText.replace(' \r', '\r')
            self.myText = self.myText.replace(', ', ' ')
            self.myText = re.sub(',+',',',self.myText)
            self.myText = self.myText.replace(', ', ' ')
            self.myText = self.myText.replace('\n ', '\n')
            #print(self.myText)
        with open(self.fileName, 'wb') as f:
            f.write(codecs.BOM_UTF16_BE)
            f.write(self.myText.encode('utf-16-be'))
        self.label2["text"] = "File encoding changed to big endian!"

root = tk.Tk()
app = Application(master=root)
app.mainloop()