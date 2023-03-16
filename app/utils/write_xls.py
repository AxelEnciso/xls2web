from app.utils.read_xls import *

read_all_xls()
wb = copy(book)
sheet_information = wb.get_sheet(0)
sheet_products = wb.get_sheet(1)
sheet_available = wb.get_sheet(2)

def save_wb():
    wb.save('./app/data/pagina.xls')

def next_id():
    next_id = parseInt(information["INFORMACION"]["NEXT_ID"])
    sheet_information.write(4, 1, next_id+1)
    save_wb()
    information["INFORMACION"]["NEXT_ID"] = next_id + 1
    return next_id

def create_product(product):
    next_row = len(information["PRODUCTOS"]) + 1
    write_product_xls(next_row, product)
    information["PRODUCTOS"].append(product)

def update_product(prev, product):
    index = get_product_idx(prev)
    write_product_xls(index+1, product)
    information["PRODUCTOS"][index] = product

def delete_product(product):
    index = get_product_idx(product)
    len_products = len(information["PRODUCTOS"])
    write_product_xls(index + 1, information["PRODUCTOS"][len_products - 1])
    delete_product_xls(len_products)
    information["PRODUCTOS"][index] = information["PRODUCTOS"][len_products - 1]
    del information["PRODUCTOS"][len_products - 1]

def write_product_xls(index, product):
    sheet_products.write(index, 0, int(product["id"]))
    sheet_products.write(index, 1, str(product["nombre"]))
    sheet_products.write(index, 2, float(product["precio"]))
    sheet_products.write(index, 3, int(float(product["cantidad"])))
    sheet_products.write(index, 4, str(product["categoria"]))
    sheet_products.write(index, 5, str(product["imagen"]))
    sheet_available.write(index, 0, int(product["id"]))
    sheet_available.write(index, 1, product["disponible"])
    save_wb()

def delete_product_xls(index):
    sheet_products.write(index, 0, "")
    sheet_products.write(index, 1, "")
    sheet_products.write(index, 2, "")
    sheet_products.write(index, 3, "")
    sheet_products.write(index, 4, "")
    sheet_products.write(index, 5, "")
    sheet_available.write(index, 0, "")
    sheet_available.write(index, 1, "")
    save_wb()
