# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_list_all_interviews.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vt_connection import vtConnection


class Ui_FormListAllInterviews(object):
    def setupUi(self, FormListAllInterviews):
        FormListAllInterviews.setObjectName("FormListAllInterviews")
        FormListAllInterviews.resize(857, 488)
        self.tableWidgetListInterviews = QtWidgets.QTableWidget(FormListAllInterviews)
        self.tableWidgetListInterviews.setGeometry(QtCore.QRect(0, 80, 850, 400))
        self.tableWidgetListInterviews.setObjectName("tableWidgetListInterviews")
        self.tableWidgetListInterviews.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetListInterviews.setHorizontalHeaderItem(5, item)
        self.tableWidgetListInterviews.horizontalHeader().setDefaultSectionSize(135)
        self.label = QtWidgets.QLabel(FormListAllInterviews)
        self.label.setGeometry(QtCore.QRect(360, 10, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditSearchInterview = QtWidgets.QLineEdit(FormListAllInterviews)
        self.lineEditSearchInterview.setGeometry(QtCore.QRect(140, 50, 201, 23))
        self.lineEditSearchInterview.setObjectName("lineEditSearchInterview")
        self.comboBoxSearchInterview = QtWidgets.QComboBox(FormListAllInterviews)
        self.comboBoxSearchInterview.setGeometry(QtCore.QRect(10, 50, 121, 23))
        self.comboBoxSearchInterview.setObjectName("comboBoxSearchInterview")
        self.comboBoxSearchInterview.addItem("")
        self.comboBoxSearchInterview.addItem("")
        self.comboBoxSearchInterview.addItem("")
        self.pushButtonSearchInterview = QtWidgets.QPushButton(FormListAllInterviews)
        self.pushButtonSearchInterview.setGeometry(QtCore.QRect(350, 50, 80, 23))
        self.pushButtonSearchInterview.setObjectName("pushButtonSearchInterview")
        self.pushButtonRefreshList = QtWidgets.QPushButton(FormListAllInterviews)
        self.pushButtonRefreshList.setGeometry(QtCore.QRect(729, 50, 111, 23))
        self.pushButtonRefreshList.setObjectName("pushButtonRefreshList")

        self.retranslateUi(FormListAllInterviews)
        QtCore.QMetaObject.connectSlotsByName(FormListAllInterviews)

    def retranslateUi(self, FormListAllInterviews):
        _translate = QtCore.QCoreApplication.translate
        FormListAllInterviews.setWindowTitle(_translate("FormListAllInterviews", "Form"))
        item = self.tableWidgetListInterviews.horizontalHeaderItem(0)
        item.setText(_translate("FormListAllInterviews", "Mülakat ID"))
        item = self.tableWidgetListInterviews.horizontalHeaderItem(1)
        item.setText(_translate("FormListAllInterviews", "İşçi ID"))
        item = self.tableWidgetListInterviews.horizontalHeaderItem(2)
        item.setText(_translate("FormListAllInterviews", "İşçi Adı"))
        item = self.tableWidgetListInterviews.horizontalHeaderItem(3)
        item.setText(_translate("FormListAllInterviews", "Şirket ID"))
        item = self.tableWidgetListInterviews.horizontalHeaderItem(4)
        item.setText(_translate("FormListAllInterviews", "Şirket Adı"))
        item = self.tableWidgetListInterviews.horizontalHeaderItem(5)
        item.setText(_translate("FormListAllInterviews", "Mülakat Sonucu"))
        self.label.setText(_translate("FormListAllInterviews", "Mülakatlar"))
        self.comboBoxSearchInterview.setItemText(0, _translate("FormListAllInterviews", "Mülakat ID"))
        self.comboBoxSearchInterview.setItemText(1, _translate("FormListAllInterviews", "İşçi Adı"))
        self.comboBoxSearchInterview.setItemText(2, _translate("FormListAllInterviews", "Şirket Adı"))
        self.pushButtonSearchInterview.setText(_translate("FormListAllInterviews", "Ara"))
        self.pushButtonRefreshList.setText(_translate("FormListAllInterviews", "Yenile"))
        self.tableWidgetListInterviews.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetListInterviews.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.refreshList()
        self.pushButtonRefreshList.clicked.connect(self.refreshList)
        self.pushButtonSearchInterview.clicked.connect(self.filterList)

    def refreshList(self):
        self.tableWidgetListInterviews.clearContents()
        self.tableWidgetListInterviews.setRowCount(0)
        interviews = vtConnection.readAllInterviews()
        i = 0
        for interview in interviews:
            self.tableWidgetListInterviews.insertRow(i)
            self.tableWidgetListInterviews.setItem(i, 0, QtWidgets.QTableWidgetItem(str(interview['id'])))
            self.tableWidgetListInterviews.setItem(i, 1, QtWidgets.QTableWidgetItem(str(interview['worker_ssn'])))
            self.tableWidgetListInterviews.setItem(i, 2, QtWidgets.QTableWidgetItem(str(interview['worker_name'])))
            self.tableWidgetListInterviews.setItem(i, 3, QtWidgets.QTableWidgetItem(str(interview['firm_id'])))
            self.tableWidgetListInterviews.setItem(i, 4, QtWidgets.QTableWidgetItem(str(interview['firm_name'])))
            self.tableWidgetListInterviews.setItem(i, 5, QtWidgets.QTableWidgetItem(str(interview['outcome'])))

            i += 1

    def filterList(self):

        if self.comboBoxSearchInterview.currentText() == 'Mülakat ID':
            if not self.lineEditSearchInterview.text().isnumeric():
                return print('Id int olmalıdır.')
            interviews = vtConnection.filterAndReadAllInterviews('id', self.lineEditSearchInterview.text())
        elif self.comboBoxSearchInterview.currentText() == 'İşçi Adı':
            interviews = vtConnection.filterAndReadAllInterviews('worker_name', self.lineEditSearchInterview.text())
        else:
            interviews = vtConnection.filterAndReadAllInterviews('firm_name', self.lineEditSearchInterview.text())
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
            self.tableWidgetListInterviews.setItem(i, 5, QtWidgets.QTableWidgetItem(str(interview['outcome'])))
            i += 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormListAllInterviews = QtWidgets.QWidget()
    ui = Ui_FormListAllInterviews()
    ui.setupUi(FormListAllInterviews)
    FormListAllInterviews.show()
    sys.exit(app.exec_())

