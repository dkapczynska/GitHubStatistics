from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


def saveToPDF(chart_path, name):
    drawing = svg2rlg(chart_path)
    renderPDF.drawToFile(drawing, name)
