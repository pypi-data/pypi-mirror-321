# ExcelUnpack

ExcelUnpack is a Python tool that allows you to extract embedded attachments from Excel files (XLSX).

## Installation

You can install ExcelUnpack using pip:

```
pip install excelunpack
```

## Usage

### As a Command-Line Tool:

```
extract-xlsx-attachments path/to/excel/file.xlsx path/to/output/folder
```

### As a Python Library:

```python
from excelunpack.excel_attachments import extract_attachments_from_xlsx

xlsx_file = "path/to/excel/file.xlsx"
output_dir = "path/to/output/folder"
extract_attachments_from_xlsx(xlsx_file, output_dir)
```

---

### **6. `tests/test_extract.py` (Unit Tests for Extraction)**

```python
import unittest
from excelunpack.extract_attachments import extract_attachments_from_xlsx

class TestExcelUnpack(unittest.TestCase):

    def test_extract_attachments(self):
        # Assuming you have a test XLSX file for this
        result = extract_attachments_from_xlsx("test.xlsx", "output_folder")
        self.assertTrue(result)  # Check expected result

if __name__ == '__main__':
    unittest.main()
```
