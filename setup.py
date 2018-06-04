from cx_Freeze import setup, Executable
import os
import cx_Freeze
import sys
import matplotlib

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR,'tcl','tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

files = {"include_files":[
                    "<Path to Python>/DLLs/tcl86t.dll",
                    "<Path to Python>/Python36-32/DLLs/tk86t.dll"
                        ],
            "packages": ["tkinter", "easygui","matplotlib"]
        }

packages = ["idna", "codecs", "tkinter"]
options = {
    'build_exe': {
        'packages':packages,
        'include_files':[
            os.path.join('<Path to Python>', 'DLLs', 'tk86t.dll'),
            os.path.join('<Path to Python>', 'DLLs', 'tcl86t.dll'),
         ],
    },    
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("EncodingConverter.py", base=base)]

cx_Freeze.setup(
    name = "EncodingCoverter",
    options = options,
    version = "1.0",
    description = 'Change encoding of your txt file to BE',
    executables = executables
)