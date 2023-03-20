from app import app
from flask import render_template, request, url_for, redirect, jsonify, send_file
from app.utils.read_xls import *
from app.utils.write_xls import *
from app.utils.xls import *

# CRUD
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

# XLS
@app.route("/xls/<int:sheet>")
def sheet(sheet):
    contains_col = request.args.get("containsCol")
    if contains_col:
        return jsonify(containsCol = contains_col_name(sheet,contains_col))

    cols = request.args.get("cols")
    if cols:
        return jsonify(get_cols(sheet,[int(col) for col in cols.split(',')]))

    sortBy = request.args.get("sortBy")
    if sortBy:
        return jsonify(sort_sheet(sheet, str(sortBy)))
    n_rows_cols = n_rows_and_columns(sheet)
    return jsonify(data = get_sheet(sheet), info = n_rows_cols)

@app.route("/xls")
def xls():
    return jsonify(nSheets = n_sheets(), sheetNames = sheet_names())

@app.route("/xls/<int:sheet>/<int:col>")
def col(sheet, col):
    return jsonify(col_data(sheet, col))

@app.route("/xls/<int:sheet>/<int:col>/<int:row>")
def cell(sheet, col, row):
    return jsonify(value = cell_value(sheet, col, row))






