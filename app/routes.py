from app import app
from flask import render_template, request, url_for, redirect
import xlsdata

@app.route("/")
@app.route("/index")
def index():
    products = xlsdata.information["PRODUCTOS"]
    page_info = xlsdata.information["INFORMACION"]
    is_available = xlsdata.is_available
    return render_template('index.html',  page_info = page_info, products = products, is_available=is_available )

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        xlsdata.add_product(request.form.to_dict())
        return redirect(url_for('index'))
    else:
        next_id = xlsdata.get_next_id()
        return render_template('add.html', next_id=next_id)

@app.route("/<int:id>/delete", methods=["GET","POST"])
def delete(id):
    product = xlsdata.get_product_by_id(id)
    if request.method == "POST":
        xlsdata.delete_product(product)
        return redirect(url_for('index'))
    return render_template('delete.html', product=product)

@app.route("/<int:id>/update", methods=["GET","POST"])
def update(id):
    product = xlsdata.get_product_by_id(id)
    if request.method == "POST":
        xlsdata.update_product(product, request.form.to_dict())
        return redirect(url_for('index'))
    return render_template('update.html', product=product)
    