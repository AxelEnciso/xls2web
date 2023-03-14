import xlrd, xlwt
from xlutils.copy import copy

book = xlrd.open_workbook('pagina.xls')
sheets = book.nsheets
information = {
    'PRODUCTOS': [],
    'DISPONIBILIDAD':{},
    'INFORMACION':{}
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
                
#esta funcion valida que la columna sea la de los ID y busca un id especifico
def get_product_by_id(id):
    for product in information["PRODUCTOS"]:
        if product["id"] == id:
            return product
    
def get_next_id():
    return information["PRODUCTOS"][-1]["id"] + 1

def add_product(product):
    wb = copy(book)
    sheet = wb.get_sheet(1)
    sheet_available = wb.get_sheet(2)
    next_row = len(information["PRODUCTOS"]) + 1
    # Add product on excel
    sheet.write(next_row, 0, int(product["id"]))
    sheet.write(next_row, 1, str(product["nombre"]))
    sheet.write(next_row, 2, float(product["precio"]))
    sheet.write(next_row, 3, int(product["cantidad"]))
    sheet.write(next_row, 4, str(product["categoria"]))
    sheet.write(next_row, 5, str(product["imagen"]))
    sheet_available.write(next_row, 0, int(product["id"]))
    sheet_available.write(next_row, 1, bool(1))
    # Add product on state
    information["PRODUCTOS"].append(product)
    information["DISPONIBILIDAD"][int(product["id"])] = bool(1)
    wb.save('pagina.xls')

def delete_product(product):
    information["PRODUCTOS"].remove(product)
    del information["DISPONIBILIDAD"][product["id"]]
    
def update_product(product):
    wb = copy(book)
    sheet = wb.get_sheet(1)
    sheet_available = wb.get_sheet(2)
    
    i = 1
    for p in information["PRODUCTOS"]:
        print(product["id"], p["id"])
        if int(float(str(product["id"]))) == int(float(str(p["id"]))):
            print(p)
            sheet.write(i, 0, int(product["id"]))
            sheet.write(i, 1, str(product["nombre"]))
            sheet.write(i, 2, float(product["precio"]))
            sheet.write(i, 3, int(float(product["cantidad"])))
            sheet.write(i, 4, str(product["categoria"]))
            sheet.write(i, 5, str(product["imagen"]))
            sheet_available.write(i, 0, int(product["id"]))
            sheet_available.write(i, 1, bool(1))
            print(i)
            break
        i += 1
    # Add product on state
    print(information["PRODUCTOS"])
    print(product)
    print(i-2)
    information["PRODUCTOS"][i-2] = product
    information["DISPONIBILIDAD"][int(product["id"])] = bool(1)
    print(information["PRODUCTOS"][i-2])
    wb.save('pagina.xls')

loadXLS()
