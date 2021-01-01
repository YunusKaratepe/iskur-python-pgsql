# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_create_todo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vt_connection import vtConnection

class Ui_FormTodo(object):
    def setupUi(self, FormTodo):
        FormTodo.setObjectName("FormTodo")
        FormTodo.resize(400, 224)
        self.textEditTodo = QtWidgets.QTextEdit(FormTodo)
        self.textEditTodo.setGeometry(QtCore.QRect(10, 60, 371, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEditTodo.setFont(font)
        self.textEditTodo.setObjectName("textEditTodo")
        self.pushButtonCreate = QtWidgets.QPushButton(FormTodo)
        self.pushButtonCreate.setGeometry(QtCore.QRect(300, 182, 80, 31))
        self.pushButtonCreate.setObjectName("pushButtonCreate")
        self.label = QtWidgets.QLabel(FormTodo)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(FormTodo)
        QtCore.QMetaObject.connectSlotsByName(FormTodo)

    def retranslateUi(self, FormTodo):
        _translate = QtCore.QCoreApplication.translate
        FormTodo.setWindowTitle(_translate("FormTodo", "Form"))
        self.pushButtonCreate.setText(_translate("FormTodo", "Oluştur"))
        self.label.setText(_translate("FormTodo", "Yapılacak İş:"))
