# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import FormAddFirm, FormAddUnemployed, FormDeleteUnemployed, FormListUnemployeds, FormListEmployees, FormListFirms, \
    FormDeleteFirm, FormListAllInterviews, FormListNullInterviews, FormCreateInterview
from vt_connection import vtConnection


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(850, 800))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableFirms = QtWidgets.QTableWidget(self.centralwidget)
        self.tableFirms.setGeometry(QtCore.QRect(0, 62, 850, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableFirms.sizePolicy().hasHeightForWidth())
        self.tableFirms.setSizePolicy(sizePolicy)
        self.tableFirms.setObjectName("tableFirms")
        self.tableFirms.setColumnCount(5)
        self.tableFirms.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableFirms.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFirms.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFirms.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFirms.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFirms.setHorizontalHeaderItem(4, item)
        self.tableFirms.horizontalHeader().setDefaultSectionSize(168)
        self.labelApplications = QtWidgets.QLabel(self.centralwidget)
        self.labelApplications.setGeometry(QtCore.QRect(340, 0, 191, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelApplications.setFont(font)
        self.labelApplications.setAlignment(QtCore.Qt.AlignCenter)
        self.labelApplications.setObjectName("labelApplications")
        self.tableEmployees = QtWidgets.QTableWidget(self.centralwidget)
        self.tableEmployees.setGeometry(QtCore.QRect(0, 392, 850, 361))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableEmployees.sizePolicy().hasHeightForWidth())
        self.tableEmployees.setSizePolicy(sizePolicy)
        self.tableEmployees.setObjectName("tableEmployees")
        self.tableEmployees.setColumnCount(8)
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
        self.tableEmployees.horizontalHeader().setDefaultSectionSize(105)
        self.labelEmployees = QtWidgets.QLabel(self.centralwidget)
        self.labelEmployees.setGeometry(QtCore.QRect(0, 362, 851, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelEmployees.setFont(font)
        self.labelEmployees.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEmployees.setObjectName("labelEmployees")
        self.pushButtonListWorkersOfFirm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonListWorkersOfFirm.setGeometry(QtCore.QRect(580, 30, 261, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonListWorkersOfFirm.sizePolicy().hasHeightForWidth())
        self.pushButtonListWorkersOfFirm.setSizePolicy(sizePolicy)
        self.pushButtonListWorkersOfFirm.setObjectName("pushButtonListWorkersOfFirm")
        self.pushButtonSearchFirm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearchFirm.setGeometry(QtCore.QRect(240, 30, 71, 23))
        self.pushButtonSearchFirm.setObjectName("pushButtonSearchFirm")
        self.comboBoxSearchFirm = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxSearchFirm.setGeometry(QtCore.QRect(10, 30, 81, 23))
        self.comboBoxSearchFirm.setObjectName("comboBoxSearchFirm")
        self.comboBoxSearchFirm.addItem("")
        self.comboBoxSearchFirm.addItem("")
        self.lineEditSearchFirm = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSearchFirm.setGeometry(QtCore.QRect(100, 30, 131, 23))
        self.lineEditSearchFirm.setObjectName("lineEditSearchFirm")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 20))
        self.menubar.setObjectName("menubar")
        self.menuFirmActions = QtWidgets.QMenu(self.menubar)
        self.menuFirmActions.setObjectName("menuFirmActions")
        self.menuEmployeeActions = QtWidgets.QMenu(self.menubar)
        self.menuEmployeeActions.setObjectName("menuEmployeeActions")
        self.menuApplicationActions = QtWidgets.QMenu(self.menubar)
        self.menuApplicationActions.setObjectName("menuApplicationActions")
        self.menuInterviewActions = QtWidgets.QMenu(self.menubar)
        self.menuInterviewActions.setObjectName("menuInterviewActions")
        MainWindow.setMenuBar(self.menubar)
        self.actionListFirms = QtWidgets.QAction(MainWindow)
        self.actionListFirms.setObjectName("actionListFirms")
        self.actionSearchFirmById = QtWidgets.QAction(MainWindow)
        self.actionSearchFirmById.setObjectName("actionSearchFirmById")
        self.actionListUnemployeds = QtWidgets.QAction(MainWindow)
        self.actionListUnemployeds.setObjectName("actionListUnemployeds")
        self.actionAddFirm = QtWidgets.QAction(MainWindow)
        self.actionAddFirm.setObjectName("actionAddFirm")
        self.actionRemoveFirm = QtWidgets.QAction(MainWindow)
        self.actionRemoveFirm.setObjectName("actionRemoveFirm")
        self.actionListEmployees = QtWidgets.QAction(MainWindow)
        self.actionListEmployees.setObjectName("actionListEmployees")
        self.actionListAllInterviews = QtWidgets.QAction(MainWindow)
        self.actionListAllInterviews.setObjectName("actionListAllInterviews")
        self.actionListFutureInterviews = QtWidgets.QAction(MainWindow)
        self.actionListFutureInterviews.setObjectName("actionListFutureInterviews")
        self.actionAddNewUnemployed = QtWidgets.QAction(MainWindow)
        self.actionAddNewUnemployed.setObjectName("actionAddNewUnemployed")
        self.actionDeleteUnemployed = QtWidgets.QAction(MainWindow)
        self.actionDeleteUnemployed.setObjectName("actionDeleteUnemployed")
        self.actionCreateInterview = QtWidgets.QAction(MainWindow)
        self.actionCreateInterview.setObjectName("actionCreateInterview")
        self.menuFirmActions.addAction(self.actionListFirms)
        self.menuFirmActions.addAction(self.actionAddFirm)
        self.menuFirmActions.addAction(self.actionRemoveFirm)
        self.menuEmployeeActions.addAction(self.actionListEmployees)
        self.menuApplicationActions.addAction(self.actionListUnemployeds)
        self.menuApplicationActions.addAction(self.actionAddNewUnemployed)
        self.menuApplicationActions.addAction(self.actionDeleteUnemployed)
        self.menuInterviewActions.addAction(self.actionListAllInterviews)
        self.menuInterviewActions.addAction(self.actionListFutureInterviews)
        self.menuInterviewActions.addAction(self.actionCreateInterview)
        self.menubar.addAction(self.menuFirmActions.menuAction())
        self.menubar.addAction(self.menuEmployeeActions.menuAction())
        self.menubar.addAction(self.menuApplicationActions.menuAction())
        self.menubar.addAction(self.menuInterviewActions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableFirms.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableFirms.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "İsim"))
        item = self.tableFirms.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Adres"))
        item = self.tableFirms.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telefon"))
        item = self.tableFirms.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Eğitim Gereksinimi"))
        self.labelApplications.setText(_translate("MainWindow", "Şirketler"))
        item = self.tableEmployees.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TC No"))
        item = self.tableEmployees.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "İsim"))
        item = self.tableEmployees.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Meslek"))
        item = self.tableEmployees.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tecrübe"))
        item = self.tableEmployees.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Eğitim"))
        item = self.tableEmployees.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sicil"))
        item = self.tableEmployees.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Engel"))
        item = self.tableEmployees.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Medeni Hal"))
        self.labelEmployees.setText(_translate("MainWindow", "İş Bulunmuş Çalışanlar"))
        self.pushButtonListWorkersOfFirm.setText(_translate("MainWindow", "Şirkete Kazandırılan Çalışanları Listele"))
        self.pushButtonSearchFirm.setText(_translate("MainWindow", "Ara"))
        self.comboBoxSearchFirm.setItemText(0, _translate("MainWindow", "ID"))
        self.comboBoxSearchFirm.setItemText(1, _translate("MainWindow", "İsim"))
        self.menuFirmActions.setTitle(_translate("MainWindow", "Şirket İşlemleri"))
        self.menuEmployeeActions.setTitle(_translate("MainWindow", "İşçi İşlemleri"))
        self.menuApplicationActions.setTitle(_translate("MainWindow", "Başvuru İşlemleri"))
        self.menuInterviewActions.setTitle(_translate("MainWindow", "Mülakat İşlemleri"))
        self.actionListFirms.setText(_translate("MainWindow", "Şirketleri Listele"))
        self.actionSearchFirmById.setText(_translate("MainWindow", "Id\'ye Göre Şirket Ara"))
        self.actionListUnemployeds.setText(_translate("MainWindow", "Başvuruları Listele"))
        self.actionAddFirm.setText(_translate("MainWindow", "Şirket Ekle"))
        self.actionRemoveFirm.setText(_translate("MainWindow", "Şirket Sil"))
        self.actionListEmployees.setText(_translate("MainWindow", "İş Sahiplerini Listele"))
        self.actionListAllInterviews.setText(_translate("MainWindow", "Tüm Mülakatları Listele"))
        self.actionListFutureInterviews.setText(_translate("MainWindow", "Bekleyen Mülakatlar"))
        self.actionCreateInterview.setText(_translate("MainWindow", "Yeni Mülakat Oluştur"))
        self.actionAddNewUnemployed.setText(_translate("MainWindow", "Başvuru Ekle"))
        self.actionDeleteUnemployed.setText(_translate("MainWindow", "Başvuru Sil"))
        self.listAllFirms()
        self.pushButtonSearchFirm.clicked.connect(self.listFilteredFirms)
        self.tableFirms.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableEmployees.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def listAllFirms(self):
        firms_data = vtConnection.readFirms()
        if not firms_data:
            return print('No data')
        self.tableFirms.clearContents()
        self.tableFirms.setRowCount(0)
        i = 0
        for firm_data in firms_data:
            self.tableFirms.insertRow(i)
            self.tableFirms.setItem(i, 0, QtWidgets.QTableWidgetItem(str(firm_data['id'])))
            self.tableFirms.setItem(i, 1, QtWidgets.QTableWidgetItem(firm_data['name_']))
            self.tableFirms.setItem(i, 2, QtWidgets.QTableWidgetItem(firm_data['address']))
            self.tableFirms.setItem(i, 3, QtWidgets.QTableWidgetItem(firm_data['phone']))
            self.tableFirms.setItem(i, 4, QtWidgets.QTableWidgetItem(firm_data['req_grad_level']))
            i = i + 1

    def listFilteredFirms(self):
        filterValue = self.lineEditSearchFirm.text()
        if self.comboBoxSearchFirm.currentText() == 'ID':
            filterType = 'id'
        else:
            filterType = 'name'

        firms_data = vtConnection.filterAndReadFirms(filterType, filterValue)

        self.tableFirms.clearContents()
        self.tableFirms.setRowCount(0)

        if not firms_data:
            return

        i = 0
        for firm_data in firms_data:
            self.tableFirms.insertRow(i)
            self.tableFirms.setItem(i, 1, QtWidgets.QTableWidgetItem(str(firm_data['id'])))
            self.tableFirms.setItem(i, 2, QtWidgets.QTableWidgetItem(firm_data['name_']))
            self.tableFirms.setItem(i, 3, QtWidgets.QTableWidgetItem(firm_data['address']))
            self.tableFirms.setItem(i, 4, QtWidgets.QTableWidgetItem(firm_data['phone']))
            self.tableFirms.setItem(i, 5, QtWidgets.QTableWidgetItem(firm_data['req_grad_level']))
            i += 1

    def openFormListUnemployeds(self):
        self.FormListUnemployeds = QtWidgets.QWidget()
        self.FormListUnemployeds_ui = FormListUnemployeds.Ui_FormListUnemployeds()
        self.FormListUnemployeds_ui.setupUi(self.FormListUnemployeds)
        self.FormListUnemployeds.show()

    def openFormAddFirm(self):
        self.FormAddFirm = QtWidgets.QWidget()
        self.FormAddFirm_ui = FormAddFirm.Ui_FormAddFirm()
        self.FormAddFirm_ui.setupUi(self.FormAddFirm)
        self.FormAddFirm.show()

    def openFormListFirms(self):
        self.FormListFirms = QtWidgets.QWidget()
        self.FormListFirms_ui = FormListFirms.Ui_FormListFirms()
        self.FormListFirms_ui.setupUi(self.FormListFirms)
        self.FormListFirms.show()

    def openFormDeletefirm(self):
        self.FormDeleteFirm = QtWidgets.QWidget()
        self.FormDeleteFirm_ui = FormDeleteFirm.Ui_FormDeleteFirm()
        self.FormDeleteFirm_ui.setupUi(self.FormDeleteFirm)
        self.FormDeleteFirm.show()

    def openFormListEmployees(self):
        self.FormListEmployees = QtWidgets.QWidget()
        self.FormListEmployees_ui = FormListEmployees.Ui_FormListEmployees()
        self.FormListEmployees_ui.setupUi(self.FormListEmployees)
        self.FormListEmployees.show()

    def openFormAddUnemployed(self):
        self.FormAddUnemployed = QtWidgets.QWidget()
        self.FormAddUnemployed_ui = FormAddUnemployed.Ui_FormAddUnemployed()
        self.FormAddUnemployed_ui.setupUi(self.FormAddUnemployed)
        self.FormAddUnemployed.show()

    def openFormDeleteUnemployed(self):
        self.FormDeleteUnemployed = QtWidgets.QWidget()
        self.FormDeleteUnemployed_ui = FormDeleteUnemployed.Ui_FormDeleteUnemployed()
        self.FormDeleteUnemployed_ui.setupUi(self.FormDeleteUnemployed)
        self.FormDeleteUnemployed.show()

    def openFormListAllInterviews(self):
        self.FormListAllInterviews = QtWidgets.QWidget()
        self.FormListAllInterviews_ui = FormListAllInterviews.Ui_FormListAllInterviews()
        self.FormListAllInterviews_ui.setupUi(self.FormListAllInterviews)
        self.FormListAllInterviews.show()

    def openFormListNullInterviews(self):
        self.FormListFutureInterviews = QtWidgets.QWidget()
        self.FormListFutureInterviews_ui = FormListNullInterviews.Ui_FormListNullInterviews()
        self.FormListFutureInterviews_ui.setupUi(self.FormListFutureInterviews)
        self.FormListFutureInterviews.show()

    def openFormCreateInterview(self):
        self.FormCreateInterview = QtWidgets.QWidget()
        self.FormCreateInterview_ui = FormCreateInterview.Ui_FormAddNewInterview()
        self.FormCreateInterview_ui.setupUi(self.FormCreateInterview)
        self.FormCreateInterview.show()




# app starts here
app = QtWidgets.QApplication(sys.argv)
mainWindow = QtWidgets.QMainWindow()
mainWindow_ui = Ui_MainWindow()
mainWindow_ui.setupUi(mainWindow)


mainWindow_ui.actionListUnemployeds.triggered.connect(mainWindow_ui.openFormListUnemployeds)
mainWindow_ui.actionAddNewUnemployed.triggered.connect(mainWindow_ui.openFormAddUnemployed)
mainWindow_ui.actionDeleteUnemployed.triggered.connect(mainWindow_ui.openFormDeleteUnemployed)
mainWindow_ui.actionListEmployees.triggered.connect(mainWindow_ui.openFormListEmployees)



mainWindow_ui.actionListAllInterviews.triggered.connect(mainWindow_ui.openFormListAllInterviews)
mainWindow_ui.actionListFutureInterviews.triggered.connect(mainWindow_ui.openFormListNullInterviews)
mainWindow_ui.actionCreateInterview.triggered.connect(mainWindow_ui.openFormCreateInterview)


mainWindow_ui.actionListFirms.triggered.connect(mainWindow_ui.openFormListFirms)
mainWindow_ui.actionAddFirm.triggered.connect(mainWindow_ui.openFormAddFirm)
mainWindow_ui.actionRemoveFirm.triggered.connect(mainWindow_ui.openFormDeletefirm)











mainWindow.show()
sys.exit(app.exec_())
