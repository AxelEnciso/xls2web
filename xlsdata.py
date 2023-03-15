import xlrd, xlwt
from xlutils.copy import copy

book = xlrd.open_workbook('pagina.xls')
sheets = book.nsheets
information = {
    'PRODUCTOS': [],
    'DISPONIBILIDAD':{},
    'INFORMACION':{}
}
EMPTY_PRODUCT = {
    'id':"",
    'nombre':"",
    'precio':"",
    'cantidad':"",
    'categoria':"",
    'imagen':"",
}

def loadXLS():
    for sheet in book:
        num_rows = sheet.nrows
        for row in range(1,num_rows):
            if sheet.name == "PRODUCTOS":
                information['PRODUCTOS'].append(format_product(sheet,row))
            elif sheet.name == "DISPONIBILIDAD":
                information['DISPONIBILIDAD'][int(float(str(sheet.cell(row, 0).value)))] = bool(int(str(sheet.cell(row, 1).value)[:1]))
            elif sheet.name == 'INFORMACION':
                information['INFORMACION'][str(sheet.cell(row, 0).value)] = str(sheet.cell(row, 1).value)
    return information

def format_product(sheet, row):
    if not sheet.cell(row, 0).value:
        return
    return {
        'id': int(float(str(sheet.cell(row, 0).value))),
        'nombre': str(sheet.cell(row, 1).value),
        'precio': float(str(sheet.cell(row, 2).value)),
        'cantidad': float(str(sheet.cell(row, 3).value)),
        'categoria': str(sheet.cell(row, 4).value),
        'imagen': str(sheet.cell(row, 5).value),
    }

def is_available(id):
    return information["DISPONIBILIDAD"][int(id)]

def get_product_by_id(id):
    for product in information["PRODUCTOS"]:
        if int(float(str(product["id"]))) == int(float(str(id))):
            return product
        
def get_product_idx(product):
    return information["PRODUCTOS"].index(product)

def get_next_id():
    return information["PRODUCTOS"][-1]["id"] + 1

def add_product(product):
    next_row = len(information["PRODUCTOS"]) + 1
    write_product(next_row, product)
    information["PRODUCTOS"].append(product)
    information["DISPONIBILIDAD"][int(product["id"])] = bool(1)

def delete_product(product):
    index = get_product_idx(product)
    len_products = len(information["PRODUCTOS"])
    delete_row(len_products)
    write_product(index + 1, information["PRODUCTOS"][len_products - 1])
    information["PRODUCTOS"][index] = information["PRODUCTOS"][len_products - 1]
    del information["PRODUCTOS"][len_products - 1]
    del information["DISPONIBILIDAD"][int(float(str(product["id"])))]

def write_product(index, product):
    sheet_products.write(index, 0, int(product["id"]))
    sheet_products.write(index, 1, str(product["nombre"]))
    sheet_products.write(index, 2, float(product["precio"]))
    sheet_products.write(index, 3, int(float(product["cantidad"])))
    sheet_products.write(index, 4, str(product["categoria"]))
    sheet_products.write(index, 5, str(product["imagen"]))
    sheet_available.write(index, 0, int(product["id"]))
    sheet_available.write(index, 1, bool(1))
    wb.save('pagina.xls')

def delete_row(index):
    sheet_products.write(index, 0, "")
    sheet_products.write(index, 1, "")
    sheet_products.write(index, 2, "")
    sheet_products.write(index, 3, "")
    sheet_products.write(index, 4, "")
    sheet_products.write(index, 5, "")
    sheet_available.write(index, 0, "")
    sheet_available.write(index, 1, "")
    wb.save('pagina.xls')

def update_product(prev, product):
    i = get_product_idx(prev)
    write_product(i+1, product)
    information["PRODUCTOS"][i] = product
    information["DISPONIBILIDAD"][int(product["id"])] = bool(1)
    
loadXLS()
wb = copy(book)
sheet_products = wb.get_sheet(1)
sheet_available = wb.get_sheet(2)