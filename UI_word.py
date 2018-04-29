#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: liaoliwei
@contact: levio@pku.edu.cn
@file: UI_word.py
@time: 2018/4/27 22:03
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from toefl_words.Topfile import Top_file, sort_vocab, LIST_LENGTH
from word import Ui_levio_word


def judge_pure_english(keyword):
	return all((ord(c) <= 122 and ord(c) >= 97)  # 小写字母
			   or (ord(c) >= 65 and ord(c) <= 90)  # 大写字母
			   for c in keyword)


class Dialog(QDialog, Ui_levio_word):
	def __init__(self, parent=None):
		super(Dialog, self).__init__(parent)
		self.setupUi(self)

	@pyqtSlot()
	def on_input_word_clicked(self):
		n = self.listWidget.__len__()
		if n == LIST_LENGTH:
			QMessageBox.information(self, u'提示', u'无法添加，请点击清空输入')
		else:
			pe = self.textEdit.toPlainText()
			if judge_pure_english(pe) and len(pe) != 0:
				res_type, times = Top_file(pe)
				if res_type:
					self.listWidget.addItem(pe)
					res_str = '单词:' + pe + ' 为新添加单词！'
					QMessageBox.information(self, u'提示', res_str)
				else:
					item_str = pe + '\t\t('+str(int(times))+')'
					self.listWidget.addItem(item_str)
					res_str = ('单词:' + pe + ' 已重复记录 ' +
							   str(int(times)) + ' 次！')
					QMessageBox.information(self, u'提示', res_str)
			else:
				QMessageBox.information(self, u'提示', '请输入正确的英文单词')

	@pyqtSlot()
	def on_clear_clicked(self):
		self.listWidget.clear()

	@pyqtSlot()
	def on_retract_add_clicked(self):
		n = self.listWidget.__len__()
		if n == LIST_LENGTH:
			QMessageBox.information(self, u'提示', u'列表单词无法删除，请点击清空输入')
		elif n == 0:
			QMessageBox.information(self, u'提示', u'请选择要删除单词')
		else:
			item_record = self.listWidget.currentItem()
			if item_record is None:
				QMessageBox.information(self, u'提示', u'请选择要删除单词')
				return
			item_word = item_record.text().split('\t')[0]
			Top_file(item_word, add_or_del = False)
			item = self.listWidget.takeItem(self.listWidget.currentRow())
			item = None

	@pyqtSlot()
	def on_re_clicked(self):
		self.textEdit.clear()

	@pyqtSlot()
	def on_list_hard_clicked(self):
		self.listWidget.clear()
		voc_list = sort_vocab()
		for word in voc_list:
			n =20 - len(word['Word'])
			# print()
			item_str = (word['Word'] + ' '*n + '\t(' +
						str(int(word['Times'])) + ')')
			self.listWidget.addItem(item_str)


if __name__ == '__main__':
	import sys

	app = QtWidgets.QApplication(sys.argv)
	# Dialog = QtWidgets.QDialog()
	app.processEvents()
	ui = Dialog()
	# ui.setupUi(Dialog)
	ui.show()
	sys.exit(app.exec_())
