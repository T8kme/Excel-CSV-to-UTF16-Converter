# Excel-CSV-to-UTF16-Converter
![GUI](https://i.imgur.com/h3wGX9A.png)

Simple python script to convert Excel UTF-8 CSV into comma delimited UTF-16 CSV
It can be used to adapt Excel CSV file to the Adobe InDesign CSV file used in the merge function

## How to use?

`python EncodingConverter.py`

## Sample output:

#### Before:
```
Name1 Surname1  ;
Name2 Surname2;
Name3 Surname3;
Name4 Surname4;
Name5 Surname5;
Name6  Surname6;
Name7 Surname7;
Name8 Surname8;
Name9 Surname9;
Name10  Surname10 ;
Name11 Surname11;
Name12 Surname12;
```
#### After
```
Name1 Surname1,
Name2 Surname2,
Name3 Surname3,
Name4 Surname4,
Name5 Surname5,
Name6 Surname6,
Name7 Surname7,
Name8 Surname8,
Name9 Surname9,
Name10 Surname10,
Name11 Surname11,
Name12 Surname12,
```
## U can simply make executable file using cx_freeze
`python setup.py build`
