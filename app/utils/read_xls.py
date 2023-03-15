import xlrd, xlwt
from xlutils.copy import copy

book = xlrd.open_workbook('./app/data/pagina.xls')
information = {
    'PRODUCTOS': [],
    'DISPONIBILIDAD':{},
    'INFORMACION':{}
}

def read_all_xls():
    for sheet in book:
        num_rows = sheet.nrows
        for row in range(1,num_rows):
            if sheet.name == "PRODUCTOS":
                information['PRODUCTOS'].append(format_product(sheet,row))
            elif sheet.name == "DISPONIBILIDAD":
                information['DISPONIBILIDAD'][parseInt(sheet.cell(row, 0).value)] = bool(int(str(sheet.cell(row, 1).value)[:1]))
            elif sheet.name == 'INFORMACION':
                information['INFORMACION'][str(sheet.cell(row, 0).value)] = str(sheet.cell(row, 1).value)
    return information

def format_product(sheet, row):
    if not sheet.cell(row, 0).value:
        return
    return {
        'id': parseInt(sheet.cell(row, 0).value),
        'nombre': str(sheet.cell(row, 1).value),
        'precio': float(str(sheet.cell(row, 2).value)),
        'cantidad': float(str(sheet.cell(row, 3).value)),
        'categoria': str(sheet.cell(row, 4).value),
        'imagen': str(sheet.cell(row, 5).value),
    }

def is_available(id):
    return information["DISPONIBILIDAD"][parseInt(id)]

def get_product_by_id(id):
    for product in information["PRODUCTOS"]:
        if parseInt(product["id"]) == parseInt(id):
            product["disponible"] = is_available(id)
            return product
        
def get_product_idx(product):
    return information["PRODUCTOS"].index(product)

def get_product_by_idx(index):
    product = information["PRODUCTOS"][index]
    product["disponible"] = is_available(product["id"])
    return product

def get_next_id():
    return information["PRODUCTOS"][-1]["id"] + 1

def parseInt(num):
    return int(float(str(num)))
