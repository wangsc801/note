import fitz


def truncate_by_range(input_doc_path: str, output_doc_path: str, start: int, end: int):
    input_doc = fitz.open(input_doc_path)
    output_doc = fitz.open()
    output_doc.insert_pdf(input_doc, start, end)
    output_doc.save(output_doc_path)
    output_doc.close()