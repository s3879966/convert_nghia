import os
from fpdf import FPDF


class PDF(FPDF):
    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        filtered_body = ''.join([c if self.is_latin1(c) else '?' for c in body])
        self.multi_cell(0, 10, filtered_body)
        self.ln()

    def is_latin1(self, char):
        try:
            char.encode('latin-1')
            return True
        except UnicodeEncodeError:
            return False


def c_to_pdf(input, output):
    if not os.path.exists(output):
        os.makedirs(output)

    for file_name in os.listdir(input):
        if file_name.endswith('.c'):
            base_name = os.path.splitext(file_name)[0]
            source_file = os.path.join(input, file_name)
            pdf_file = os.path.join(output, f"{base_name}.pdf")

            pdf = PDF()
            pdf.add_page()

            with open(source_file, 'r', encoding='utf-8') as file:
                content = file.read()

            pdf.chapter_body(content)
            pdf.output(pdf_file)

            print(f"c_to_pdfed {source_file} to {pdf_file}")

    print("All files have been c_to_pdfed.")


if __name__ == "__main__":
    input = "C:/Users/Admin/Desktop/SampleData"
    output = "C:/Users/Admin/Desktop/ctopdf/pdf2"

    c_to_pdf(input, output)
