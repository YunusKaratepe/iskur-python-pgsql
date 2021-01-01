# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import FormAddFirm, FormAddUnemployed, FormDeleteUnemployed, FormListUnemployeds, FormListEmployees, FormListFirms, \
    FormDeleteFirm, FormListAllInterviews, FormListNullInterviews, FormCreateInterview, FormCreateTodo
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

        self.labelLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelLogo.setGeometry(QtCore.QRect(195, -10, 470, 470))
        self.pixmap = QtGui.QPixmap('public/ytulogopng.png').scaled(self.labelLogo.width(), self.labelLogo.height())
        self.labelLogo.setPixmap(self.pixmap)

        self.labelLogo.show()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 430, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 470, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 520, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 550, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 580, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.listWidgetTodo = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetTodo.setGeometry(QtCore.QRect(60, 610, 661, 131))
        self.listWidgetTodo.setObjectName("listWidgetTodo")

        self.pushButtonDeleteTodo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDeleteTodo.setGeometry(QtCore.QRect(730, 710, 81, 31))
        self.pushButtonDeleteTodo.setObjectName("pushButtonDeleteTodo")

        self.pushButtonAddTodo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddTodo.setGeometry(QtCore.QRect(730, 670, 81, 31))
        self.pushButtonAddTodo.setObjectName("pushButtonAddTodo")

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
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidgetTodo.setFont(font)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Yıldız Teknik Üniversitesi"))
        self.label_2.setText(_translate("MainWindow", "İşkur Sistemi"))
        self.label_3.setText(_translate("MainWindow", "Yardım:"))
        self.label_4.setText(_translate("MainWindow", "Ekranın üst kısmında bulunan navigasyon ile işlem ekranları açılabilir."))
        self.label_5.setText(_translate("MainWindow", "Yapılacaklar Listesi:"))
        self.pushButtonAddTodo.setText(_translate("MainWindow", "Ekle"))
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
        self.pushButtonDeleteTodo.setText(_translate("MainWindow", "Seçiliyi Sil"))
        self.listTodos()
        self.pushButtonAddTodo.clicked.connect(self.openFormAddTodo)
        self.pushButtonDeleteTodo.clicked.connect(self.deleteTodo)

    def addTodo(self):
        if self.FormCreateTodo_ui.textEditTodo.toPlainText() and not self.FormCreateTodo_ui.textEditTodo.toPlainText().isspace():
            vtConnection.addTodo(self.FormCreateTodo_ui.textEditTodo.toPlainText())
            messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Todo', 'İş eklendi')
            messageBox.exec()
            self.listWidgetTodo.addItem(self.FormCreateTodo_ui.textEditTodo.toPlainText())
        else:
            messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Todo',
                                               'Yapılacak iş boş olamaz.')
            messageBox.exec()


    def openFormAddTodo(self):
        self.FormCreateTodo = QtWidgets.QWidget()
        self.FormCreateTodo_ui = FormCreateTodo.Ui_FormTodo()
        self.FormCreateTodo_ui.setupUi(self.FormCreateTodo)
        self.FormCreateTodo_ui.pushButtonCreate.clicked.connect(self.addTodo)
        self.FormCreateTodo.show()

    def listTodos(self):
        todos = vtConnection.readTodos()
        for t in todos:
            self.listWidgetTodo.addItem(t['todo'])

    def deleteTodo(self):
        if self.listWidgetTodo.selectedIndexes():
            vtConnection.deleteTodo(self.listWidgetTodo.currentItem().text())
            item = self.listWidgetTodo.takeItem(self.listWidgetTodo.currentRow());
            del item
            messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Todo',
                                               'İş başarıyla silindi')
            messageBox.exec()
        else:
            messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Todo', 'Önce listeden bir iş seçmelisiniz.')
            messageBox.exec()

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
MainWindow = QtWidgets.QMainWindow()
MainWindow_ui = Ui_MainWindow()
MainWindow_ui.setupUi(MainWindow)

MainWindow_ui.actionListUnemployeds.triggered.connect(MainWindow_ui.openFormListUnemployeds)
MainWindow_ui.actionAddNewUnemployed.triggered.connect(MainWindow_ui.openFormAddUnemployed)
MainWindow_ui.actionDeleteUnemployed.triggered.connect(MainWindow_ui.openFormDeleteUnemployed)
MainWindow_ui.actionListEmployees.triggered.connect(MainWindow_ui.openFormListEmployees)

MainWindow_ui.actionListAllInterviews.triggered.connect(MainWindow_ui.openFormListAllInterviews)
MainWindow_ui.actionListFutureInterviews.triggered.connect(MainWindow_ui.openFormListNullInterviews)
MainWindow_ui.actionCreateInterview.triggered.connect(MainWindow_ui.openFormCreateInterview)

MainWindow_ui.actionListFirms.triggered.connect(MainWindow_ui.openFormListFirms)
MainWindow_ui.actionAddFirm.triggered.connect(MainWindow_ui.openFormAddFirm)
MainWindow_ui.actionRemoveFirm.triggered.connect(MainWindow_ui.openFormDeletefirm)

MainWindow.show()
sys.exit(app.exec_())


