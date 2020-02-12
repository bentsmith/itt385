import openpyxl

filename = "C:\\Users\\labuser\\Desktop\\Four-Cells.xlsx"

workbook = openpyxl.load_workbook(filename)

sheet = workbook.get_sheet_by_name("Sheet1")

for row in range(1,3):
    for col in range(1,3):
        print(row, col, sheet.cell(row,col).value)