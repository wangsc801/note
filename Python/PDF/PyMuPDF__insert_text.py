from msilib.schema import Font
import fitz
from fitz.utils import getColor


def add_watermark(fpath: str, text: str, point_x: int, point_y: int,  fontsize: int, opacity: float = 0.5, rotate=0, fill_color="black"):
    point = fitz.Point(point_x, point_y)
    doc = fitz.open(fpath)
    for page in doc:
        page.insert_text(point, text, fontsize=fontsize, rotate=rotate,
                         fill_opacity=opacity, fill=getColor(fill_color))
    doc.save(fpath, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()


def add_text(fpath: str, pno: int, text: str, fontfile: str, fontsize: int, point_x: int, point_y: int):
    doc = fitz.open(fpath)
    font = fitz.Font(fontfile=fontfile)
    page = doc[pno]
    point = fitz.Point(point_x, point_y)
    text_writer = fitz.TextWriter(page.rect)
    # core code
    # append(...) and appendv(...)
    text_writer.append(point, text, font=font,fontsize=fontsize)
    text_writer.write_text(page)
    doc.save(fpath, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()


def cover_rect(filepath, pno=0, rect=(20, 20, 36, 36), stroke_color="LIGHTBLUE", fill_color="CHOCOLATE"):
    doc = fitz.open(filepath)
    stroke_color = getColor(stroke_color)
    fill_color = getColor(fill_color)
    page = doc[pno]
    page.draw_rect(rect, color=stroke_color, fill=fill_color)
    doc.save(filepath, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
