# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_delete_firm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vt_connection import vtConnection


class Ui_FormDeleteFirm(object):
    def setupUi(self, FormDeleteFirm):
        FormDeleteFirm.setObjectName("FormDeleteFirm")
        FormDeleteFirm.resize(857, 533)
        self.tableWidgetListFirms = QtWidgets.QTableWidget(FormDeleteFirm)
        self.tableWidgetListFirms.setGeometry(QtCore.QRect(0, 80, 850, 400))
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
        self.tableWidgetListFirms.horizontalHeader().setDefaultSectionSize(120)
        self.label = QtWidgets.QLabel(FormDeleteFirm)
        self.label.setGeometry(QtCore.QRect(370, 10, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditSearchFirm = QtWidgets.QLineEdit(FormDeleteFirm)
        self.lineEditSearchFirm.setGeometry(QtCore.QRect(110, 50, 141, 23))
        self.lineEditSearchFirm.setObjectName("lineEditSearchFirm")
        self.comboBoxSearchFirm = QtWidgets.QComboBox(FormDeleteFirm)
        self.comboBoxSearchFirm.setGeometry(QtCore.QRect(10, 50, 91, 23))
        self.comboBoxSearchFirm.setObjectName("comboBoxSearchFirm")
        self.comboBoxSearchFirm.addItem("")
        self.comboBoxSearchFirm.addItem("")
        self.pushButtonSearchFirm = QtWidgets.QPushButton(FormDeleteFirm)
        self.pushButtonSearchFirm.setGeometry(QtCore.QRect(260, 50, 80, 23))
        self.pushButtonSearchFirm.setObjectName("pushButtonSearchFirm")
        self.pushButtonRefreshList = QtWidgets.QPushButton(FormDeleteFirm)
        self.pushButtonRefreshList.setGeometry(QtCore.QRect(760, 50, 80, 23))
        self.pushButtonRefreshList.setObjectName("pushButtonRefreshList")
        self.pushButtonDeleteSelectedFirm = QtWidgets.QPushButton(FormDeleteFirm)
        self.pushButtonDeleteSelectedFirm.setGeometry(QtCore.QRect(10, 490, 141, 30))
        self.pushButtonDeleteSelectedFirm.setObjectName("pushButtonDeleteSelectedFirm")
        self.tableWidgetListFirms.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetListFirms.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.idListToDeleteFirms = []
        self.retranslateUi(FormDeleteFirm)
        QtCore.QMetaObject.connectSlotsByName(FormDeleteFirm)

    def retranslateUi(self, FormDeleteFirm):
        _translate = QtCore.QCoreApplication.translate
        FormDeleteFirm.setWindowTitle(_translate("FormDeleteFirm", "Form"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(0)
        item.setText(_translate("FormDeleteFirm", "ID"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(1)
        item.setText(_translate("FormDeleteFirm", "İsim"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(2)
        item.setText(_translate("FormDeleteFirm", "Adres"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(3)
        item.setText(_translate("FormDeleteFirm", "Telefon"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(4)
        item.setText(_translate("FormDeleteFirm", "Eğitim Gereksinimi"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(5)
        item.setText(_translate("FormDeleteFirm", "Engel İzni"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(6)
        item.setText(_translate("FormDeleteFirm", "Sicil Koşulu"))
        self.label.setText(_translate("FormDeleteFirm", "Şirket Sil"))
        self.comboBoxSearchFirm.setItemText(0, _translate("FormDeleteFirm", "ID"))
        self.comboBoxSearchFirm.setItemText(1, _translate("FormDeleteFirm", "İsim"))
        self.pushButtonSearchFirm.setText(_translate("FormDeleteFirm", "Ara"))
        self.pushButtonRefreshList.setText(_translate("FormDeleteFirm", "Yenile"))
        self.pushButtonDeleteSelectedFirm.setText(_translate("FormDeleteFirm", "Seçileni Sil"))
        # select all firms
        self.listAllFirms()
        self.pushButtonRefreshList.clicked.connect(self.listAllFirms)
        self.pushButtonSearchFirm.clicked.connect(self.listFilteredFirms)
        self.pushButtonDeleteSelectedFirm.clicked.connect(self.deleteFirm)

    def listAllFirms(self):
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

    def listFilteredFirms(self):
        filterValue = self.lineEditSearchFirm.text()
        if self.comboBoxSearchFirm.currentText() == 'ID':
            filterType = 'id'
        else:
            filterType = 'name_'

        firms_data = vtConnection.filterAndReadFirms(filterType, filterValue)

        self.tableWidgetListFirms.clearContents()
        self.tableWidgetListFirms.setRowCount(0)

        if not firms_data:
            return

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

    def deleteFirm(self):
        if not self.tableWidgetListFirms.selectedIndexes():
            return print('Bir şey seçilmedi.')

        messageBox = QtWidgets.QMessageBox.question(None, 'Seçileni Sil', 'Silmek istediğinize emin misiniz?',
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        if messageBox == QtWidgets.QMessageBox.Yes:
            vtConnection.deleteWithIdFirm(int(self.tableWidgetListFirms.selectedIndexes()[0].data()))
            self.tableWidgetListFirms.removeRow(self.tableWidgetListFirms.currentRow())
        return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormDeleteFirm = QtWidgets.QWidget()
    ui = Ui_FormDeleteFirm()
    ui.setupUi(FormDeleteFirm)
    FormDeleteFirm.show()
    sys.exit(app.exec_())

