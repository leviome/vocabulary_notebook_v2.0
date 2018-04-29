#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: liaoliwei
@contact: levio@pku.edu.cn
@file: read_excel.py
@time: 2018/4/12 16:48
"""
import xlrd


def open_excel(file='file.xls'):
	try:
		data = xlrd.open_workbook(file)
		return data
	except Exception as e:
		print(str(e))


def excel_table_byname(data,
                       colnameindex=0,
                       by_name=u'Sheet1'):
	table = data.sheet_by_name(by_name)  # 获得表格
	nrows = table.nrows  # 拿到总共行数
	colnames = table.row_values(colnameindex) # list
	list = []
	for rownum in range(1, nrows):
		row = table.row_values(rownum)
		if row:
			app = {}
			for i in range(len(colnames)):
				app[colnames[i]] = row[i]
			# 表头与数据对应
			list.append(app)
	return list


def main():
	workbook = open_excel(u'C:\\Users\\levio\\Desktop\\vocabulary\\hard_words.xlsx')
	tables = excel_table_byname(workbook)
	# print(tables)
	for row in tables:
		print(row)

if __name__ == "__main__":
	main()
