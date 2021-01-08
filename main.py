from flask import Flask, render_template
from stargazers_count import *
from top_projects import *
from python_repos import *
from lang_popularity import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/pythonprojects/", methods=['POST'])
def view_chart_python_projects():
    viewBrowserPythonStats()
    return render_template('index.html')


@app.route("/PDFpythonprojects/", methods=['POST'])
def savePDF_chart_python_projects():
    savePDFPythonStats()
    return render_template('index.html')


@app.route("/topprojects/", methods=['POST'])
def view_chart_top_projects():
    viewBrowserTopProjectStats()
    return render_template('index.html')


@app.route("/PDFtopprojects/", methods=['POST'])
def savePDF_chart_top_projects():
    savePDFTopProjectStats()
    return render_template('index.html')


@app.route("/toplanguagues/", methods=['POST'])
def view_chart_top_languages():
    viewBrowserStarStats()
    return render_template('index.html')


@app.route("/PDFtoplanguagues/", methods=['POST'])
def savePDF_chart_top_languages():
    sevePDFStarStats()
    return render_template('index.html')


@app.route("/timeline/", methods=['POST'])
def view_chart_time_line():
    view_line()
    return render_template('index.html')


@app.route("/PDFtimeline/", methods=['POST'])
def savePDF_chart_time_line():
    savePDF_line()
    return render_template('index.html')


@app.route("/barhorizontal/", methods=['POST'])
def view_chart_time_bar_horizontal():
    view_bar_horizontal()
    return render_template('index.html')


@app.route("/PDFbarhorizontal/", methods=['POST'])
def savePDF_chart_time_bar_horizontal():
    savePDF_bar_horizontal()
    return render_template('index.html')


@app.route("/barstacked/", methods=['POST'])
def view_chart_time_bar_stacked():
    view_bar_stacked()
    return render_template('index.html')


@app.route("/PDFbarstacked/", methods=['POST'])
def savePDF_chart_time_bar_stacked():
    savePDF_bar_stacked()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
