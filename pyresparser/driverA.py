from pyresparser import ResumeParser
# This script attempts to parse a resume PDF file and handle any errors that may occur during the process.
pdf_path = r'C:\Work\resumeList\Ashu Resume 2024.pdf'
print(f"Attempting to parse: {pdf_path}")

try:
    data = ResumeParser(pdf_path).get_extracted_data()
    print("Successfully parsed! Extracted data:")
    print(data)
except FileNotFoundError:
    print(f"ERROR: The file was not found at {pdf_path}")
    print("Please double-check the path and ensure the file exists.")
except Exception as e:
    print(f"An error occurred during parsing: {e}")
    import traceback
    print("Full traceback:")
    traceback.print_exc()