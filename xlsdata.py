import xlrd
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
    return {
        'id': int(float(str(sheet.cell(row, 0).value))),
        'nombre': str(sheet.cell(row, 1).value),
        'precio': float(str(sheet.cell(row, 2).value)),
        'cantidad': float(str(sheet.cell(row, 3).value)),
        'categoria': str(sheet.cell(row, 4).value),
        'imagen': str(sheet.cell(row, 5).value),
    }

def is_available(id):
    return information["DISPONIBILIDAD"][id]
                
#esta funcion valida que la columna sea la de los ID y busca un id especifico
def get_product_by_id(id):
    for product in information["PRODUCTOS"]:
        if product == id:
            return product

#find_id_col(2,1)
loadXLS()
#print("Loading data for web")
