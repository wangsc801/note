import fitz
from pathlib import Path

def image_to_PDF(src_dir:str,output_path:str):
    output = fitz.open()
    img_ext=['.jpg','.jpeg','.png','.bmp']
    for f in Path(src_dir).iterdir():
        if f.suffix[-4:].lower() in img_ext:
            img = fitz.open(f)
            pdfbytes=img.convert_to_pdf()
            img_pdf = fitz.open('pdf', pdfbytes)
            output.insert_pdf(img_pdf)
    output.save(output_path)
    output.close()
    