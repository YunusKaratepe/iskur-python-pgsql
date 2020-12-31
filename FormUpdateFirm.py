# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_add_firm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from vt_connection import vtConnection


class Ui_FormUpdateFirm(object):
    def setupUi(self, FormUpdateFirm):
        FormUpdateFirm.setObjectName("FormUpdateFirm")
        FormUpdateFirm.resize(418, 591)
        font = QtGui.QFont()
        font.setPointSize(12)
        FormUpdateFirm.setFont(font)
        self.label = QtWidgets.QLabel(FormUpdateFirm)
        self.label.setGeometry(QtCore.QRect(150, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(FormUpdateFirm)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 120, 24))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FormUpdateFirm)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 120, 24))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(FormUpdateFirm)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 120, 24))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(FormUpdateFirm)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 161, 24))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(FormUpdateFirm)
        self.label_7.setGeometry(QtCore.QRect(20, 310, 101, 24))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(FormUpdateFirm)
        self.label_8.setGeometry(QtCore.QRect(20, 370, 120, 24))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(FormUpdateFirm)
        self.label_9.setGeometry(QtCore.QRect(20, 430, 120, 24))
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(FormUpdateFirm)
        self.label_10.setGeometry(QtCore.QRect(200, 430, 120, 24))
        self.label_10.setObjectName("label_10")

        self.lineEditFirmName = QtWidgets.QLineEdit(FormUpdateFirm)
        self.lineEditFirmName.setGeometry(QtCore.QRect(150, 110, 251, 23))
        self.lineEditFirmName.setObjectName("lineEditFirmName")
        self.lineEditFirmAddress = QtWidgets.QLineEdit(FormUpdateFirm)
        self.lineEditFirmAddress.setGeometry(QtCore.QRect(150, 160, 251, 23))
        self.lineEditFirmAddress.setObjectName("lineEditFirmAddress")
        self.lineEditFirmPhone = QtWidgets.QLineEdit(FormUpdateFirm)
        self.lineEditFirmPhone.setGeometry(QtCore.QRect(150, 210, 251, 23))
        self.lineEditFirmPhone.setObjectName("lineEditFirmPhone")
        self.comboBoxEducation = QtWidgets.QComboBox(FormUpdateFirm)
        self.comboBoxEducation.setGeometry(QtCore.QRect(190, 260, 211, 23))
        self.comboBoxEducation.setObjectName("comboBoxEducation")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")

        self.radioButtonDisablePermission = QtWidgets.QRadioButton(FormUpdateFirm)
        self.radioButtonDisablePermission.setGeometry(QtCore.QRect(150, 315, 100, 21))
        self.radioButtonDisablePermission.setObjectName("radioButtonDisablePermission")
        self.radioButtonDisableNoPermission = QtWidgets.QRadioButton(FormUpdateFirm)
        self.radioButtonDisableNoPermission.setGeometry(QtCore.QRect(280, 315, 131, 21))
        self.radioButtonDisableNoPermission.setObjectName("radioButtonDisableNoPermission")

        self.radioButtonRegisteryStrict = QtWidgets.QRadioButton(FormUpdateFirm)
        self.radioButtonRegisteryStrict.setGeometry(QtCore.QRect(150, 370, 100, 21))
        self.radioButtonRegisteryStrict.setObjectName("radioButtonRegisteryStrict")
        self.radioButtonRegisteryRelax = QtWidgets.QRadioButton(FormUpdateFirm)
        self.radioButtonRegisteryRelax.setGeometry(QtCore.QRect(280, 370, 100, 21))
        self.radioButtonRegisteryRelax.setObjectName("radioButtonRegisteryRelax")
        self.pushButtonAddFirm = QtWidgets.QPushButton(FormUpdateFirm)
        self.pushButtonAddFirm.setGeometry(QtCore.QRect(110, 500, 181, 31))
        self.pushButtonAddFirm.setObjectName("pushButtonAddFirm")
        self.pushButtonAddFirm.clicked.connect(self.updateFirm)
        self.radioButtonDisablePermission.setAutoExclusive(False)
        self.radioButtonDisableNoPermission.setAutoExclusive(False)
        self.radioButtonDisableNoPermission.clicked.connect(self.disableSet)
        self.radioButtonDisablePermission.clicked.connect(self.disableUnset)
        self.firm_id = None

        self.retranslateUi(FormUpdateFirm)
        QtCore.QMetaObject.connectSlotsByName(FormUpdateFirm)

    def disableSet(self):
        self.radioButtonDisablePermission.setChecked(False)
    def disableUnset(self):
        self.radioButtonDisableNoPermission.setChecked(False)

    def updateFirm(self):
        if (self.lineEditFirmName.text() != '' and self.lineEditFirmAddress.text() != '' and \
            self.lineEditFirmPhone.text() != '') and (self.radioButtonDisablePermission.isChecked() or
            self.radioButtonDisableNoPermission.isChecked()) and (self.radioButtonRegisteryRelax.isChecked() or
            self.radioButtonRegisteryStrict.isChecked()):
            messageBox = QtWidgets.QMessageBox.question(None, 'Güncelle', 'Güncellemek istediğinize emin misiniz?',
                                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
            if messageBox == QtWidgets.QMessageBox.Yes:
                new_firm = {
                    "id": self.firm_id,
                    "name_": self.lineEditFirmName.text(),
                    "address": self.lineEditFirmAddress.text(),
                    "phone": self.lineEditFirmPhone.text(),
                    "req_grad_level": self.comboBoxEducation.currentText(),
                    "disable_permission": self.radioButtonDisablePermission.isChecked(),
                    "registery_permission": self.radioButtonRegisteryRelax.isChecked()  # izin var = true
                }
                vtConnection.updateFirm(new_firm)
        else:
            messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Güncelle',
                                               'Güncelleme işleminde alanlar boş bırakılamaz.')
            messageBox.exec_()

    def retranslateUi(self, FormUpdateFirm):
        _translate = QtCore.QCoreApplication.translate
        FormUpdateFirm.setWindowTitle(_translate("FormUpdateFirm", "Form"))
        self.label.setText(_translate("FormUpdateFirm", "Şirket Ekle"))
        self.label_3.setText(_translate("FormUpdateFirm", "İsim:"))
        self.label_4.setText(_translate("FormUpdateFirm", "Adres:"))
        self.label_5.setText(_translate("FormUpdateFirm", "Telefon:"))
        self.label_6.setText(_translate("FormUpdateFirm", "Eğitim Gereksinimi:"))
        self.label_7.setText(_translate("FormUpdateFirm", "Engel İzni:"))
        self.label_8.setText(_translate("FormUpdateFirm", "Sicil Koşulu:"))
        self.label_9.setText(_translate("FromUpdateFirm", "Toplam Maaş:"))
        self.label_10.setText(_translate("FormUpdateFirm", "0.0"))
        self.comboBoxEducation.setItemText(0, _translate("FormUpdateFirm", "Yok"))
        self.comboBoxEducation.setItemText(1, _translate("FormUpdateFirm", "İlkokul"))
        self.comboBoxEducation.setItemText(2, _translate("FormUpdateFirm", "Ortaokul"))
        self.comboBoxEducation.setItemText(3, _translate("FormUpdateFirm", "Lise"))
        self.comboBoxEducation.setItemText(4, _translate("FormUpdateFirm", "Ön Lisans"))
        self.comboBoxEducation.setItemText(5, _translate("FormUpdateFirm", "Lisans"))
        self.comboBoxEducation.setItemText(6, _translate("FormUpdateFirm", "Lisansüstü"))
        self.radioButtonDisablePermission.setText(_translate("FormUpdateFirm", "İzin Var"))
        self.radioButtonDisableNoPermission.setText(_translate("FormUpdateFirm", "İzin Yok"))
        self.radioButtonRegisteryStrict.setText(_translate("FormUpdateFirm", "Temiz"))
        self.radioButtonRegisteryRelax.setText(_translate("FormUpdateFirm", "Serbest"))
        self.pushButtonAddFirm.setText(_translate("FormUpdateFirm", "Güncelle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormUpdateFirm = QtWidgets.QWidget()
    ui = Ui_FormUpdateFirm()
    ui.setupUi(FormUpdateFirm)
    FormUpdateFirm.show()
    sys.exit(app.exec_())
