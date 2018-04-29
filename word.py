# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'word.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_levio_word(object):
    def setupUi(self, levio_word):
        levio_word.setObjectName("levio_word")
        levio_word.resize(437, 477)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pictures/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        levio_word.setWindowIcon(icon)
        self.textEdit = QtWidgets.QTextEdit(levio_word)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 291, 41))
        self.textEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.textEdit.setObjectName("textEdit")
        self.input_word = QtWidgets.QPushButton(levio_word)
        self.input_word.setGeometry(QtCore.QRect(80, 90, 121, 51))
        self.input_word.setObjectName("input_word")
        self.clear = QtWidgets.QPushButton(levio_word)
        self.clear.setGeometry(QtCore.QRect(250, 90, 121, 51))
        self.clear.setObjectName("clear")
        self.retract_add = QtWidgets.QPushButton(levio_word)
        self.retract_add.setGeometry(QtCore.QRect(80, 160, 121, 51))
        self.retract_add.setObjectName("retract_add")
        self.list_hard = QtWidgets.QPushButton(levio_word)
        self.list_hard.setGeometry(QtCore.QRect(250, 160, 121, 51))
        self.list_hard.setObjectName("list_hard")
        self.listWidget = QtWidgets.QListWidget(levio_word)
        self.listWidget.setGeometry(QtCore.QRect(70, 250, 331, 201))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.re = QtWidgets.QPushButton(levio_word)
        self.re.setGeometry(QtCore.QRect(350, 30, 41, 41))
        self.re.setObjectName("re")

        self.retranslateUi(levio_word)
        QtCore.QMetaObject.connectSlotsByName(levio_word)

    def retranslateUi(self, levio_word):
        _translate = QtCore.QCoreApplication.translate
        levio_word.setWindowTitle(_translate("levio_word", "深刻单词本"))
        self.input_word.setText(_translate("levio_word", "添加单词"))
        self.clear.setText(_translate("levio_word", "清空列表"))
        self.retract_add.setText(_translate("levio_word", "撤销添加"))
        self.list_hard.setText(_translate("levio_word", "难点单词"))
        self.re.setText(_translate("levio_word", "re"))

