import xlwings as xw

wb = xw.Book('D:/test2.xls')

#wb.sheets['sheet1'].range('A1').value='rs'

#wb.sheets['sheet1'].range('D1').value='人生'
#wb.sheets['sheet1'].range('E1').value='苦短'
wb.save()

sht = wb.sheets['sheet1']
a = sht.range('A1').value
#b = sht.range('A1:R500').value

#读取全部数据
b = sht.range('A1:R1').expand().value

print(a)
print(b)
