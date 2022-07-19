import openpyexcel

def getRowscount(file,SheetName):
    workbook = openpyexcel.load_workbook(file)
    sheet = workbook.get_sheet_by_name(SheetName)
    return sheet.max_row
def getColumncount(file,SheetName):
    workbook = openpyexcel.load_workbook(file)
    sheet = workbook.get_sheet_by_name(SheetName)
    return sheet.max_column
def readData(file,SheetName,rownum,columnnum):
    workbook = openpyexcel.load_workbook(file)
    sheet = workbook.get_sheet_by_name(SheetName)
    return sheet.cell(row=rownum,column=columnum).value
def writeDate(file,SheetName,rownum,columnnum,data):
    workbook = openpyexcel.load_workbook(file)
    sheet = workbook.get_sheet_by_name(SheetName)
    sheet.cell(row=rownum,column=columnnum).value=data
    workbook.save(file)
