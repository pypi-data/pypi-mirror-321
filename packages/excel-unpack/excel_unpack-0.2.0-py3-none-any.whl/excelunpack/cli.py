import argparse
from .extract_attachments import extract_attachments_from_xlsx

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description="Extract and save attachments from an Excel (.xlsx) file."
    )
    # Add arguments for the input Excel file and output directory
    parser.add_argument(
        "xlsx_file",
        type=str,
        help="Path to the Excel (.xlsx) file.",
    )
    parser.add_argument(
        "output_dir",
        type=str,
        help="Path to the output directory where attachments will be saved.",
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function with the parsed arguments
    extract_attachments_from_xlsx(args.xlsx_file, args.output_dir)

if __name__ == "__main__":
    main()
