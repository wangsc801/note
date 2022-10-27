import os
import shutil
import fitz

TMP_DIR = f".{os.sep}image_exctracted{os.sep}"


def remove_tmp_dir():
    shutil.rmtree(TMP_DIR)


def create_tmp_dir():
    if os.path.exists(TMP_DIR):
        remove_tmp_dir()
    os.mkdir(TMP_DIR)


def PDF_to_image(file_path: str, output_dir: str, zoom: float, rotate: int = 0):
    create_tmp_dir()
    doc = fitz.open(file_path)
    mat = fitz.Matrix(zoom, zoom).prerotate(rotate)
    for pno in range(doc.page_count):
        pix = doc[pno].get_pixmap(matrix=mat)
        pix.save(f"{output_dir}{os.sep}page-{pno}.png")
    doc.close()
    ### historic code ###
    # for page in range(file.pageCount):
    #     cur_page = file[page]
    #     trans = fitz.Matrix(1.2, 1.2).preRotate(int(0))
    #     pix = cur_page.getPixmap(matrix=trans, alpha=False)
    #     pix.writePNG(str(page)+'.png')


def PDF_page_to_image(file_path: str, pno: int, zoom: float, output_dir: str):
    doc = fitz.open(file_path)
    page = doc[pno]
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    pix.save(f".{os.sep}output_image.png")