from fitz import open as fitz_open
from pathlib import Path

def merge_PDF_files_to_one(src_dir: str, dest_path: str):
    output = fitz_open()
    for p in Path(src_dir).iterdir():
        if p.is_file() and p.name[-3:].lower() == 'pdf':
            output.insert_pdf(fitz_open(p))
    output.save(dest_path)
    output.close()
