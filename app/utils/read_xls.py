import xlrd, xlwt
from xlutils.copy import copy

book = xlrd.open_workbook('./app/data/pagina.xls')
information = {
    'PRODUCTOS': [],
    'INFORMACION':{}
}

def read_all_xls():
    for sheet in book:
        num_rows = sheet.nrows
        for row in range(1,num_rows):
            if sheet.name == "PRODUCTOS":
                information['PRODUCTOS'].append(format_product(sheet, row))
            elif sheet.name == "DISPONIBILIDAD":
                information['PRODUCTOS'][row-1]["disponible"] = bool(int(str(sheet.cell(row, 1).value)[:1]))
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

def get_product_by_id(id):
    for product in information["PRODUCTOS"]:
        if parseInt(product["id"]) == parseInt(id):
            return product

def get_product_idx(product):
    return information["PRODUCTOS"].index(product)

def parseForm(form):
    product = form.to_dict()
    product["disponible"] = "disponible" in product
    return product

def parseInt(num):
    return int(float(str(num)))
