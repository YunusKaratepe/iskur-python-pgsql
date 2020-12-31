# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_list_null_interviews.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vt_connection import vtConnection
import UnemployedInfos

class Ui_FormListNullInterviews(object):
    def setupUi(self, FormListNullInterviews):
        FormListNullInterviews.setObjectName("FormListNullInterviews")
        FormListNullInterviews.resize(857, 526)
        self.tableWidgetListInterviews = QtWidgets.QTableWidget(FormListNullInterviews)
        self.tableWidgetListInterviews.setGeometry(QtCore.QRect(0, 80, 850, 400))
        self.tableWidgetListInterviews.setObjectName("tableWidgetListInterviews")
        self.tableWidgetListInterviews.setColumnCount(5)
        self.tableWidgetListInterviews.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListInterviews.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListInterviews.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListInterviews.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListInterviews.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListInterviews.setHorizontalHeaderItem(4, item)
        self.tableWidgetListInterviews.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetListInterviews.horizontalHeader().setDefaultSectionSize(160)
        self.label = QtWidgets.QLabel(FormListNullInterviews)
        self.label.setGeometry(QtCore.QRect(320, 10, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditSearchInterview = QtWidgets.QLineEdit(FormListNullInterviews)
        self.lineEditSearchInterview.setGeometry(QtCore.QRect(140, 50, 201, 23))
        self.lineEditSearchInterview.setObjectName("lineEditSearchInterview")
        self.comboBoxSearchInterview = QtWidgets.QComboBox(FormListNullInterviews)
        self.comboBoxSearchInterview.setGeometry(QtCore.QRect(10, 50, 121, 23))
        self.comboBoxSearchInterview.setObjectName("comboBoxSearchInterview")
        self.comboBoxSearchInterview.addItem("")
        self.comboBoxSearchInterview.addItem("")
        self.comboBoxSearchInterview.addItem("")
        self.pushButtonSearchInterview = QtWidgets.QPushButton(FormListNullInterviews)
        self.pushButtonSearchInterview.setGeometry(QtCore.QRect(350, 50, 80, 23))
        self.pushButtonSearchInterview.setObjectName("pushButtonSearchInterview")
        self.pushButtonRefreshList = QtWidgets.QPushButton(FormListNullInterviews)
        self.pushButtonRefreshList.setGeometry(QtCore.QRect(760, 50, 80, 23))
        self.pushButtonRefreshList.setObjectName("pushButtonRefreshList")
        self.pushButtonRefreshList_2 = QtWidgets.QPushButton(FormListNullInterviews)
        self.pushButtonRefreshList_2.setGeometry(QtCore.QRect(190, 490, 191, 31))
        self.pushButtonRefreshList_2.setObjectName("pushButtonRefreshList_2")
        self.label_2 = QtWidgets.QLabel(FormListNullInterviews)
        self.label_2.setGeometry(QtCore.QRect(10, 490, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(FormListNullInterviews)
        QtCore.QMetaObject.connectSlotsByName(FormListNullInterviews)

    def retranslateUi(self, FormListNullInterviews):
        _translate = QtCore.QCoreApplication.translate
        FormListNullInterviews.setWindowTitle(_translate("FormListNullInterviews", "Form"))
        item = self.tableWidgetListInterviews.horizontalHeaderItem(0)
        item.setText(_translate("FormListNullInterviews", "Mülakat ID"))
        item = self.tableWidgetListInterviews.horizontalHeaderItem(1)
        item.setText(_translate("FormListNullInterviews", "İşçi ID"))
        item = self.tableWidgetListInterviews.horizontalHeaderItem(2)
        item.setText(_translate("FormListNullInterviews", "İşçi Adı"))
        item = self.tableWidgetListInterviews.horizontalHeaderItem(3)
        item.setText(_translate("FormListNullInterviews", "Şirket ID"))
        item = self.tableWidgetListInterviews.horizontalHeaderItem(4)
        item.setText(_translate("FormListNullInterviews", "Şirket Adı"))
        self.label.setText(_translate("FormListNullInterviews", "Sonuçsuz Mülakatlar"))
        self.comboBoxSearchInterview.setItemText(0, _translate("FormListNullInterviews", "Mülakat ID"))
        self.comboBoxSearchInterview.setItemText(1, _translate("FormListNullInterviews", "İşçi Adı"))
        self.comboBoxSearchInterview.setItemText(2, _translate("FormListNullInterviews", "Şirket Adı"))
        self.pushButtonSearchInterview.setText(_translate("FormListNullInterviews", "Ara"))
        self.pushButtonRefreshList.setText(_translate("FormListNullInterviews", "Yenile"))
        self.pushButtonRefreshList_2.setText(_translate("FormListNullInterviews", "Bilgileri Görüntüle"))
        self.label_2.setText(_translate("FormListNullInterviews", "Onaylamak İçin ->"))
        self.tableWidgetListInterviews.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetListInterviews.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.pushButtonRefreshList.clicked.connect(self.refreshList)
        self.pushButtonRefreshList_2.clicked.connect(self.openUnemployedInfos)


        self.refreshList()
        self.pushButtonSearchInterview.clicked.connect(self.filterList)

    def openUnemployedInfos(self):
        if self.tableWidgetListInterviews.selectedIndexes():
            print(self.tableWidgetListInterviews.selectedIndexes()[1].data())
            selected_unemployed = vtConnection.unemployedInfoShow(self.tableWidgetListInterviews.selectedIndexes()[1].data())

            self.UnemployedInfos = QtWidgets.QWidget()
            self.UnemployedInfos_ui = UnemployedInfos.Ui_UnemployedInfos()
            self.UnemployedInfos_ui.setupUi(self.UnemployedInfos)
            self.UnemployedInfos_ui.lineEditPersonTcNo.setText(selected_unemployed['ssn'])
            self.UnemployedInfos_ui.lineEditPersonName.setText(selected_unemployed['name_'])
            self.UnemployedInfos_ui.lineEditPersonJob.setText(selected_unemployed['job'])
            self.UnemployedInfos_ui.spinBoxExperience.setValue(int(selected_unemployed['experience']))
            self.UnemployedInfos_ui.comboBoxEducation.setCurrentText(selected_unemployed['grad_level'])
            if selected_unemployed['registery'] == 'Temiz':
                self.UnemployedInfos_ui.radioButtonRegisteryClean.setChecked(True)
            else:
                self.UnemployedInfos_ui.radioButtonRegisteryNotClean.setChecked(True)
            if selected_unemployed['disable_level']:
                self.UnemployedInfos_ui.radioButtonDisabled.setChecked(True)
            else:
                self.UnemployedInfos_ui.radioButtonNotDisabled.setChecked(True)
            if selected_unemployed['marriage']:
                self.UnemployedInfos_ui.radioButtonMarried.setChecked(True)
            else:
                self.UnemployedInfos_ui.radioButtonSingle.setChecked(True)
            if selected_unemployed['gender']:
                self.UnemployedInfos_ui.radioButtonGenderMale.setChecked(True)
            else:
                self.UnemployedInfos_ui.radioButtonGenderFemale.setChecked(True)
            self.UnemployedInfos_ui.dateEditBirthday.setDate(QtCore.QDate(selected_unemployed['birthdate']))
            self.UnemployedInfos_ui.lineEditPersonTcNo.setReadOnly(True)
            self.UnemployedInfos_ui.lineEditPersonName.setReadOnly(True)
            self.UnemployedInfos_ui.lineEditPersonJob.setReadOnly(True)
            self.UnemployedInfos_ui.spinBoxExperience.setReadOnly(True)
            self.UnemployedInfos_ui.comboBoxEducation.setDisabled(True)
            self.UnemployedInfos_ui.radioButtonNotDisabled.setDisabled(True)
            self.UnemployedInfos_ui.radioButtonDisabled.setDisabled(True)
            self.UnemployedInfos_ui.radioButtonGenderFemale.setDisabled(True)
            self.UnemployedInfos_ui.radioButtonGenderMale.setDisabled(True)
            self.UnemployedInfos_ui.radioButtonRegisteryClean.setDisabled(True)
            self.UnemployedInfos_ui.radioButtonRegisteryNotClean.setDisabled(True)
            self.UnemployedInfos_ui.radioButtonSingle.setDisabled(True)
            self.UnemployedInfos_ui.radioButtonMarried.setDisabled(True)
            self.UnemployedInfos_ui.label.setText('İşçi Bilgileri')
            self.UnemployedInfos_ui.dateEditBirthday.setReadOnly(True)
            self.UnemployedInfos_ui.unemloyed_ssn = selected_unemployed['ssn']
            self.UnemployedInfos_ui.firm_id = int(self.tableWidgetListInterviews.selectedIndexes()[3].data())
            self.UnemployedInfos.show()
            self.UnemployedInfos_ui.pushButtonHireUnemployed.clicked.connect(self.hireUnemployed)
            self.UnemployedInfos_ui.pushButtonDenyUnemployed.clicked.connect(self.denyUnemployed)
        else:
            messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Bilgiler',
                                               'Bilgileri görmek için bir satır seçmelisiniz.')
            messageBox.exec_()

    def hireUnemployed(self):
        if self.UnemployedInfos_ui.lineEditSalary.text().isnumeric():
            messageBox = QtWidgets.QMessageBox.question(None, 'İşe Al', 'İşe almak istediğinize emin misiniz?',
                                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
            if messageBox == QtWidgets.QMessageBox.Yes:
                vtConnection.hireOrDenyUnemployed(self.UnemployedInfos_ui.unemloyed_ssn, self.UnemployedInfos_ui.firm_id, True,
                                                  int(self.UnemployedInfos_ui.lineEditSalary.text()))
                messageBox2 = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'İşe Al',
                                                   'Başarıyla işe alındı')
                messageBox2.exec_()
                self.tableWidgetListInterviews.removeRow(self.tableWidgetListInterviews.currentRow())
        else:
            messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'İşe Al', 'İşe alım yapabilmek için maaş bölümünü doldurmalısınız.')
            messageBox.exec_()

    def denyUnemployed(self):
        messageBox = QtWidgets.QMessageBox.question(None, 'Reddet', 'Reddetmek istediğinize emin misiniz?',
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        if messageBox == QtWidgets.QMessageBox.Yes:
            vtConnection.hireOrDenyUnemployed(self.UnemployedInfos_ui.unemloyed_ssn, self.UnemployedInfos_ui.firm_id, False)

    def refreshList(self):
        self.tableWidgetListInterviews.clearContents()
        self.tableWidgetListInterviews.setRowCount(0)
        interviews = vtConnection.readNullInterviews()
        i = 0
        for interview in interviews:
            self.tableWidgetListInterviews.insertRow(i)
            self.tableWidgetListInterviews.setItem(i, 0, QtWidgets.QTableWidgetItem(str(interview['id'])))
            self.tableWidgetListInterviews.setItem(i, 1, QtWidgets.QTableWidgetItem(str(interview['worker_ssn'])))
            self.tableWidgetListInterviews.setItem(i, 2, QtWidgets.QTableWidgetItem(str(interview['worker_name'])))
            self.tableWidgetListInterviews.setItem(i, 3, QtWidgets.QTableWidgetItem(str(interview['firm_id'])))
            self.tableWidgetListInterviews.setItem(i, 4, QtWidgets.QTableWidgetItem(str(interview['firm_name'])))
            i += 1

    def filterList(self):
        if self.comboBoxSearchInterview.currentText() == 'Mülakat ID':
            if not self.lineEditSearchInterview.text().isnumeric():
                return print('Id int olmalıdır.')
            interviews = vtConnection.filterAndReadNullInterviews('id', self.lineEditSearchInterview.text())
        elif self.comboBoxSearchInterview.currentText() == 'İşçi Adı':
            interviews = vtConnection.filterAndReadNullInterviews('worker_name', self.lineEditSearchInterview.text())
        else:
            interviews = vtConnection.filterAndReadNullInterviews('firm_name', self.lineEditSearchInterview.text())

        self.tableWidgetListInterviews.clearContents()
        self.tableWidgetListInterviews.setRowCount(0)
        i = 0
        for interview in interviews:
            self.tableWidgetListInterviews.insertRow(i)
            self.tableWidgetListInterviews.setItem(i, 0, QtWidgets.QTableWidgetItem(str(interview['id'])))
            self.tableWidgetListInterviews.setItem(i, 1, QtWidgets.QTableWidgetItem(str(interview['worker_ssn'])))
            self.tableWidgetListInterviews.setItem(i, 2, QtWidgets.QTableWidgetItem(str(interview['worker_name'])))
            self.tableWidgetListInterviews.setItem(i, 3, QtWidgets.QTableWidgetItem(str(interview['firm_id'])))
            self.tableWidgetListInterviews.setItem(i, 4, QtWidgets.QTableWidgetItem(str(interview['firm_name'])))
            i += 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormListNullInterviews = QtWidgets.QWidget()
    ui = Ui_FormListNullInterviews()
    ui.setupUi(FormListNullInterviews)
    FormListNullInterviews.show()
    sys.exit(app.exec_())

