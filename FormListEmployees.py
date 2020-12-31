# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_list_employees.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vt_connection import vtConnection


class Ui_FormListEmployees(object):
    def setupUi(self, FormListEmployees):
        FormListEmployees.setObjectName("FormListEmployees")
        FormListEmployees.resize(914, 504)
        FormListEmployees.setMaximumSize(QtCore.QSize(1000, 504))
        self.tableEmployees = QtWidgets.QTableWidget(FormListEmployees)
        self.tableEmployees.setGeometry(QtCore.QRect(0, 90, 911, 371))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableEmployees.sizePolicy().hasHeightForWidth())
        self.tableEmployees.setSizePolicy(sizePolicy)
        self.tableEmployees.setGridStyle(QtCore.Qt.SolidLine)
        self.tableEmployees.setObjectName("tableEmployees")
        self.tableEmployees.setColumnCount(9)
        self.tableEmployees.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEmployees.setHorizontalHeaderItem(8, item)
        self.tableEmployees.horizontalHeader().setDefaultSectionSize(100)
        self.labelTitle = QtWidgets.QLabel(FormListEmployees)
        self.labelTitle.setGeometry(QtCore.QRect(270, 10, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.comboBoxSearchType = QtWidgets.QComboBox(FormListEmployees)
        self.comboBoxSearchType.setGeometry(QtCore.QRect(10, 50, 100, 25))
        self.comboBoxSearchType.setObjectName("comboBoxSearchType")
        self.comboBoxSearchType.addItem("")
        self.comboBoxSearchType.addItem("")
        self.comboBoxSearchType.addItem("")
        self.comboBoxSearchType.addItem("")
        self.comboBoxSearchType.addItem("")
        self.comboBoxSearchType.addItem("")
        self.lineEditSearchEmployees = QtWidgets.QLineEdit(FormListEmployees)
        self.lineEditSearchEmployees.setGeometry(QtCore.QRect(120, 50, 150, 25))
        self.lineEditSearchEmployees.setObjectName("lineEditSearchEmployees")
        self.pushButtonSearch = QtWidgets.QPushButton(FormListEmployees)
        self.pushButtonSearch.setGeometry(QtCore.QRect(280, 50, 80, 25))
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.pushButtonListAllEmployees = QtWidgets.QPushButton(FormListEmployees)
        self.pushButtonListAllEmployees.setGeometry(QtCore.QRect(770, 50, 131, 25))
        self.pushButtonListAllEmployees.setObjectName("pushButtonListAllEmployees")
        self.pushButtonUpdate = QtWidgets.QPushButton(FormListEmployees)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(0, 462, 170, 40))
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.tableEmployees.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableEmployees.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.retranslateUi(FormListEmployees)
        QtCore.QMetaObject.connectSlotsByName(FormListEmployees)

    def retranslateUi(self, FormListEmployees):
        _translate = QtCore.QCoreApplication.translate
        FormListEmployees.setWindowTitle(_translate("FormListEmployees", "Form"))
        self.tableEmployees.setSortingEnabled(False)
        item = self.tableEmployees.horizontalHeaderItem(0)
        item.setText(_translate("FormListEmployees", "Tc No"))
        item = self.tableEmployees.horizontalHeaderItem(1)
        item.setText(_translate("FormListEmployees", "İsim"))
        item = self.tableEmployees.horizontalHeaderItem(2)
        item.setText(_translate("FormListEmployees", "Meslek"))
        item = self.tableEmployees.horizontalHeaderItem(3)
        item.setText(_translate("FormListEmployees", "Tecrübe"))
        item = self.tableEmployees.horizontalHeaderItem(4)
        item.setText(_translate("FormListEmployees", "Eğitim"))
        item = self.tableEmployees.horizontalHeaderItem(5)
        item.setText(_translate("FormListEmployees", "Sicil"))
        item = self.tableEmployees.horizontalHeaderItem(6)
        item.setText(_translate("FormListEmployees", "Engel Durumu"))
        item = self.tableEmployees.horizontalHeaderItem(7)
        item.setText(_translate("FormListEmployees", "Medeni Hali"))
        item = self.tableEmployees.horizontalHeaderItem(8)
        item.setText(_translate("FormListEmployees", "Şirket Adı"))
        self.labelTitle.setText(_translate("FormListEmployees", "Kayıtlı İş Sahibi Çalışanlar"))
        self.comboBoxSearchType.setItemText(0, _translate("FormListEmployees", "Tc No"))
        self.comboBoxSearchType.setItemText(1, _translate("FormListEmployees", "Isim"))
        self.comboBoxSearchType.setItemText(2, _translate("FormListEmployees", "Meslek"))
        self.comboBoxSearchType.setItemText(3, _translate("FormListEmployees", "Tecrube"))
        self.comboBoxSearchType.setItemText(4, _translate("FormListEmployees", "Egitim"))
        self.comboBoxSearchType.setItemText(5, _translate("FormListEmployees", "Şirket Adı"))
        self.pushButtonSearch.setText(_translate("FormListEmployees", "Ara"))
        self.pushButtonListAllEmployees.setText(_translate("FormListEmployees", "Tüm Kayıtları Getir"))
        self.pushButtonUpdate.setText(_translate("FormListEmployees", "Güncelle"))
        self.listAllEmployees()
        self.pushButtonUpdate.clicked.connect(self.updateSelectedEmployee)
        self.pushButtonSearch.clicked.connect(self.listFilteredEmployees)
        self.pushButtonListAllEmployees.clicked.connect(self.listAllEmployees)
     
    def updateSelectedEmployee(self):
        print("Güncelle")

    def listAllEmployees(self):
        employees_data = vtConnection.readEmployees()
        self.tableEmployees.clearContents()
        self.tableEmployees.setRowCount(0)
        i = 0
        for employee_data in employees_data:
            print(employee_data)
            self.tableEmployees.insertRow(i)
            self.tableEmployees.setItem(i, 0, QtWidgets.QTableWidgetItem(str(employee_data['ssn'])))
            self.tableEmployees.setItem(i, 1, QtWidgets.QTableWidgetItem(employee_data['name_']))
            self.tableEmployees.setItem(i, 2, QtWidgets.QTableWidgetItem(employee_data['job']))
            self.tableEmployees.setItem(i, 3, QtWidgets.QTableWidgetItem(str(employee_data['experience'])))
            self.tableEmployees.setItem(i, 4, QtWidgets.QTableWidgetItem(employee_data['grad_level']))
            if employee_data['registery']:
                self.tableEmployees.setItem(i, 5, QtWidgets.QTableWidgetItem('Temiz'))
            else:
                self.tableEmployees.setItem(i, 5, QtWidgets.QTableWidgetItem('Temiz Değil'))
            self.tableEmployees.setItem(i, 6, QtWidgets.QTableWidgetItem(str(employee_data['disable_level'])))
            if employee_data['marriage']:
                self.tableEmployees.setItem(i, 7, QtWidgets.QTableWidgetItem('Evli'))
            else:
                self.tableEmployees.setItem(i, 7, QtWidgets.QTableWidgetItem('Bekar'))
            self.tableEmployees.setItem(i, 8, QtWidgets.QTableWidgetItem(employee_data['firm_name']))
            i = i + 1


    def listFilteredEmployees(self):
        filterValue = self.lineEditSearchEmployees.text()
        if self.comboBoxSearchType.currentText() == 'Tc No':
            filterType = 'ssn'
        elif self.comboBoxSearchType.currentText() == 'Isim':
            filterType = 'name_'
        elif self.comboBoxSearchType.currentText() == 'Meslek':
            filterType = 'job'
        elif self.comboBoxSearchType.currentText() == 'Tecrube':
            if not filterValue.isnumeric():
                return print('Tecrübe tam sayı formatında olmalıdır.')
            filterType = 'experience'
        else:
            filterType = 'grad_level'

        print(filterType)

        employees_data = vtConnection.filterAndReadEmployees(filterType, filterValue)


        self.tableEmployees.clearContents()
        self.tableEmployees.setRowCount(0)
        i = 0
        for employee_data in employees_data:
            print(employees_data)
            self.tableEmployees.insertRow(i)
            self.tableEmployees.setItem(i, 0, QtWidgets.QTableWidgetItem(str(employee_data['ssn'])))
            self.tableEmployees.setItem(i, 1, QtWidgets.QTableWidgetItem(employee_data['name_']))
            self.tableEmployees.setItem(i, 2, QtWidgets.QTableWidgetItem(employee_data['job']))
            self.tableEmployees.setItem(i, 3, QtWidgets.QTableWidgetItem(employee_data['experience']))
            self.tableEmployees.setItem(i, 4, QtWidgets.QTableWidgetItem(employee_data['grad_level']))
            if employee_data['registery']:
                self.tableEmployees.setItem(i, 5, QtWidgets.QTableWidgetItem('Temiz'))
            else:
                self.tableEmployees.setItem(i, 5, QtWidgets.QTableWidgetItem('Temiz Değil'))
            self.tableEmployees.setItem(i, 6, QtWidgets.QTableWidgetItem(str(employee_data['disable_level'])))
            if employee_data['marriage']:
                self.tableEmployees.setItem(i, 7, QtWidgets.QTableWidgetItem('Evli'))
            else:
                self.tableEmployees.setItem(i, 7, QtWidgets.QTableWidgetItem('Bekar'))
            self.tableEmployees.setItem(i, 8, QtWidgets.QTableWidgetItem(employee_data['name_']))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormListEmployees = QtWidgets.QWidget()
    ui = Ui_FormListEmployees()
    ui.setupUi(FormListEmployees)
    FormListEmployees.show()
    sys.exit(app.exec_())

