import xlrd

book = xlrd.open_workbook('./app/data/pagina.xls')

def sheet_names():
    return book.sheet_names()

def n_sheets():
    return book.nsheets

def n_rows_and_columns(sheet_index):
    if sheet_index > n_sheets() - 1:
        return
    sheet = book.sheet_by_index(sheet_index)
    return {"nrows":sheet.nrows, "ncols":sheet.ncols}

def cell_value(sheet_index, row, col):
    sheet = book.sheet_by_index(sheet_index)
    return sheet.cell(row,col).value

def col_data(sheet_index, col_index):
    sheet = book.sheet_by_index(sheet_index)
    return {sheet.cell(0, col_index).value : sheet.col_values(col_index, 1)}

def contains_col_name(sheet_index, col_name):
    sheet = book.sheet_by_index(sheet_index)
    for col in range(sheet.ncols):
        if sheet.cell(0, col).value == col_name:
            return True
    return False

def get_cols(sheet_index, cols):
    sheet = book.sheet_by_index(sheet_index)
    data = []
    for row in range(1,sheet.nrows):
        aux = {}
        for col in cols:
            aux[sheet.cell(0, col).value] = sheet.cell(row, col).value
        data.append(aux)
    return data

def get_sheet(sheet_index):
    sheet = book.sheet_by_index(sheet_index)
    data = []
    for row in range(1,sheet.nrows):
        aux = {}
        for col in range(0, sheet.ncols):
            aux[sheet.cell(0, col).value] = sheet.cell(row, col).value
        data.append(aux)
    return data

def sort_sheet(sheet, col):
    return sorted(get_sheet(sheet), key=lambda p: p[col])
