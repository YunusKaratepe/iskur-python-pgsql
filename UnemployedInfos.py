# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_update_unemployed.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UnemployedInfos(object):
    def setupUi(self, UnemployedInfos):
        UnemployedInfos.setObjectName("UnemployedInfos")
        UnemployedInfos.resize(412, 710)
        font = QtGui.QFont()
        font.setPointSize(12)
        UnemployedInfos.setFont(font)
        UnemployedInfos.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label = QtWidgets.QLabel(UnemployedInfos)
        self.label.setGeometry(QtCore.QRect(140, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(UnemployedInfos)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 120, 24))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(UnemployedInfos)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 120, 24))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(UnemployedInfos)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 120, 24))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(UnemployedInfos)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 161, 24))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(UnemployedInfos)
        self.label_7.setGeometry(QtCore.QRect(20, 310, 131, 24))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(UnemployedInfos)
        self.label_8.setGeometry(QtCore.QRect(20, 400, 120, 24))
        self.label_8.setObjectName("label_8")
        self.lineEditPersonName = QtWidgets.QLineEdit(UnemployedInfos)
        self.lineEditPersonName.setGeometry(QtCore.QRect(150, 110, 251, 23))
        self.lineEditPersonName.setObjectName("lineEditPersonName")
        self.lineEditPersonJob = QtWidgets.QLineEdit(UnemployedInfos)
        self.lineEditPersonJob.setGeometry(QtCore.QRect(150, 160, 251, 23))
        self.lineEditPersonJob.setObjectName("lineEditPersonJob")

        self.lineEditSalary = QtWidgets.QLineEdit(UnemployedInfos)
        self.lineEditSalary.setGeometry(QtCore.QRect(150, 600, 251, 23))
        self.lineEditSalary.setObjectName("lineEditSalary")
        self.lineEditSalary.setValidator(QtGui.QIntValidator())

        self.comboBoxEducation = QtWidgets.QComboBox(UnemployedInfos)
        self.comboBoxEducation.setGeometry(QtCore.QRect(160, 260, 241, 23))
        self.comboBoxEducation.setObjectName("comboBoxEducation")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.comboBoxEducation.addItem("")
        self.radioButtonNotDisabled = QtWidgets.QRadioButton(UnemployedInfos)
        self.radioButtonNotDisabled.setGeometry(QtCore.QRect(20, 350, 120, 21))
        self.radioButtonNotDisabled.setObjectName("radioButtonNotDisabled")
        self.radioButtonDisabled = QtWidgets.QRadioButton(UnemployedInfos)
        self.radioButtonDisabled.setGeometry(QtCore.QRect(190, 350, 131, 21))
        self.radioButtonDisabled.setObjectName("radioButtonDisabled")
        self.radioButtonRegisteryClean = QtWidgets.QRadioButton(UnemployedInfos)
        self.radioButtonRegisteryClean.setGeometry(QtCore.QRect(150, 400, 100, 21))
        self.radioButtonRegisteryClean.setObjectName("radioButtonRegisteryClean")
        self.radioButtonRegisteryNotClean = QtWidgets.QRadioButton(UnemployedInfos)
        self.radioButtonRegisteryNotClean.setGeometry(QtCore.QRect(280, 400, 131, 21))
        self.radioButtonRegisteryNotClean.setObjectName("radioButtonRegisteryNotClean")
        self.label_9 = QtWidgets.QLabel(UnemployedInfos)
        self.label_9.setGeometry(QtCore.QRect(20, 60, 120, 24))
        self.label_9.setObjectName("label_9")
        self.lineEditPersonTcNo = QtWidgets.QLineEdit(UnemployedInfos)
        self.lineEditPersonTcNo.setGeometry(QtCore.QRect(150, 60, 251, 23))
        self.lineEditPersonTcNo.setObjectName("lineEditPersonTcNo")
        self.label_10 = QtWidgets.QLabel(UnemployedInfos)
        self.label_10.setGeometry(QtCore.QRect(20, 450, 120, 24))
        self.label_10.setObjectName("label_10")
        self.radioButtonMarried = QtWidgets.QRadioButton(UnemployedInfos)
        self.radioButtonMarried.setGeometry(QtCore.QRect(150, 450, 100, 21))
        self.radioButtonMarried.setObjectName("radioButtonMarried")
        self.radioButtonSingle = QtWidgets.QRadioButton(UnemployedInfos)
        self.radioButtonSingle.setGeometry(QtCore.QRect(270, 450, 100, 21))
        self.radioButtonSingle.setObjectName("radioButtonSingle")

        self.pushButtonHireUnemployed = QtWidgets.QPushButton(UnemployedInfos)
        self.pushButtonHireUnemployed.setGeometry(QtCore.QRect(40, 650, 150, 30))
        self.pushButtonHireUnemployed.setObjectName("pushButtonHireUnemployed")

        self.pushButtonDenyUnemployed = QtWidgets.QPushButton(UnemployedInfos)
        self.pushButtonDenyUnemployed.setGeometry(QtCore.QRect(220, 650, 150, 30))
        self.pushButtonDenyUnemployed.setObjectName("pushButtonDenyUnemployed")

        self.label_11 = QtWidgets.QLabel(UnemployedInfos)
        self.label_11.setGeometry(QtCore.QRect(20, 500, 120, 24))
        self.label_11.setObjectName("label_11")
        self.radioButtonGenderMale = QtWidgets.QRadioButton(UnemployedInfos)
        self.radioButtonGenderMale.setGeometry(QtCore.QRect(150, 500, 100, 21))
        self.radioButtonGenderMale.setObjectName("radioButtonGenderMale")
        self.radioButtonGenderFemale = QtWidgets.QRadioButton(UnemployedInfos)
        self.radioButtonGenderFemale.setGeometry(QtCore.QRect(270, 500, 100, 21))
        self.radioButtonGenderFemale.setObjectName("radioButtonGenderFemale")
        self.dateEditBirthday = QtWidgets.QDateEdit(UnemployedInfos)
        self.dateEditBirthday.setGeometry(QtCore.QRect(160, 550, 121, 31))
        self.dateEditBirthday.setObjectName("dateEditBirthday")
        self.label_12 = QtWidgets.QLabel(UnemployedInfos)
        self.label_12.setGeometry(QtCore.QRect(20, 550, 120, 24))
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(UnemployedInfos)
        self.label_13.setGeometry(QtCore.QRect(20, 600, 120, 24))
        self.label_13.setObjectName("label_13")
        self.spinBoxExperience = QtWidgets.QSpinBox(UnemployedInfos)
        self.spinBoxExperience.setGeometry(QtCore.QRect(180, 210, 141, 24))
        self.spinBoxExperience.setObjectName("spinBoxExperience")

        self.retranslateUi(UnemployedInfos)
        QtCore.QMetaObject.connectSlotsByName(UnemployedInfos)

    def retranslateUi(self, UnemployedInfos):
        _translate = QtCore.QCoreApplication.translate
        UnemployedInfos.setWindowTitle(_translate("UnemployedInfos", "Form"))
        self.label.setText(_translate("UnemployedInfos", "Başvuru Ekle"))
        self.label_3.setText(_translate("UnemployedInfos", "İsim:"))
        self.label_4.setText(_translate("UnemployedInfos", "Meslek:"))
        self.label_5.setText(_translate("UnemployedInfos", "Tecrübe (yıl):"))
        self.label_6.setText(_translate("UnemployedInfos", "Eğitim Seviyesi:"))
        self.label_7.setText(_translate("UnemployedInfos", "Engel Durumu:"))
        self.label_8.setText(_translate("UnemployedInfos", "Sicil Durumu:"))
        self.comboBoxEducation.setItemText(0, _translate("UnemployedInfos", "Yok"))
        self.comboBoxEducation.setItemText(1, _translate("UnemployedInfos", "İlkokul"))
        self.comboBoxEducation.setItemText(2, _translate("UnemployedInfos", "Ortaokul"))
        self.comboBoxEducation.setItemText(3, _translate("UnemployedInfos", "Lise"))
        self.comboBoxEducation.setItemText(4, _translate("UnemployedInfos", "Ön Lisans"))
        self.comboBoxEducation.setItemText(5, _translate("UnemployedInfos", "Lisans"))
        self.comboBoxEducation.setItemText(6, _translate("UnemployedInfos", "Lisansüstü"))

        self.radioButtonRegisteryClean.setText(_translate("UnemployedInfos", "Temiz"))
        self.radioButtonRegisteryNotClean.setText(_translate("UnemployedInfos", "Temiz Değil"))
        self.label_9.setText(_translate("UnemployedInfos", "TC No:"))
        self.label_10.setText(_translate("UnemployedInfos", "Medeni Hali:"))
        self.radioButtonMarried.setText(_translate("UnemployedInfos", "Evli"))
        self.radioButtonSingle.setText(_translate("UnemployedInfos", "Bekar"))
        self.pushButtonHireUnemployed.setText(_translate("UnemployedInfos", "İşe Al"))
        self.pushButtonDenyUnemployed.setText(_translate("UnemployedInfos", "Reddet"))
        self.label_11.setText(_translate("UnemployedInfos", "Cinsiyet:"))
        self.radioButtonGenderMale.setText(_translate("UnemployedInfos", "Erkek"))
        self.radioButtonGenderFemale.setText(_translate("UnemployedInfos", "Kadın"))
        self.radioButtonNotDisabled.setText(_translate("UnemployedInfos", "Engeli Yok"))
        self.radioButtonDisabled.setText(_translate("UnemployedInfos", "Engeli Var"))
        self.label_12.setText(_translate("UnemployedInfos", "Doğum Tarihi:"))
        self.label_13.setText(_translate("UnemployedInfos", "Maaş (TL):"))
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
        self.unemloyed_ssn = None
        self.firm_id = None

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UnemployedInfos = QtWidgets.QWidget()
    ui = Ui_UnemployedInfos()
    ui.setupUi(UnemployedInfos)
    UnemployedInfos.show()
    sys.exit(app.exec_())

