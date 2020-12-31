# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_add_firm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vt_connection import vtConnection


class Ui_FormAddFirm(object):
    def setupUi(self, FormAddFirm):
        FormAddFirm.setObjectName("FormAddFirm")
        FormAddFirm.resize(418, 541)
        font = QtGui.QFont()
        font.setPointSize(12)
        FormAddFirm.setFont(font)
        self.label = QtWidgets.QLabel(FormAddFirm)
        self.label.setGeometry(QtCore.QRect(150, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(FormAddFirm)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 120, 24))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FormAddFirm)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 120, 24))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(FormAddFirm)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 120, 24))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(FormAddFirm)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 161, 24))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(FormAddFirm)
        self.label_7.setGeometry(QtCore.QRect(20, 310, 101, 24))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(FormAddFirm)
        self.label_8.setGeometry(QtCore.QRect(20, 370, 120, 24))
        self.label_8.setObjectName("label_8")
        self.lineEditFirmName = QtWidgets.QLineEdit(FormAddFirm)
        self.lineEditFirmName.setGeometry(QtCore.QRect(150, 110, 251, 23))
        self.lineEditFirmName.setObjectName("lineEditFirmName")
        self.lineEditFirmAddress = QtWidgets.QLineEdit(FormAddFirm)
        self.lineEditFirmAddress.setGeometry(QtCore.QRect(150, 160, 251, 23))
        self.lineEditFirmAddress.setObjectName("lineEditFirmAddress")
        self.lineEditFirmPhone = QtWidgets.QLineEdit(FormAddFirm)
        self.lineEditFirmPhone.setGeometry(QtCore.QRect(150, 210, 251, 23))
        self.lineEditFirmPhone.setObjectName("lineEditFirmPhone")
        self.comboBoxEducation = QtWidgets.QComboBox(FormAddFirm)
        self.comboBoxEducation.setGeometry(QtCore.QRect(190, 260, 211, 23))
        self.comboBoxEducation.setObjectName("comboBoxEducation")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")

        self.radioButtonDisablePermission = QtWidgets.QRadioButton(FormAddFirm)
        self.radioButtonDisablePermission.setGeometry(QtCore.QRect(150, 315, 100, 21))
        self.radioButtonDisablePermission.setObjectName("radioButtonDisablePermission")
        self.radioButtonDisableNoPermission = QtWidgets.QRadioButton(FormAddFirm)
        self.radioButtonDisableNoPermission.setGeometry(QtCore.QRect(280, 315, 131, 21))
        self.radioButtonDisableNoPermission.setObjectName("radioButtonDisableNoPermission")

        self.radioButtonRegisteryStrict = QtWidgets.QRadioButton(FormAddFirm)
        self.radioButtonRegisteryStrict.setGeometry(QtCore.QRect(150, 370, 100, 21))
        self.radioButtonRegisteryStrict.setObjectName("radioButtonRegisteryStrict")
        self.radioButtonRegisteryRelax = QtWidgets.QRadioButton(FormAddFirm)
        self.radioButtonRegisteryRelax.setGeometry(QtCore.QRect(280, 370, 100, 21))
        self.radioButtonRegisteryRelax.setObjectName("radioButtonRegisteryRelax")
        self.pushButtonAddFirm = QtWidgets.QPushButton(FormAddFirm)
        self.pushButtonAddFirm.setGeometry(QtCore.QRect(110, 450, 181, 31))
        self.pushButtonAddFirm.setObjectName("pushButtonAddFirm")
        self.pushButtonAddFirm.clicked.connect(self.createFirm)
        self.radioButtonDisablePermission.setAutoExclusive(False)
        self.radioButtonDisableNoPermission.setAutoExclusive(False)
        self.radioButtonDisableNoPermission.clicked.connect(self.disableSet)
        self.radioButtonDisablePermission.clicked.connect(self.disableUnset)


        self.retranslateUi(FormAddFirm)
        QtCore.QMetaObject.connectSlotsByName(FormAddFirm)

    def disableSet(self):
        self.radioButtonDisablePermission.setChecked(False)
    def disableUnset(self):
        self.radioButtonDisableNoPermission.setChecked(False)

    def createFirm(self):
        if (self.lineEditFirmName.text() != '' and self.lineEditFirmAddress.text() != '' and \
            self.lineEditFirmPhone.text() != '') and (self.radioButtonDisablePermission.isChecked() or
            self.radioButtonDisableNoPermission.isChecked()) and (self.radioButtonRegisteryRelax.isChecked() or
            self.radioButtonRegisteryStrict.isChecked()):
            new_firm = {
                "name_": self.lineEditFirmName.text(),
                "address": self.lineEditFirmAddress.text(),
                "phone": self.lineEditFirmPhone.text(),
                "req_grad_level": self.comboBoxEducation.currentText(),
                "disable_permission": self.radioButtonDisablePermission.isChecked(),
                "registery_permission": self.radioButtonRegisteryRelax.isChecked()  # izin var = true
            }
            vtConnection.addNewFirm(new_firm)
            messageBox = QtWidgets.QMessageBox()
            messageBox.setIcon(QtWidgets.QMessageBox.Information)
            messageBox.setText('Firma başarıyla eklendi')
            messageBox.setWindowTitle('Alert')
            messageBox.exec()

        return print('Alanlarin hepsini doldurun!')

    def retranslateUi(self, FormAddFirm):
        _translate = QtCore.QCoreApplication.translate
        FormAddFirm.setWindowTitle(_translate("FormAddFirm", "Form"))
        self.label.setText(_translate("FormAddFirm", "Şirket Ekle"))
        self.label_3.setText(_translate("FormAddFirm", "İsim:"))
        self.label_4.setText(_translate("FormAddFirm", "Adres:"))
        self.label_5.setText(_translate("FormAddFirm", "Telefon:"))
        self.label_6.setText(_translate("FormAddFirm", "Eğitim Gereksinimi:"))
        self.label_7.setText(_translate("FormAddFirm", "Engel İzni:"))
        self.label_8.setText(_translate("FormAddFirm", "Sicil Koşulu:"))
        self.comboBoxEducation.setItemText(0, _translate("FormAddFirm", "Yok"))
        self.comboBoxEducation.setItemText(1, _translate("FormAddFirm", "İlkokul"))
        self.comboBoxEducation.setItemText(2, _translate("FormAddFirm", "Ortaokul"))
        self.comboBoxEducation.setItemText(3, _translate("FormAddFirm", "Lise"))
        self.comboBoxEducation.setItemText(4, _translate("FormAddFirm", "Ön Lisans"))
        self.comboBoxEducation.setItemText(5, _translate("FormAddFirm", "Lisans"))
        self.comboBoxEducation.setItemText(6, _translate("FormAddFirm", "Lisansüstü"))
        self.radioButtonDisablePermission.setText(_translate("FormAddFirm", "İzin Var"))
        self.radioButtonDisableNoPermission.setText(_translate("FormAddFirm", "İzin Yok"))
        self.radioButtonRegisteryStrict.setText(_translate("FormAddFirm", "Temiz"))
        self.radioButtonRegisteryRelax.setText(_translate("FormAddFirm", "Serbest"))
        self.pushButtonAddFirm.setText(_translate("FormAddFirm", "Oluştur"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormAddFirm = QtWidgets.QWidget()
    ui = Ui_FormAddFirm()
    ui.setupUi(FormAddFirm)
    FormAddFirm.show()
    sys.exit(app.exec_())
