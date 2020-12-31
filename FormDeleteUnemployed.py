# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_delete_unemployed.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vt_connection import vtConnection


class Ui_FormDeleteUnemployed(object):
    def setupUi(self, FormDeleteUnemployed):
        FormDeleteUnemployed.setObjectName("FormDeleteUnemployed")
        FormDeleteUnemployed.resize(1020, 504)
        FormDeleteUnemployed.setMaximumSize(QtCore.QSize(1020, 504))
        self.tableUnemployeds = QtWidgets.QTableWidget(FormDeleteUnemployed)
        self.tableUnemployeds.setGeometry(QtCore.QRect(0, 90, 1020, 371))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableUnemployeds.sizePolicy().hasHeightForWidth())
        self.tableUnemployeds.setSizePolicy(sizePolicy)
        self.tableUnemployeds.setGridStyle(QtCore.Qt.SolidLine)
        self.tableUnemployeds.setObjectName("tableUnemployeds")
        self.tableUnemployeds.setColumnCount(10)
        self.tableUnemployeds.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableUnemployeds.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUnemployeds.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUnemployeds.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUnemployeds.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUnemployeds.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUnemployeds.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUnemployeds.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUnemployeds.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUnemployeds.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUnemployeds.setHorizontalHeaderItem(9, item)
        self.tableUnemployeds.horizontalHeader().setDefaultSectionSize(100)
        self.labelTitle = QtWidgets.QLabel(FormDeleteUnemployed)
        self.labelTitle.setGeometry(QtCore.QRect(270, 10, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.pushButtonRemoveUnemployed = QtWidgets.QPushButton(FormDeleteUnemployed)
        self.pushButtonRemoveUnemployed.setGeometry(QtCore.QRect(0, 462, 170, 40))
        self.pushButtonRemoveUnemployed.setObjectName("pushButtonRemoveUnemployed")
        self.comboBoxSearchType = QtWidgets.QComboBox(FormDeleteUnemployed)
        self.comboBoxSearchType.setGeometry(QtCore.QRect(10, 50, 100, 25))
        self.comboBoxSearchType.setObjectName("comboBoxSearchType")
        self.comboBoxSearchType.addItem("")
        self.comboBoxSearchType.addItem("")
        self.comboBoxSearchType.addItem("")
        self.comboBoxSearchType.addItem("")
        self.comboBoxSearchType.addItem("")
        self.lineEditSearchUnemployed = QtWidgets.QLineEdit(FormDeleteUnemployed)
        self.lineEditSearchUnemployed.setGeometry(QtCore.QRect(120, 50, 150, 25))
        self.lineEditSearchUnemployed.setObjectName("lineEditSearchUnemployed")
        self.pushButtonSearch = QtWidgets.QPushButton(FormDeleteUnemployed)
        self.pushButtonSearch.setGeometry(QtCore.QRect(280, 50, 80, 25))
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.pushButtonListAllUnemployeds = QtWidgets.QPushButton(FormDeleteUnemployed)
        self.pushButtonListAllUnemployeds.setGeometry(QtCore.QRect(870, 50, 131, 25))
        self.pushButtonListAllUnemployeds.setObjectName("pushButtonListAllUnemployeds")
        self.tableUnemployeds.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.idListToDeleteUnemployeds = []

        self.retranslateUi(FormDeleteUnemployed)
        QtCore.QMetaObject.connectSlotsByName(FormDeleteUnemployed)

    def retranslateUi(self, FormDeleteUnemployed):
        _translate = QtCore.QCoreApplication.translate
        FormDeleteUnemployed.setWindowTitle(_translate("FormDeleteUnemployed", "Form"))
        self.tableUnemployeds.setSortingEnabled(False)
        item = self.tableUnemployeds.horizontalHeaderItem(0)
        item.setText(_translate("FormDeleteUnemployed", "Tc No"))
        item = self.tableUnemployeds.horizontalHeaderItem(1)
        item.setText(_translate("FormDeleteUnemployed", "İsim"))
        item = self.tableUnemployeds.horizontalHeaderItem(2)
        item.setText(_translate("FormDeleteUnemployed", "Meslek"))
        item = self.tableUnemployeds.horizontalHeaderItem(3)
        item.setText(_translate("FormDeleteUnemployed", "Tecrübe"))
        item = self.tableUnemployeds.horizontalHeaderItem(4)
        item.setText(_translate("FormDeleteUnemployed", "Eğitim"))
        item = self.tableUnemployeds.horizontalHeaderItem(5)
        item.setText(_translate("FormDeleteUnemployed", "Sicil"))
        item = self.tableUnemployeds.horizontalHeaderItem(6)
        item.setText(_translate("FormDeleteUnemployed", "Engel"))
        item = self.tableUnemployeds.horizontalHeaderItem(7)
        item.setText(_translate("FormDeleteUnemployed", "Medeni Hal"))
        item = self.tableUnemployeds.horizontalHeaderItem(8)
        item.setText(_translate("FormDeleteUnemployed", "Cinsiyet"))
        item = self.tableUnemployeds.horizontalHeaderItem(9)
        item.setText(_translate("FormDeleteUnemployed", "Doğum Tarihi"))
        self.labelTitle.setText(_translate("FormDeleteUnemployed", "Kayıtlu Başvuru Sil"))
        self.pushButtonRemoveUnemployed.setText(_translate("FormDeleteUnemployed", "Seçileni Sistemden Sil"))
        self.comboBoxSearchType.setItemText(0, _translate("FormDeleteUnemployed", "Tc No"))
        self.comboBoxSearchType.setItemText(1, _translate("FormDeleteUnemployed", "Isim"))
        self.comboBoxSearchType.setItemText(2, _translate("FormDeleteUnemployed", "Meslek"))
        self.comboBoxSearchType.setItemText(3, _translate("FormDeleteUnemployed", "Tecrube"))
        self.comboBoxSearchType.setItemText(4, _translate("FormDeleteUnemployed", "Egitim"))
        self.pushButtonSearch.setText(_translate("FormDeleteUnemployed", "Ara"))
        self.pushButtonListAllUnemployeds.setText(_translate("FormDeleteUnemployed", "Yenile"))
        self.listAllUnemployeds()
        self.pushButtonSearch.clicked.connect(self.listFilteredUnemployeds)
        self.pushButtonListAllUnemployeds.clicked.connect(self.listAllUnemployeds)
        self.pushButtonRemoveUnemployed.clicked.connect(self.deleteUnemployed)

    def deleteUnemployed(self):
        if not self.tableUnemployeds.selectedIndexes():
            return

        messageBox = QtWidgets.QMessageBox.question(None, 'Seçileni Sil', 'Silmek istediğinize emin misiniz?',
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        if messageBox == QtWidgets.QMessageBox.Yes:
            vtConnection.deleteWithSsnUnemployed(self.tableUnemployeds.selectedIndexes()[0].data())
            self.tableUnemployeds.removeRow(self.tableUnemployeds.currentRow())



    def listAllUnemployeds(self):
        unemployeds_data = vtConnection.readUnemployeds()
        self.tableUnemployeds.clearContents()
        self.tableUnemployeds.setRowCount(0)
        i = 0
        for undemployed_data in unemployeds_data:
            self.tableUnemployeds.insertRow(i)
            self.tableUnemployeds.setItem(i, 0, QtWidgets.QTableWidgetItem(str(undemployed_data['ssn'])))
            self.tableUnemployeds.setItem(i, 1, QtWidgets.QTableWidgetItem(undemployed_data['name_']))
            self.tableUnemployeds.setItem(i, 2, QtWidgets.QTableWidgetItem(undemployed_data['job']))
            self.tableUnemployeds.setItem(i, 3, QtWidgets.QTableWidgetItem(str(undemployed_data['experience'])))
            self.tableUnemployeds.setItem(i, 4, QtWidgets.QTableWidgetItem(undemployed_data['grad_level']))
            if undemployed_data['registery']:
                self.tableUnemployeds.setItem(i, 5, QtWidgets.QTableWidgetItem('Temiz'))
            else:
                self.tableUnemployeds.setItem(i, 5, QtWidgets.QTableWidgetItem('Temiz Değil'))
            self.tableUnemployeds.setItem(i, 6, QtWidgets.QTableWidgetItem(str(undemployed_data['disable_level'])))
            if undemployed_data['marriage']:
                self.tableUnemployeds.setItem(i, 7, QtWidgets.QTableWidgetItem('Evli'))
            else:
                self.tableUnemployeds.setItem(i, 7, QtWidgets.QTableWidgetItem('Bekar'))
            if undemployed_data['gender']:
                self.tableUnemployeds.setItem(i, 8, QtWidgets.QTableWidgetItem('Erkek'))
            else:
                self.tableUnemployeds.setItem(i, 8, QtWidgets.QTableWidgetItem('Kadın'))
            self.tableUnemployeds.setItem(i, 9, QtWidgets.QTableWidgetItem(str(undemployed_data['birthdate'])[0:10]))
            i = i + 1

    def listFilteredUnemployeds(self):
        filterValue = self.lineEditSearchUnemployed.text()
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

        unemployeds_data = vtConnection.filterAndReadUnemployeds(filterType, filterValue)

        self.tableUnemployeds.clearContents()
        self.tableUnemployeds.setRowCount(0)
        i = 0
        for undemployed_data in unemployeds_data:
            self.tableUnemployeds.insertRow(i)
            self.tableUnemployeds.setItem(i, 0, QtWidgets.QTableWidgetItem(str(undemployed_data['ssn'])))
            self.tableUnemployeds.setItem(i, 1, QtWidgets.QTableWidgetItem(undemployed_data['name_']))
            self.tableUnemployeds.setItem(i, 2, QtWidgets.QTableWidgetItem(undemployed_data['job']))
            self.tableUnemployeds.setItem(i, 3, QtWidgets.QTableWidgetItem(str(undemployed_data['experience'])))
            self.tableUnemployeds.setItem(i, 4, QtWidgets.QTableWidgetItem(undemployed_data['grad_level']))
            if undemployed_data['registery']:
                self.tableUnemployeds.setItem(i, 5, QtWidgets.QTableWidgetItem('Temiz'))
            else:
                self.tableUnemployeds.setItem(i, 5, QtWidgets.QTableWidgetItem('Temiz Değil'))
            self.tableUnemployeds.setItem(i, 6, QtWidgets.QTableWidgetItem(str(undemployed_data['disable_level'])))
            if undemployed_data['marriage']:
                self.tableUnemployeds.setItem(i, 7, QtWidgets.QTableWidgetItem('Evli'))
            else:
                self.tableUnemployeds.setItem(i, 7, QtWidgets.QTableWidgetItem('Bekar'))
            i = i + 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormDeleteUnemployed = QtWidgets.QWidget()
    ui = Ui_FormDeleteUnemployed()
    ui.setupUi(FormDeleteUnemployed)
    FormDeleteUnemployed.show()
    sys.exit(app.exec_())

