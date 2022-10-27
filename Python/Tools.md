# Tools

## unrar

```py
import rarfile
import zipfile
from pathlib import Path

def unzip(src_dir,targ_dir):
    for f in Path(src_dir).iterdir():
        if f.is_file():
            if f.suffix == '.zip':
                zip_file=zipfile.ZipFile(f.resolve())
                for name in zip_file.namelist():
                    print(str(name))
                    zip_file.extract(name,targ_dir)
                zip_file.close()

def unrar(src_dir,targ_dir):
    for f in Path(src_dir).iterdir():
        if f.is_file():
            if f.suffix == '.rar':
                rar_file=rarfile.RarFile(f.resolve())
                rar_file.extractall(targ_dir)
```

## sh

sh库让你像调用方法那样调用系统中的命令。

```py
import sh
sh.pwd()
sh.mkdir('new_folder')
sh.touch('new_file.txt')
```

## SHA256

```py
import hashlib
import sys
def check_sha256(path,checksum):
    with open(path,'rb') as f:
        sha256obj=hashlib.sha256()
        sha256obj.update(f.read())
        hash_val=sha256obj.hexdigest().upper()
        if hash_val == str(checksum).upper():
            return True
    return False

if __name__ == '__main__':
    if len(sys.argv) == 3:
        if check_sha256(sys.argv[1],sys.argv[2]):
            print("right")
        else:
            print("unceccessfully check")
    else:
        print("arg1: file path\narg2: checksum")
```

## PDF

### PyMuPDF - getColor

```py
from fitz.utils import getColorList

colors=getColorList()
for c in colors:
    print(c,end=', ')
```

### PyPDF2 - PDF info

```py
from PyPDF2 import PdfFileReader


def info(path):
    with open(path, 'rb') as file:
        pdf = PdfFileReader(file)
        # https://pypdf2.readthedocs.io/en/latest/modules/DocumentInformation.html#PyPDF2.DocumentInformation
        info = pdf.getDocumentInfo()
        res = f"""
file: \t\t{path}
author: \t{info.author}
creator: \t{info.creator}
title: \t\t{info.title}
creation date: \t{info.creation_date}
pages number: \t{pdf.getNumPages()}
"""
        return res
```
