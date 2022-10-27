from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path


def merge_PDF_files_to_one(src_dir: str, dest_path: str):
    pdf_writer = PdfFileWriter()
    for p in Path(src_dir).iterdir():
        if p.is_file() and p.name[-3:].lower() == 'pdf':
            pdf_reader = PdfFileReader(p)
            num_of_pages = pdf_reader.getNumPages()
            for page in range(0, num_of_pages):
                pdf_writer.addPage(pdf_reader.getPage(page))
    with open(dest_path, 'wb') as output_file:
        pdf_writer.write(output_file)
