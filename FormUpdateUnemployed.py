# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_update_unemployed.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from vt_connection import vtConnection


class Ui_FormUpdateUnemployed(object):
    def setupUi(self, FormUpdateUnemployed):
        FormUpdateUnemployed.setObjectName("FormUpdateUnemployed")
        FormUpdateUnemployed.resize(412, 660)
        font = QtGui.QFont()
        font.setPointSize(12)
        FormUpdateUnemployed.setFont(font)
        FormUpdateUnemployed.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label = QtWidgets.QLabel(FormUpdateUnemployed)
        self.label.setGeometry(QtCore.QRect(140, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(FormUpdateUnemployed)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 120, 24))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FormUpdateUnemployed)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 120, 24))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(FormUpdateUnemployed)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 120, 24))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(FormUpdateUnemployed)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 161, 24))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(FormUpdateUnemployed)
        self.label_7.setGeometry(QtCore.QRect(20, 310, 131, 24))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(FormUpdateUnemployed)
        self.label_8.setGeometry(QtCore.QRect(20, 400, 120, 24))
        self.label_8.setObjectName("label_8")
        self.lineEditPersonName = QtWidgets.QLineEdit(FormUpdateUnemployed)
        self.lineEditPersonName.setGeometry(QtCore.QRect(150, 110, 251, 23))
        self.lineEditPersonName.setObjectName("lineEditPersonName")
        self.lineEditPersonJob = QtWidgets.QLineEdit(FormUpdateUnemployed)
        self.lineEditPersonJob.setGeometry(QtCore.QRect(150, 160, 251, 23))
        self.lineEditPersonJob.setObjectName("lineEditPersonJob")
        self.comboBoxEducation = QtWidgets.QComboBox(FormUpdateUnemployed)
        self.comboBoxEducation.setGeometry(QtCore.QRect(160, 260, 241, 23))
        self.comboBoxEducation.setObjectName("comboBoxEducation")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.radioButtonNotDisabled = QtWidgets.QRadioButton(FormUpdateUnemployed)
        self.radioButtonNotDisabled.setGeometry(QtCore.QRect(20, 350, 120, 21))
        self.radioButtonNotDisabled.setObjectName("radioButtonNotDisabled")
        self.radioButtonDisabled = QtWidgets.QRadioButton(FormUpdateUnemployed)
        self.radioButtonDisabled.setGeometry(QtCore.QRect(190, 350, 131, 21))
        self.radioButtonDisabled.setObjectName("radioButtonDisabled")
        self.radioButtonRegisteryClean = QtWidgets.QRadioButton(FormUpdateUnemployed)
        self.radioButtonRegisteryClean.setGeometry(QtCore.QRect(150, 400, 100, 21))
        self.radioButtonRegisteryClean.setObjectName("radioButtonRegisteryClean")
        self.radioButtonRegisteryNotClean = QtWidgets.QRadioButton(FormUpdateUnemployed)
        self.radioButtonRegisteryNotClean.setGeometry(QtCore.QRect(280, 400, 131, 21))
        self.radioButtonRegisteryNotClean.setObjectName("radioButtonRegisteryNotClean")
        self.label_9 = QtWidgets.QLabel(FormUpdateUnemployed)
        self.label_9.setGeometry(QtCore.QRect(20, 60, 120, 24))
        self.label_9.setObjectName("label_9")
        self.lineEditPersonTcNo = QtWidgets.QLineEdit(FormUpdateUnemployed)
        self.lineEditPersonTcNo.setGeometry(QtCore.QRect(150, 60, 251, 23))
        self.lineEditPersonTcNo.setObjectName("lineEditPersonTcNo")
        self.label_10 = QtWidgets.QLabel(FormUpdateUnemployed)
        self.label_10.setGeometry(QtCore.QRect(20, 450, 120, 24))
        self.label_10.setObjectName("label_10")
        self.radioButtonMarried = QtWidgets.QRadioButton(FormUpdateUnemployed)
        self.radioButtonMarried.setGeometry(QtCore.QRect(150, 450, 100, 21))
        self.radioButtonMarried.setObjectName("radioButtonMarried")
        self.radioButtonSingle = QtWidgets.QRadioButton(FormUpdateUnemployed)
        self.radioButtonSingle.setGeometry(QtCore.QRect(270, 450, 100, 21))
        self.radioButtonSingle.setObjectName("radioButtonSingle")
        self.pushButtonUpdateUnemployed = QtWidgets.QPushButton(FormUpdateUnemployed)
        self.pushButtonUpdateUnemployed.setGeometry(QtCore.QRect(110, 600, 171, 31))
        self.pushButtonUpdateUnemployed.setObjectName("pushButtonUpdateUnemployed")
        self.label_11 = QtWidgets.QLabel(FormUpdateUnemployed)
        self.label_11.setGeometry(QtCore.QRect(20, 500, 120, 24))
        self.label_11.setObjectName("label_11")
        self.radioButtonGenderMale = QtWidgets.QRadioButton(FormUpdateUnemployed)
        self.radioButtonGenderMale.setGeometry(QtCore.QRect(150, 500, 100, 21))
        self.radioButtonGenderMale.setObjectName("radioButtonGenderMale")
        self.radioButtonGenderFemale = QtWidgets.QRadioButton(FormUpdateUnemployed)
        self.radioButtonGenderFemale.setGeometry(QtCore.QRect(270, 500, 100, 21))
        self.radioButtonGenderFemale.setObjectName("radioButtonGenderFemale")
        self.dateEditBirthday = QtWidgets.QDateEdit(FormUpdateUnemployed)
        self.dateEditBirthday.setGeometry(QtCore.QRect(160, 550, 121, 31))
        self.dateEditBirthday.setObjectName("dateEditBirthday")
        self.label_12 = QtWidgets.QLabel(FormUpdateUnemployed)
        self.label_12.setGeometry(QtCore.QRect(20, 550, 120, 24))
        self.label_12.setObjectName("label_12")
        self.spinBoxExperience = QtWidgets.QSpinBox(FormUpdateUnemployed)
        self.spinBoxExperience.setGeometry(QtCore.QRect(180, 210, 141, 24))
        self.spinBoxExperience.setObjectName("spinBoxExperience")

        self.retranslateUi(FormUpdateUnemployed)
        QtCore.QMetaObject.connectSlotsByName(FormUpdateUnemployed)

    def retranslateUi(self, FormUpdateUnemployed):
        _translate = QtCore.QCoreApplication.translate
        FormUpdateUnemployed.setWindowTitle(_translate("FormUpdateUnemployed", "Form"))
        self.label.setText(_translate("FormUpdateUnemployed", "Başvuru Ekle"))
        self.label_3.setText(_translate("FormUpdateUnemployed", "İsim:"))
        self.label_4.setText(_translate("FormUpdateUnemployed", "Meslek:"))
        self.label_5.setText(_translate("FormUpdateUnemployed", "Tecrübe (yıl):"))
        self.label_6.setText(_translate("FormUpdateUnemployed", "Eğitim Seviyesi:"))
        self.label_7.setText(_translate("FormUpdateUnemployed", "Engel Durumu:"))
        self.label_8.setText(_translate("FormUpdateUnemployed", "Sicil Durumu:"))
        self.comboBoxEducation.setItemText(0, _translate("FormUpdateUnemployed", "Yok"))
        self.comboBoxEducation.setItemText(1, _translate("FormUpdateUnemployed", "İlkokul"))
        self.comboBoxEducation.setItemText(2, _translate("FormUpdateUnemployed", "Ortaokul"))
        self.comboBoxEducation.setItemText(3, _translate("FormUpdateUnemployed", "Lise"))
        self.comboBoxEducation.setItemText(4, _translate("FormUpdateUnemployed", "Ön Lisans"))
        self.comboBoxEducation.setItemText(5, _translate("FormUpdateUnemployed", "Lisans"))
        self.comboBoxEducation.setItemText(6, _translate("FormUpdateUnemployed", "Lisansüstü"))

        self.radioButtonRegisteryClean.setText(_translate("FormUpdateUnemployed", "Temiz"))
        self.radioButtonRegisteryNotClean.setText(_translate("FormUpdateUnemployed", "Temiz Değil"))
        self.label_9.setText(_translate("FormUpdateUnemployed", "TC No:"))
        self.label_10.setText(_translate("FormUpdateUnemployed", "Medeni Hali:"))
        self.radioButtonMarried.setText(_translate("FormUpdateUnemployed", "Evli"))
        self.radioButtonSingle.setText(_translate("FormUpdateUnemployed", "Bekar"))
        self.pushButtonUpdateUnemployed.setText(_translate("FormUpdateUnemployed", "Oluştur"))
        self.label_11.setText(_translate("FormUpdateUnemployed", "Cinsiyet:"))
        self.radioButtonGenderMale.setText(_translate("FormUpdateUnemployed", "Erkek"))
        self.radioButtonGenderFemale.setText(_translate("FormUpdateUnemployed", "Kadın"))
        self.radioButtonNotDisabled.setText(_translate("FormUpdateUnemployed", "Engeli Yok"))
        self.radioButtonDisabled.setText(_translate("FormUpdateUnemployed", "Engeli Var"))
        self.label_12.setText(_translate("FormUpdateUnemployed", "Doğum Tarihi:"))
        self.pushButtonUpdateUnemployed.clicked.connect(self.updateUnemployed)
        self.radioButtonRegisteryClean.setAutoExclusive(False)
        self.radioButtonRegisteryNotClean.setAutoExclusive(False)
        self.radioButtonMarried.setAutoExclusive(False)
        self.radioButtonSingle.setAutoExclusive(False)
        self.radioButtonGenderFemale.setAutoExclusive(False)
        self.radioButtonGenderMale.setAutoExclusive(False)
        self.radioButtonGenderFemale.clicked.connect(self.radioSetMale)
        self.radioButtonGenderMale.clicked.connect(self.radioSetFemale)
        self.radioButtonRegisteryClean.clicked.connect(self.radioSetRegisteryNotClean)
        self.radioButtonRegisteryNotClean.clicked.connect(self.radioSetRegisteryClean)
        self.radioButtonSingle.clicked.connect(self.radioSetMarried)
        self.radioButtonMarried.clicked.connect(self.radioSetSingle)

    def radioSetFemale(self):
        self.radioButtonGenderFemale.setChecked(False)

    def radioSetMale(self):
        self.radioButtonGenderMale.setChecked(False)

    def radioSetRegisteryNotClean(self):
        self.radioButtonRegisteryNotClean.setChecked(False)

    def radioSetRegisteryClean(self):
        self.radioButtonRegisteryClean.setChecked(False)

    def radioSetMarried(self):
        self.radioButtonMarried.setChecked(False)

    def radioSetSingle(self):
        self.radioButtonSingle.setChecked(False)

    def updateUnemployed(self):
        if (self.lineEditPersonTcNo != '' and self.lineEditPersonJob != '' and self.lineEditPersonName != '') \
                and (self.radioButtonDisabled.isChecked() or self.radioButtonNotDisabled.isChecked()) \
                and (self.radioButtonRegisteryClean.isChecked() or self.radioButtonRegisteryNotClean.isChecked())\
                and (self.radioButtonMarried.isChecked() or self.radioButtonSingle.isChecked()) and \
                (self.radioButtonGenderMale.isChecked() or self.radioButtonGenderFemale.isChecked()):
            messageBox = QtWidgets.QMessageBox.question(None, 'Güncelle', 'Güncellemek istediğinize emin misiniz?',
                                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
            if messageBox == QtWidgets.QMessageBox.Yes:
                new_unemployed = {
                    "ssn": self.lineEditPersonTcNo.text(),
                    "name_": self.lineEditPersonName.text(),
                    "job": self.lineEditPersonJob.text(),
                    "experience": self.spinBoxExperience.value(),
                    "grad_level": self.comboBoxEducation.currentText(),
                    "registery": self.radioButtonRegisteryClean.isChecked(),
                    "disable_level": self.radioButtonDisabled.isChecked(),
                    "marriage": self.radioButtonMarried.isChecked(),
                    "gender": self.radioButtonGenderMale.isChecked(),
                    "birthdate": self.dateEditBirthday.date().toString('dd/MM/yyyy')
                }
                vtConnection.updateUnemployed(new_unemployed)
        else:
            messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information, 'Güncelle',
                                               'Güncelleme işleminde alanlar boş bırakılamaz.')
            messageBox.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormUpdateUnemployed = QtWidgets.QWidget()
    ui = Ui_FormUpdateUnemployed()
    ui.setupUi(FormUpdateUnemployed)
    FormUpdateUnemployed.show()
    sys.exit(app.exec_())

