from app.utils.read_xls import *

read_all_xls()
wb = copy(book)
sheet_products = wb.get_sheet(1)
sheet_available = wb.get_sheet(2)

def create_product(product):
    next_row = len(information["PRODUCTOS"]) + 1
    product["disponible"] = "disponible" in product
    write_product_xls(next_row, product)
    information["PRODUCTOS"].append(product)
    information["DISPONIBILIDAD"][parseInt(product["id"])] = product["disponible"]

def update_product(prev, product):
    index = get_product_idx(prev)
    product["disponible"] = "disponible" in product
    write_product_xls(index+1, product)
    information["PRODUCTOS"][index] = product
    information["DISPONIBILIDAD"][parseInt(product["id"])] = product["disponible"]

def delete_product(product):
    index = get_product_idx(product)
    product["disponible"] = "disponible" in product
    len_products = len(information["PRODUCTOS"])
    write_product_xls(index + 1, get_product_by_idx(len_products - 1))
    delete_product_xls(len_products)
    information["PRODUCTOS"][index] = information["PRODUCTOS"][len_products - 1]
    del information["PRODUCTOS"][len_products - 1]
    del information["DISPONIBILIDAD"][parseInt(product["id"])]

def write_product_xls(index, product):
    sheet_products.write(index, 0, int(product["id"]))
    sheet_products.write(index, 1, str(product["nombre"]))
    sheet_products.write(index, 2, float(product["precio"]))
    sheet_products.write(index, 3, int(float(product["cantidad"])))
    sheet_products.write(index, 4, str(product["categoria"]))
    sheet_products.write(index, 5, str(product["imagen"]))
    sheet_available.write(index, 0, int(product["id"]))
    sheet_available.write(index, 1, product["disponible"])
    wb.save('./app/data/pagina.xls')

def delete_product_xls(index):
    sheet_products.write(index, 0, "")
    sheet_products.write(index, 1, "")
    sheet_products.write(index, 2, "")
    sheet_products.write(index, 3, "")
    sheet_products.write(index, 4, "")
    sheet_products.write(index, 5, "")
    sheet_available.write(index, 0, "")
    sheet_available.write(index, 1, "")
    wb.save('./app/data/pagina.xls')
