from xlrd import open_workbook
wb = open_workbook('ESPP.xlsx')
for s in wb.sheets():
    for row in range(s.nrows):
        print(s.cell(row,0).value)
