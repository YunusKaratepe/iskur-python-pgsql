# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_list_unemployeds.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vt_connection import vtConnection
import FormUpdateUnemployed

class Ui_FormListUnemployeds(object):
    def setupUi(self, FormListUnemployeds):
        FormListUnemployeds.setObjectName("FormListUnemployeds")
        FormListUnemployeds.resize(1020, 504)
        FormListUnemployeds.setMaximumSize(QtCore.QSize(1020, 504))
        self.tableUnemployeds = QtWidgets.QTableWidget(FormListUnemployeds)
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
        self.labelTitle = QtWidgets.QLabel(FormListUnemployeds)
        self.labelTitle.setGeometry(QtCore.QRect(320, 10, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.comboBoxSearchType = QtWidgets.QComboBox(FormListUnemployeds)
        self.comboBoxSearchType.setGeometry(QtCore.QRect(10, 50, 100, 25))
        self.comboBoxSearchType.setObjectName("comboBoxSearchType")
        self.comboBoxSearchType.addItem("")
        self.comboBoxSearchType.addItem("")
        self.comboBoxSearchType.addItem("")
        self.comboBoxSearchType.addItem("")
        self.comboBoxSearchType.addItem("")
        self.lineEditSearchUnemployed = QtWidgets.QLineEdit(FormListUnemployeds)
        self.lineEditSearchUnemployed.setGeometry(QtCore.QRect(120, 50, 150, 25))
        self.lineEditSearchUnemployed.setObjectName("lineEditSearchUnemployed")
        self.pushButtonSearch = QtWidgets.QPushButton(FormListUnemployeds)
        self.pushButtonSearch.setGeometry(QtCore.QRect(280, 50, 80, 25))
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.pushButtonListAllUnemployeds = QtWidgets.QPushButton(FormListUnemployeds)
        self.pushButtonListAllUnemployeds.setGeometry(QtCore.QRect(870, 50, 131, 25))
        self.pushButtonListAllUnemployeds.setObjectName("pushButtonListAllUnemployeds")
        self.pushButtonUpdate = QtWidgets.QPushButton(FormListUnemployeds)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(840, 462, 170, 40))
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")

        self.labelAvgAge = QtWidgets.QLabel(FormListUnemployeds)
        self.labelAvgAge.setGeometry(QtCore.QRect(10, 462, 130, 40))
        self.labelAvgAge.setObjectName("labelAvgAge")

        self.labelAvgAgeValue = QtWidgets.QLabel(FormListUnemployeds)
        self.labelAvgAgeValue.setGeometry(QtCore.QRect(140, 462, 130, 40))
        self.labelAvgAgeValue.setObjectName("labelAvgAgeValue")

        self.tableUnemployeds.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.retranslateUi(FormListUnemployeds)
        QtCore.QMetaObject.connectSlotsByName(FormListUnemployeds)

    def retranslateUi(self, FormListUnemployeds):
        _translate = QtCore.QCoreApplication.translate
        FormListUnemployeds.setWindowTitle(_translate("FormListUnemployeds", "Form"))
        self.tableUnemployeds.setSortingEnabled(False)
        item = self.tableUnemployeds.horizontalHeaderItem(0)
        item.setText(_translate("FormListUnemployeds", "Tc No"))
        item = self.tableUnemployeds.horizontalHeaderItem(1)
        item.setText(_translate("FormListUnemployeds", "İsim"))
        item = self.tableUnemployeds.horizontalHeaderItem(2)
        item.setText(_translate("FormListUnemployeds", "Meslek"))
        item = self.tableUnemployeds.horizontalHeaderItem(3)
        item.setText(_translate("FormListUnemployeds", "Tecrübe"))
        item = self.tableUnemployeds.horizontalHeaderItem(4)
        item.setText(_translate("FormListUnemployeds", "Eğitim"))
        item = self.tableUnemployeds.horizontalHeaderItem(5)
        item.setText(_translate("FormListUnemployeds", "Sicil"))
        item = self.tableUnemployeds.horizontalHeaderItem(6)
        item.setText(_translate("FormListUnemployeds", "Engel"))
        item = self.tableUnemployeds.horizontalHeaderItem(7)
        item.setText(_translate("FormListUnemployeds", "Medeni Hal"))
        item = self.tableUnemployeds.horizontalHeaderItem(8)
        item.setText(_translate("FormListUnemployeds", "Cinsiyet"))
        item = self.tableUnemployeds.horizontalHeaderItem(9)
        item.setText(_translate("FormListUnemployeds", "Doğum Tarihi"))
        self.labelTitle.setText(_translate("FormListUnemployeds", "Kayıtlı Başvurular"))
        self.comboBoxSearchType.setItemText(0, _translate("FormListUnemployeds", "Tc No"))
        self.comboBoxSearchType.setItemText(1, _translate("FormListUnemployeds", "Isim"))
        self.comboBoxSearchType.setItemText(2, _translate("FormListUnemployeds", "Meslek"))
        self.comboBoxSearchType.setItemText(3, _translate("FormListUnemployeds", "Tecrube"))
        self.comboBoxSearchType.setItemText(4, _translate("FormListUnemployeds", "Egitim"))
        self.pushButtonSearch.setText(_translate("FormListUnemployeds", "Ara"))
        self.pushButtonListAllUnemployeds.setText(_translate("FormListUnemployeds", "Yenile"))
        self.pushButtonUpdate.setText(_translate("FormListUnemployeds", "Seçileni Güncelle"))
        self.labelAvgAge.setText(_translate("FormListUnemployeds", "Ortalama Yaş:"))
        self.labelAvgAgeValue.setText(_translate("FormListUnemployeds", "0.0"))
        self.tableUnemployeds.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableUnemployeds.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.listAllUnemployeds()
        self.pushButtonListAllUnemployeds.clicked.connect(self.listAllUnemployeds)
        self.pushButtonSearch.clicked.connect(self.listFilteredUnemployeds)
        self.pushButtonUpdate.clicked.connect(self.openFormUpdateUnemployed)

    def openFormUpdateUnemployed(self):
        if self.tableUnemployeds.selectedIndexes():
            selected = self.tableUnemployeds.selectedIndexes()
            self.FormUpdateUnemployed = QtWidgets.QWidget()
            self.FormUpdateUnemployed_ui = FormUpdateUnemployed.Ui_FormUpdateUnemployed()
            self.FormUpdateUnemployed_ui.setupUi(self.FormUpdateUnemployed)
            self.FormUpdateUnemployed_ui.lineEditPersonTcNo.setText(selected[0].data())
            self.FormUpdateUnemployed_ui.lineEditPersonTcNo.setReadOnly(True)
            self.FormUpdateUnemployed_ui.lineEditPersonName.setText(selected[1].data())
            self.FormUpdateUnemployed_ui.lineEditPersonJob.setText(selected[2].data())
            self.FormUpdateUnemployed_ui.spinBoxExperience.setValue(int(selected[3].data()))
            self.FormUpdateUnemployed_ui.comboBoxEducation.setCurrentText(selected[4].data())
            if selected[5].data() == 'Temiz':
                self.FormUpdateUnemployed_ui.radioButtonRegisteryClean.setChecked(True)
            else:
                self.FormUpdateUnemployed_ui.radioButtonRegisteryNotClean.setChecked(True)
            if selected[6].data() == 'True':
                self.FormUpdateUnemployed_ui.radioButtonDisabled.setChecked(True)
            else:
                self.FormUpdateUnemployed_ui.radioButtonNotDisabled.setChecked(True)
            if selected[7].data() == 'Evli':
                self.FormUpdateUnemployed_ui.radioButtonMarried.setChecked(True)
            else:
                self.FormUpdateUnemployed_ui.radioButtonSingle.setChecked(True)
            if selected[8].data() == 'Erkek':
                self.FormUpdateUnemployed_ui.radioButtonGenderMale.setChecked(True)
            else:
                self.FormUpdateUnemployed_ui.radioButtonGenderFemale.setChecked(True)
            date = selected[9].data().split('-')
            self.FormUpdateUnemployed_ui.dateEditBirthday.setDate(QtCore.QDate(int(date[0]), int(date[1]), int(date[2])))
            self.FormUpdateUnemployed.show()

    def listAllUnemployeds(self):
        unemployeds_data = vtConnection.readUnemployeds()
        self.tableUnemployeds.clearContents()
        self.tableUnemployeds.setRowCount(0)
        if not unemployeds_data:
            self.labelAvgAgeValue.setText('0.0')
            return
        self.labelAvgAgeValue.setText(str(vtConnection.avg_age()[0]['avg']))
        i = 0
        for unemployed_data in unemployeds_data:
            self.tableUnemployeds.insertRow(i)
            self.tableUnemployeds.setItem(i, 0, QtWidgets.QTableWidgetItem(str(unemployed_data['ssn'])))
            self.tableUnemployeds.setItem(i, 1, QtWidgets.QTableWidgetItem(unemployed_data['name_']))
            self.tableUnemployeds.setItem(i, 2, QtWidgets.QTableWidgetItem(unemployed_data['job']))
            self.tableUnemployeds.setItem(i, 3, QtWidgets.QTableWidgetItem(str(unemployed_data['experience'])))
            self.tableUnemployeds.setItem(i, 4, QtWidgets.QTableWidgetItem(unemployed_data['grad_level']))
            if unemployed_data['registery']:
                self.tableUnemployeds.setItem(i, 5, QtWidgets.QTableWidgetItem('Temiz'))
            else:
                self.tableUnemployeds.setItem(i, 5, QtWidgets.QTableWidgetItem('Temiz Değil'))
            self.tableUnemployeds.setItem(i, 6, QtWidgets.QTableWidgetItem(str(unemployed_data['disable_level'])))
            if unemployed_data['marriage']:
                self.tableUnemployeds.setItem(i, 7, QtWidgets.QTableWidgetItem('Evli'))
            else:
                self.tableUnemployeds.setItem(i, 7, QtWidgets.QTableWidgetItem('Bekar'))
            if unemployed_data['gender']:
                self.tableUnemployeds.setItem(i, 8, QtWidgets.QTableWidgetItem('Erkek'))
            else:
                self.tableUnemployeds.setItem(i, 8, QtWidgets.QTableWidgetItem('Kadın'))
            self.tableUnemployeds.setItem(i, 9, QtWidgets.QTableWidgetItem(str(unemployed_data['birthdate'])[0:10]))
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

        print(filterType)

        unemployeds_data = vtConnection.filterAndReadUnemployeds(filterType, filterValue)

        self.tableUnemployeds.clearContents()
        self.tableUnemployeds.setRowCount(0)
        i = 0

        for unemployed_data in unemployeds_data:
            self.tableUnemployeds.insertRow(i)
            self.tableUnemployeds.setItem(i, 0, QtWidgets.QTableWidgetItem(str(unemployed_data['ssn'])))
            self.tableUnemployeds.setItem(i, 1, QtWidgets.QTableWidgetItem(unemployed_data['name_']))
            self.tableUnemployeds.setItem(i, 2, QtWidgets.QTableWidgetItem(unemployed_data['job']))
            self.tableUnemployeds.setItem(i, 3, QtWidgets.QTableWidgetItem(str(unemployed_data['experience'])))
            self.tableUnemployeds.setItem(i, 4, QtWidgets.QTableWidgetItem(unemployed_data['grad_level']))
            if unemployed_data['registery']:
                self.tableUnemployeds.setItem(i, 5, QtWidgets.QTableWidgetItem('Temiz'))
            else:
                self.tableUnemployeds.setItem(i, 5, QtWidgets.QTableWidgetItem('Temiz Değil'))
            self.tableUnemployeds.setItem(i, 6, QtWidgets.QTableWidgetItem(str(unemployed_data['disable_level'])))
            if unemployed_data['marriage']:
                self.tableUnemployeds.setItem(i, 7, QtWidgets.QTableWidgetItem('Evli'))
            else:
                self.tableUnemployeds.setItem(i, 7, QtWidgets.QTableWidgetItem('Bekar'))
            if unemployed_data['gender']:
                self.tableUnemployeds.setItem(i, 8, QtWidgets.QTableWidgetItem('Erkek'))
            else:
                self.tableUnemployeds.setItem(i, 8, QtWidgets.QTableWidgetItem('Kadın'))
            self.tableUnemployeds.setItem(i, 9, QtWidgets.QTableWidgetItem(str(unemployed_data['birthdate'])[0:10]))
            i = i + 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormListUnemployeds = QtWidgets.QWidget()
    ui = Ui_FormListUnemployeds()
    ui.setupUi(FormListUnemployeds)
    FormListUnemployeds.show()
    sys.exit(app.exec_())

