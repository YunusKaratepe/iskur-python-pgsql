# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_list_firms.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vt_connection import vtConnection
import FormUpdateFirm

class Ui_FormListFirms(object):
    def setupUi(self, FormListFirms):
        FormListFirms.setObjectName("FormListFirms")
        FormListFirms.resize(857, 525)
        self.tableWidgetListFirms = QtWidgets.QTableWidget(FormListFirms)
        self.tableWidgetListFirms.setGeometry(QtCore.QRect(0, 80, 857, 400))
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
        self.label = QtWidgets.QLabel(FormListFirms)
        self.label.setGeometry(QtCore.QRect(370, 10, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditSearchFirm = QtWidgets.QLineEdit(FormListFirms)
        self.lineEditSearchFirm.setGeometry(QtCore.QRect(110, 50, 141, 23))
        self.lineEditSearchFirm.setObjectName("lineEditSearchFirm")

        self.lineEditListFirmsHavingEmployee = QtWidgets.QSpinBox(FormListFirms)
        self.lineEditListFirmsHavingEmployee.setGeometry(QtCore.QRect(450, 50, 80, 23))
        self.lineEditListFirmsHavingEmployee.setObjectName("lineEditListFirmsHavingEmployee")


        self.comboBoxSearchFirm = QtWidgets.QComboBox(FormListFirms)
        self.comboBoxSearchFirm.setGeometry(QtCore.QRect(10, 50, 91, 23))
        self.comboBoxSearchFirm.setObjectName("comboBoxSearchFirm")
        self.comboBoxSearchFirm.addItem("")
        self.comboBoxSearchFirm.addItem("")
        self.pushButtonSearchFirm = QtWidgets.QPushButton(FormListFirms)
        self.pushButtonSearchFirm.setGeometry(QtCore.QRect(260, 50, 80, 23))
        self.pushButtonSearchFirm.setObjectName("pushButtonSearchFirm")

        self.pushButtonSearchFirmsHavingEmployee = QtWidgets.QPushButton(FormListFirms)
        self.pushButtonSearchFirmsHavingEmployee.setGeometry(QtCore.QRect(535, 50, 210, 23))
        self.pushButtonSearchFirmsHavingEmployee.setObjectName("pushButtonSearchFirmsHavingEmployee")

        self.pushButtonUpdate = QtWidgets.QPushButton(FormListFirms)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(700, 485, 150, 30))
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.pushButtonRefreshList = QtWidgets.QPushButton(FormListFirms)
        self.pushButtonRefreshList.setGeometry(QtCore.QRect(760, 50, 80, 23))
        self.pushButtonRefreshList.setObjectName("pushButtonRefreshList")
        self.tableWidgetListFirms.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetListFirms.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.retranslateUi(FormListFirms)
        QtCore.QMetaObject.connectSlotsByName(FormListFirms)

    def retranslateUi(self, FormListFirms):
        _translate = QtCore.QCoreApplication.translate
        FormListFirms.setWindowTitle(_translate("FormListFirms", "Form"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(0)
        item.setText(_translate("FormListFirms", "ID"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(1)
        item.setText(_translate("FormListFirms", "İsim"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(2)
        item.setText(_translate("FormListFirms", "Adres"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(3)
        item.setText(_translate("FormListFirms", "Telefon"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(4)
        item.setText(_translate("FormListFirms", "Eğitim Gereksinimi"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(5)
        item.setText(_translate("FormListFirms", "Engel İzni"))
        item = self.tableWidgetListFirms.horizontalHeaderItem(6)
        item.setText(_translate("FormListFirms", "Sicil Koşulu"))
        self.label.setText(_translate("FormListFirms", "Şirketler"))
        self.comboBoxSearchFirm.setItemText(0, _translate("FormListFirms", "ID"))
        self.comboBoxSearchFirm.setItemText(1, _translate("FormListFirms", "İsim"))
        self.pushButtonSearchFirm.setText(_translate("FormListFirms", "Ara"))
        self.pushButtonRefreshList.setText(_translate("FormListFirms", "Yenile"))
        self.pushButtonUpdate.setText(_translate("FormListFirms", "Seçileni Güncelle"))
        self.pushButtonSearchFirmsHavingEmployee.setText(_translate("FormListFirms", "Min. İşçiye Sahipleri Listele"))
        self.pushButtonSearchFirm.clicked.connect(self.listFilteredFirms)
        self.pushButtonRefreshList.clicked.connect(self.listAllFirms)
        self.pushButtonUpdate.clicked.connect(self.updateSelectedFirm)
        self.pushButtonSearchFirmsHavingEmployee.clicked.connect(self.listFirmsHavingEmployee)
        self.listAllFirms()

    def updateSelectedFirm(self):
        if not self.tableWidgetListFirms.selectedIndexes():
            messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Seçim', 'Önce seçim yapmalısınız.')
            messageBox.exec()
            return
        selected_firm = self.tableWidgetListFirms.selectedIndexes()
        self.FormUpdateFirm = QtWidgets.QWidget()
        self.FormUpdateFirm_ui = FormUpdateFirm.Ui_FormUpdateFirm()
        self.FormUpdateFirm_ui.setupUi(self.FormUpdateFirm)
        self.FormUpdateFirm_ui.lineEditFirmName.setText(selected_firm[1].data())
        self.FormUpdateFirm_ui.lineEditFirmAddress.setText(selected_firm[2].data())
        self.FormUpdateFirm_ui.lineEditFirmPhone.setText(selected_firm[3].data())
        self.FormUpdateFirm_ui.comboBoxEducation.setCurrentText(selected_firm[4].data())
        if selected_firm[5] == 'True':
            self.FormUpdateFirm_ui.radioButtonDisablePermission.setChecked(True)
        else:
            self.FormUpdateFirm_ui.radioButtonDisableNoPermission.setChecked(True)
        if selected_firm[6] == 'True':
            self.FormUpdateFirm_ui.radioButtonRegisteryRelax.setChecked(True)
        else:
            self.FormUpdateFirm_ui.radioButtonRegisteryStrict.setChecked(True)
        self.FormUpdateFirm_ui.firm_id = int(selected_firm[0].data())
        self.FormUpdateFirm_ui.label_10.setText(str(vtConnection.total_salary(int(selected_firm[0].data()))[0]['total_salary']))
        self.FormUpdateFirm.show()

    def listFirmsHavingEmployee(self):
        min_employee = self.lineEditListFirmsHavingEmployee.value()
        firms_data = vtConnection.hires_from_firm(min_employee)
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
        print(filterValue)
        if self.comboBoxSearchFirm.currentText() == 'ID':
            if not filterValue.isnumeric():
                return print('Firma id tam sayı formatında olmalıdır.')
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormListFirms = QtWidgets.QWidget()
    ui = Ui_FormListFirms()
    ui.setupUi(FormListFirms)
    FormListFirms.show()
    sys.exit(app.exec_())

