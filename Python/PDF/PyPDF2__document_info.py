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
