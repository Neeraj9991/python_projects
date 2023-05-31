import PyPDF2


def scan_pdf(pdf_path, pdf_output):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        pages = len(reader.pages)

        with open(pdf_output, "w", encoding="utf-8") as output:

            for page_num in range(pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                output.write(f"Page {page_num + 1}:")
                output.write(text)
                output.write('\n\n')


file_path = "####### Write PDF path here #########"
output_file = "output.txt"
scan_pdf(file_path, output_file)
