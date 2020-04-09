from openpyxl import load_workbook
 
wb = load_workbook('IP汇总.xlsx')
ws = wb['Sheet3']
all_data = []
for row in ws.rows:
    for cell in row:
        all_data.append(cell.value)
#print(sum(all_data))
for x in all_data:
    sum1 = 0
    sum1 = sum1 + int(x)

        