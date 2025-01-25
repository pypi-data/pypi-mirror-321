# ExcelUnpack

ExcelUnpack is a Python tool that allows you to extract embedded attachments from Excel files (XLSX).

## Installation

You can install ExcelUnpack using pip:

```
pip install excel-unpack
```

## Usage

### As a Command-Line Tool:

```
excel-unpack path/to/excel/file.xlsx path/to/output/folder
```

### As a Python Library:

```python
from excelunpack.excel_attachments import extract_attachments_from_xlsx

xlsx_file = "path/to/excel/file.xlsx"
output_dir = "path/to/output/folder"
extract_attachments_from_xlsx(xlsx_file, output_dir)
```
