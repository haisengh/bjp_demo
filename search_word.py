from openpyxl import Workbook, load_workbook
from pymongo import MongoClient

sheet_sw = load_workbook("search_word.xlsx")["搜索型1"]
# print(sheet_sw)

def parse_sheet(sheet):
	table = []
	table_heads = [head for head in sheet[1]]
	# print(sheet_sw["A"][0].row)
	for row in sheet_sw:
		if row[0].row != 1:
			table.append({})
			for index in range(7):
				table[-1][table_heads[index].value] = row[index].value

	return table
print(parse_sheet(sheet_sw))

		