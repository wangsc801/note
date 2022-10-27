from PyPDF2 import PdfFileReader, PdfFileWriter


def rotate_page(src_path: str, src_pno: int, angle: int, dest_path: str):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(src_path)
    do_page = pdf_reader.getPage(src_pno).rotateClockwise(angle)
    pdf_writer.addPage(do_page)
    with open(dest_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
