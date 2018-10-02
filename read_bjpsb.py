from openpyxl import Workbook, load_workbook
ws = load_workbook("test.xlsx")["sheet"]

def extarct(row):
	collection = []
	for cell in row:
		if cell.value:
			collection.append({"name": cell.value, "span": [cell,]})
		else:
			collection[-1]["span"].append(cell)
	return collection

def span(span):
	"""
	return the tuple following the cells specified by the span.
	"""
	start = span[0].col_idx - 1
	end = span[-1].col_idx
	row = span[0].row + 1
	return ws[row][start:end]



cates = extarct(ws[1])
cates1 = extarct(span(cates[0]["span"]))
# ul = extarct(span(cates1[0]["span"]))
ul = span(cates1[0]["span"])
# ul1 = span(ul)
a = []

def create_list(ul):
	if span(ul)[0].value == None:
		return 
	else:
		ul = span(ul)
		a.append(ul)
		return create_list(ul)
create_list(ul)
print(a)




# def create_table(th):
# 	"""
# 	th ::= table head. a tuple consist of two cells.
# 	return the collection.
# 	"""
# 	tables = []
# 	row,col = th[0].row, th[0].column
# 	row1,col1 = th[1].row, th[1].column
# 	li = ws[col][row-1:]
# 	li1 = ws[col1][row1-1:]
# 	for a,b in zip(li,li1):
# 		tables.append({"name": a.value, "time": b.value, "row": a.row})
# 	return tables

# print(ul1)





