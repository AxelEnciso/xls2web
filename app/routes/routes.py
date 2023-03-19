from app import app
from flask import render_template, request, url_for, redirect, jsonify, send_file
from app.utils.read_xls import *
from app.utils.write_xls import *

@app.route("/")
@app.route("/index")
def index():
    products = information["PRODUCTOS"]
    page_info = information["INFORMACION"]
    return render_template('index.html',  page_info = page_info, products = products)

@app.route("/create", methods=["GET","POST"])
def create():
    if request.method == "POST":
        create_product(parseForm(request.form))
        return redirect(url_for('index'))
    else:
        return render_template('create.html', next_id = next_id())

@app.route("/<int:id>/delete", methods=["GET", "POST"])
def delete(id):
    product = get_product_by_id(id)
    if request.method == "POST":
        delete_product(product)
        return redirect(url_for('index'))
    return render_template('delete.html', product = product)

@app.route("/<int:id>/update", methods=["GET", "POST"])
def update(id):
    product = get_product_by_id(id)
    if request.method == "POST":
        update_product(product, parseForm(request.form))
        return redirect(url_for('index'))
    return render_template('update.html', product = product)

# API
@app.route("/api/informacion", methods=["GET"])
def informacion():
    return jsonify(information["INFORMACION"])

@app.route("/api/productos/", methods=["GET"])
def productos():
    return jsonify(total = len(information["PRODUCTOS"]), productos = information["PRODUCTOS"])

@app.route("/api/productos/<int:id>", methods=["GET"])
def producto(id):
    product = get_product_by_id(id)
    return jsonify(producto=product)

@app.route("/api/logo.png", methods=["GET"])
def logo():
    return send_file("static\img\keyboard.png", mimetype='image/gif')


