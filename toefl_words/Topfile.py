#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: liaoliwei
@contact: levio@pku.edu.cn
@file: Topfile.py
@time: 2018/4/27 16:17
"""
from toefl_words import read_excel
# from toefl_words.change_excel import change_excel
from xlutils.copy import copy
# import os
LIST_LENGTH = 100

def Top_file(input_word,
			 add_or_del = True
			 # True表示添加单词，False表示删除单词
								):
	filename = 'new_excels.xls'
	excel = read_excel.open_excel(filename)
	tables = read_excel.excel_table_byname(excel)
	word_list = excel.sheet_by_name(u'Sheet1').col_values(0)[1:]
	if add_or_del:
		if input_word in word_list:
			word_index = word_list.index(input_word)
			times = tables[word_index]['Times']
			if times == '':
				content = 1
			else:
				content = times+1
			new_excel = copy(excel)
			new_excel.get_sheet(0).write(word_index+1, 1, content)
			# if os.path.exists('new_excels.xls'):
			# 	os.remove('new_excels.xls')
			new_excel.save('new_excels.xls')
			return False, content
		else:
			word_num = len(word_list)
			new_excel = copy(excel)
			new_excel.get_sheet(0).write(word_num + 1, 0, input_word)
			# if os.path.exists('new_excels.xls'):
			# 	os.remove('new_excels.xls')
			new_excel.save('new_excels.xls')
			return True, 0
	else:
		assert input_word in word_list
		word_index = word_list.index(input_word)
		times = tables[word_index]['Times']
		new_excel = copy(excel)
		if times == '':
			new_excel.get_sheet(0).write(word_index + 1, 0, '')
		elif times == 1:
			new_excel.get_sheet(0).write(word_index + 1, 1, '')
		else:
			new_excel.get_sheet(0).write(word_index + 1, 1, times-1)
		new_excel.save('new_excels.xls')

def sort_vocab():
	filename = 'new_excels.xls'
	excel = read_excel.open_excel(filename)
	tables = read_excel.excel_table_byname(excel)
	for member in tables:
		if type(member['Times']) == str:
			member['Times'] = 0
	##### 对表格进行冒泡排序 ######
	for i in range(len(tables)):
		for j in range(len(tables)-1):
			if tables[j]['Times']<tables[j+1]['Times']:
				temp = tables[j]
				tables[j] = tables[j+1]
				tables[j+1] = temp
	##### 对表格进行冒泡排序 ######
	return tables[0:LIST_LENGTH]
# sort_vocab()