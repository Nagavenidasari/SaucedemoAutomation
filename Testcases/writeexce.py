import openpyexcel
path = "C:\SAMPLEDATA.xlsx"
workbook = openpyexcel.load_workbook(path)
sheet = workbook.get_sheet_by_name("Sheet2")

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row=r,column=c).value = "Welcome"
workbook.save(path)