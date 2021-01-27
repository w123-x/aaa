'''
演示如果操作Excel

Workbook 工作簿
Worksheet 工作表
Cell 单元格

'''

import openpyxl

# 打开工作簿
workbook = openpyxl.load_workbook(r'ranzhi\data.xlsx')

# 打开指定的工作表
login_success = workbook['login_success']

# [('admin','123456'),('user0','123456')]
r = []
for row in login_success:
    e = []
    for cell in row:
        e.append(cell.value)
    r.append(tuple(e))
print(r)
