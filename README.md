# ADM Common Defintion XML Generator.

This is a Python script for generating the ADM Common Definitions XML file from the ITU BS.2094 XLSX spreadsheet. It only works on the specific XLSX spreadsheet file that's been authored as part of BS.2094.

## Installation

To install the python script: 
```
pip install -e .
```

## Running

To run:
```
adm_cd_gen <input xls file> <output xml file>
```
where `<input xls file>` is the input XLS spreadsheet file, and `<output xml file>` is the ADM XML output file.
