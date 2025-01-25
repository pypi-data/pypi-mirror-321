import random
import string
import zipfile
import os
import shutil
import olefile
import xml.etree.ElementTree as ET

def generate_random_name(length=5):
    # Generate a random string of specified length from uppercase letters and digits
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def extract_attachments_from_xlsx(xlsx_file, output_dir):
    """
    Extracts attachments from an Excel file (XLSX) and organizes them by sheet.

    Args:
        xlsx_file (str): Path to the input XLSX file.
        output_dir (str): Directory where extracted files will be saved.
    """
    zip_extract_dir = os.path.join(output_dir, "zip_extract")
    os.makedirs(zip_extract_dir, exist_ok=True)

    with zipfile.ZipFile(xlsx_file, 'r') as zip_ref:
        zip_ref.extractall(zip_extract_dir)

    workbook_path = os.path.join(zip_extract_dir, "xl", "workbook.xml")
    sheet_names = []
    if os.path.exists(workbook_path):
        tree = ET.parse(workbook_path)
        root = tree.getroot()
        namespace = {"ns": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
        sheets = root.find("ns:sheets", namespace)
        if sheets is not None:
            for sheet in sheets.findall("ns:sheet", namespace):
                sheet_id = sheet.attrib.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
                sheet_names.append({"name": sheet.attrib["name"], "rId": sheet_id})

    worksheet_rels_path = os.path.join(zip_extract_dir, "xl", "worksheets", "_rels")
    embeddings_path = os.path.join(zip_extract_dir, "xl", "embeddings")

    attachments_output_path = os.path.join(output_dir, "attachments")
    os.makedirs(attachments_output_path, exist_ok=True)

    if os.path.exists(worksheet_rels_path) and os.path.exists(embeddings_path):
        for sheet_index, sheet in enumerate(sheet_names):
            sheet_name = sheet["name"]
            sheet_rels_file = os.path.join(worksheet_rels_path, f"sheet{sheet_index + 1}.xml.rels")

            if not os.path.exists(sheet_rels_file):
                print(f"No .rels file found for sheet: {sheet_name}")
                continue

            tree = ET.parse(sheet_rels_file)
            root = tree.getroot()
            namespace = {"ns": "http://schemas.openxmlformats.org/package/2006/relationships"}
            sheet_folder = os.path.join(attachments_output_path, sheet_name)
            os.makedirs(sheet_folder, exist_ok=True)

            for rel in root.findall("ns:Relationship", namespace):
                if "embeddings" in rel.attrib["Target"]:
                    embedding_file = os.path.basename(rel.attrib["Target"])
                    embedding_path = os.path.join(embeddings_path, embedding_file)

                    if not os.path.exists(embedding_path):
                        print(f"Embedding file not found: {embedding_file}")
                        continue

                    extension = os.path.splitext(embedding_file)[-1]

                    if extension != ".bin":
                        shutil.copy(embedding_path, os.path.join(sheet_folder, embedding_file))
                        print(f"Extracted: {embedding_file} to {sheet_folder}")
                    else:
                        if not olefile.isOleFile(embedding_path):
                            print(f"{embedding_path} is not a valid OLE file.")
                            continue

                        ole = olefile.OleFileIO(embedding_path)
                        if ['\x01Ole10Native'] in ole.listdir():
                            print("Found 'Ole10Native' stream.")
                            stream = ole.openstream(['\x01Ole10Native'])
                            data = stream.read()
                            parts = data.split(b'\x00', maxsplit=4)
                            filename = parts[3].decode('utf-8', errors='ignore')  # Extract the filename
                            if filename is None:
                                filename = generate_random_name()
                            file_content = parts[-1]  # Binary content of the embedded file
                            output_path = os.path.join(sheet_folder, filename)
                            with open(output_path, 'wb') as file:
                                file.write(file_content)
                            print(f"Saved embedded file as: {output_path}")
                        else:
                            print("No 'Ole10Native' stream found.")
                        ole.close()
    else:
        print("No embedded files or worksheet relationships found.")

    if os.path.exists(zip_extract_dir):
        shutil.rmtree(zip_extract_dir)
        print(f"Deleted folder: {zip_extract_dir}")
    else:
        print(f"Folder not found: {zip_extract_dir}")
