# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_create_interview.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vt_connection import vtConnection

class Ui_FormAddNewInterview(object):
    def setupUi(self, FormAddNewInterview):
        FormAddNewInterview.setObjectName("FormAddNewInterview")
        FormAddNewInterview.resize(984, 735)
        self.tableWidgetListFirms = QtWidgets.QTableWidget(FormAddNewInterview)
        self.tableWidgetListFirms.setGeometry(QtCore.QRect(20, 40, 941, 301))
        self.tableWidgetListFirms.setObjectName("tableWidgetListFirms")
        self.tableWidgetListFirms.setColumnCount(7)
        self.tableWidgetListFirms.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListFirms.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListFirms.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListFirms.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListFirms.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListFirms.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListFirms.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListFirms.setHorizontalHeaderItem(6, item)
        self.tableWidgetListFirms.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidgetListUnemployeds = QtWidgets.QTableWidget(FormAddNewInterview)
        self.tableWidgetListUnemployeds.setGeometry(QtCore.QRect(20, 390, 941, 301))
        self.tableWidgetListUnemployeds.setObjectName("tableWidgetListUnemployeds")
        self.tableWidgetListUnemployeds.setColumnCount(10)
        self.tableWidgetListUnemployeds.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUnemployeds.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUnemployeds.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUnemployeds.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUnemployeds.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUnemployeds.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUnemployeds.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUnemployeds.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUnemployeds.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUnemployeds.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListUnemployeds.setHorizontalHeaderItem(9, item)
        self.tableWidgetListUnemployeds.horizontalHeader().setDefaultSectionSize(91)
        self.label = QtWidgets.QLabel(FormAddNewInterview)
        self.label.setGeometry(QtCore.QRect(20, 10, 941, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FormAddNewInterview)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(FormAddNewInterview)
        self.label_3.setGeometry(QtCore.QRect(30, 360, 251, 16))
        self.label_3.setObjectName("label_3")
        self.pushButtonCreateInterview = QtWidgets.QPushButton(FormAddNewInterview)
        self.pushButtonCreateInterview.setGeometry(QtCore.QRect(790, 700, 171, 31))
        self.pushButtonCreateInterview.setObjectName("pushButtonCreateInterview")
        self.pushButtonListUnemployeds = QtWidgets.QPushButton(FormAddNewInterview)
        self.pushButtonListUnemployeds.setGeometry(QtCore.QRect(690, 350, 271, 31))
        self.pushButtonListUnemployeds.setObjectName("pushButtonListUnemployeds")

        self.retranslateUi(FormAddNewInterview)
        QtCore.QMetaObject.connectSlotsByName(FormAddNewInterview)

    def retranslateUi(self, FormAddNewInterview):
        _translate = QtCore.QCoreApplication.translate
        FormAddNewInterview.setWindowTitle(_translate("FormAddNewInterview", "Form"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(0)
        item.setText(_translate("FormAddNewInterview", "Firma ID"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(1)
        item.setText(_translate("FormAddNewInterview", "Firma Adı"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(2)
        item.setText(_translate("FormAddNewInterview", "Firma Adres"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(3)
        item.setText(_translate("FormAddNewInterview", "Firma Telefon"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(4)
        item.setText(_translate("FormAddNewInterview", "Eğitim Gereksinimi"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(5)
        item.setText(_translate("FormAddNewInterview", "Engel İzni"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(6)
        item.setText(_translate("FormAddNewInterview", "Sicil Koşulu"))
        item = self.tableWidgetListUnemployeds.horizontalHeaderItem(0)
        item.setText(_translate("FormAddNewInterview", "Tc No"))
        item = self.tableWidgetListUnemployeds.horizontalHeaderItem(1)
        item.setText(_translate("FormAddNewInterview", "İsim"))
        item = self.tableWidgetListUnemployeds.horizontalHeaderItem(2)
        item.setText(_translate("FormAddNewInterview", "Meslek"))
        item = self.tableWidgetListUnemployeds.horizontalHeaderItem(3)
        item.setText(_translate("FormAddNewInterview", "Tecrübe"))
        item = self.tableWidgetListUnemployeds.horizontalHeaderItem(4)
        item.setText(_translate("FormAddNewInterview", "Eğitim"))
        item = self.tableWidgetListUnemployeds.horizontalHeaderItem(5)
        item.setText(_translate("FormAddNewInterview", "Sicil"))
        item = self.tableWidgetListUnemployeds.horizontalHeaderItem(6)
        item.setText(_translate("FormAddNewInterview", "Engel"))
        item = self.tableWidgetListUnemployeds.horizontalHeaderItem(7)
        item.setText(_translate("FormAddNewInterview", "Medeni Hal"))
        item = self.tableWidgetListUnemployeds.horizontalHeaderItem(8)
        item.setText(_translate("FormAddNewInterview", "Cinsiyet"))
        item = self.tableWidgetListUnemployeds.horizontalHeaderItem(9)
        item.setText(_translate("FormAddNewInterview", "Doğum Tarihi"))
        self.label.setText(_translate("FormAddNewInterview", "Mülakat Oluştur"))
        self.label_2.setText(_translate("FormAddNewInterview", "Mülakata Alacak Firmalar:"))
        self.label_3.setText(_translate("FormAddNewInterview", "Mülakata Girecek Başvuru Sahipleri:"))
        self.pushButtonCreateInterview.setText(_translate("FormAddNewInterview", "Mülakatı Oluştur"))
        self.pushButtonListUnemployeds.setText(_translate("FormAddNewInterview", "Gereksinimlere Uyan Başvuruları Listele"))
        self.tableWidgetListUnemployeds.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetListUnemployeds.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidgetListFirms.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetListFirms.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.listFirms()
        self.listUnemployeds()
        self.pushButtonListUnemployeds.clicked.connect(self.listUnemployeds)
        self.pushButtonCreateInterview.clicked.connect(self.createNewInterview)

    def createNewInterview(self):
        if self.tableWidgetListFirms.selectedIndexes() and self.tableWidgetListUnemployeds.selectedIndexes():
            vtConnection.createNewInterview(int(self.tableWidgetListFirms.selectedIndexes()[0].data()),
                                            self.tableWidgetListUnemployeds.selectedIndexes()[0].data())
        else:
            return print('Hem firma hem de işçi seçilmelidir.')

    def listFirms(self):
        firms_data = vtConnection.readFirms()
        self.tableWidgetListFirms.clearContents()
        self.tableWidgetListFirms.setRowCount(0)
        i = 0
        for firm_data in firms_data:
            self.tableWidgetListFirms.insertRow(i)
            self.tableWidgetListFirms.setItem(i, 0, QtWidgets.QTableWidgetItem(str(firm_data['id'])))
            self.tableWidgetListFirms.setItem(i, 1, QtWidgets.QTableWidgetItem(firm_data['name_']))
            self.tableWidgetListFirms.setItem(i, 2, QtWidgets.QTableWidgetItem(firm_data['address']))
            self.tableWidgetListFirms.setItem(i, 3, QtWidgets.QTableWidgetItem(firm_data['phone']))
            self.tableWidgetListFirms.setItem(i, 4, QtWidgets.QTableWidgetItem(firm_data['req_grad_level']))
            self.tableWidgetListFirms.setItem(i, 5, QtWidgets.QTableWidgetItem(str(firm_data['disable_permission'])))
            if firm_data['registery_permission']:
                self.tableWidgetListFirms.setItem(i, 6, QtWidgets.QTableWidgetItem('Serbest'))
            else:
                self.tableWidgetListFirms.setItem(i, 6, QtWidgets.QTableWidgetItem('Katı'))
            i = i + 1
        self.tableWidgetListFirms.sortItems(0, QtCore.Qt.DescendingOrder)

    def listUnemployeds(self):
        if self.tableWidgetListFirms.selectedIndexes():
            unemployeds_data = vtConnection.listUnemployedsByRequirementsOfFirm(int(self.tableWidgetListFirms.
                                                                                    selectedIndexes()[0].data()))
        else:
            unemployeds_data = vtConnection.readUnemployeds()
        self.tableWidgetListUnemployeds.clearContents()
        self.tableWidgetListUnemployeds.setRowCount(0)
        i = 0
        for unemployed_data in unemployeds_data:
            self.tableWidgetListUnemployeds.insertRow(i)
            self.tableWidgetListUnemployeds.setItem(i, 0, QtWidgets.QTableWidgetItem(str(unemployed_data['ssn'])))
            self.tableWidgetListUnemployeds.setItem(i, 1, QtWidgets.QTableWidgetItem(unemployed_data['name_']))
            self.tableWidgetListUnemployeds.setItem(i, 2, QtWidgets.QTableWidgetItem(unemployed_data['job']))
            self.tableWidgetListUnemployeds.setItem(i, 3, QtWidgets.QTableWidgetItem(str(unemployed_data['experience'])))
            self.tableWidgetListUnemployeds.setItem(i, 4, QtWidgets.QTableWidgetItem(unemployed_data['grad_level']))
            if unemployed_data['registery']:
                self.tableWidgetListUnemployeds.setItem(i, 5, QtWidgets.QTableWidgetItem('Temiz'))
            else:
                self.tableWidgetListUnemployeds.setItem(i, 5, QtWidgets.QTableWidgetItem('Temiz Değil'))
            self.tableWidgetListUnemployeds.setItem(i, 6, QtWidgets.QTableWidgetItem(str(unemployed_data['disable_level'])))
            if unemployed_data['marriage']:
                self.tableWidgetListUnemployeds.setItem(i, 7, QtWidgets.QTableWidgetItem('Evli'))
            else:
                self.tableWidgetListUnemployeds.setItem(i, 7, QtWidgets.QTableWidgetItem('Bekar'))
            if unemployed_data['gender']:
                self.tableWidgetListUnemployeds.setItem(i, 8, QtWidgets.QTableWidgetItem('Erkek'))
            else:
                self.tableWidgetListUnemployeds.setItem(i, 8, QtWidgets.QTableWidgetItem('Kadın'))
            self.tableWidgetListUnemployeds.setItem(i, 9, QtWidgets.QTableWidgetItem(str(unemployed_data['birthdate'])[0:10]))
            i = i + 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormAddNewInterview = QtWidgets.QWidget()
    ui = Ui_FormAddNewInterview()
    ui.setupUi(FormAddNewInterview)
    FormAddNewInterview.show()
    sys.exit(app.exec_())

