import fitz


def append_page(fpath, text, fontsize, page_width=595, page_height=842):
    doc = fitz.open(fpath)
    page_count = doc.page_count
    doc.insert_page(page_count, text=text, fontsize=fontsize,
                    width=page_width, height=page_height)
    # Since version 1.9.1, incremental saves are possible for PDF documents.
    # - it is normally a lot faster, because changes are appended to the file,
    #   it is not rewritten as a whole
    # - it spares handling intermediate files if all you want is actually
    #   updating a specific document
    # https://github.com/pymupdf/PyMuPDF/wiki/Using-Incremental-Saves
    # https://pymupdf.readthedocs.io/en/latest/document.html#Document.save
    # https://pymupdf.readthedocs.io/en/latest/vars.html#encryptionmethods
    doc.save(filename=fpath, incremental=True,
             encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()


def new_page_and_text_example(fpath):
    doc = fitz.open()
    point = fitz.Point(64, 800)
    text = "file path: "+fpath
    # A4-paper size: width=595, height=842
    page = doc.new_page(pno=-1, width=595, height=842)
    page.insert_text(point, text, fontsize=48, rotate=90, fill_opacity=0.5)
    page.insert_text(fitz.Point(64, 64), "file 1", fontsize=56)
    doc.save(fpath)
    doc.close()
