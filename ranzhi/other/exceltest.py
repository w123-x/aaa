'''
演示如何操作Excel
Workbook 工作簿 文件名
Worksheet 工作表 sheet1、sheet2、sheet3
Cell 单元格 坐标
'''
import openpyxl

#打开工作簿
workbook = openpyxl.load_workbook(r'ranzhi\data.xlsx')

#打开指定的工作表
login_success=workbook['login_success']

'''
b=[]
for row in login_success:
    a=[]
    for cell in row:
        a.append(cell.value)
        # print(cell.value)
        print(a)
    b.append(tuple(a))
print(b)
'''

#列表生成式
r=[tuple(cell.value for cell in row) for row in login_success]
print(r)
















