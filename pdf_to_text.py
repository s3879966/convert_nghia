import pymupdf  # imports the pymupdf library
import os

pdf_folder = "C:/Users/Admin/Desktop/pdf/"
output_folder = "C:/Users/Admin/Desktop/text_files/"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)

        # Create a text file name based on the PDF file name
        text_filename = filename.replace(".pdf", ".txt")
        text_file_path = os.path.join(output_folder, text_filename)

        # Open the PDF document
        doc = pymupdf.open(pdf_path)

        with open(text_file_path, "w", encoding="utf-8") as output_file:
            for page in doc:
                text = page.get_text()  # get plain text encoded as UTF-8
                output_file.write(text)  # write text to the output file

        print(f"Text extracted and written to {text_file_path}.")

print("Processing complete.")
