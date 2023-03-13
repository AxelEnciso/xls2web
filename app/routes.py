from app import app
from flask import render_template
import xlsdata

@app.route("/")
@app.route("/index")
def index():
    products = xlsdata.information["PRODUCTOS"]
    page_info = xlsdata.information["INFORMACION"]
    is_available = xlsdata.is_available
    return render_template('index.html',  page_info = page_info, products = products, is_available=is_available )
