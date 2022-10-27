from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('simhei', 'simhei.ttf'))

# Drawing(image-width, image-height)
drawing = Drawing(200, 123)
string = String(10, 10, "__TEXT__".encode('utf-8'), fontName='simhei', fontSize=18)
drawing.add(string)

renderPDF.drawToFile(drawing, "reportlab_output.pdf")
