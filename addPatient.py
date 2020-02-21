# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addPatient.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewPatientWindow(object):
    def setupUi(self, NewPatientWindow):
        NewPatientWindow.setObjectName("NewPatientWindow")
        NewPatientWindow.resize(493, 426)
        self.centralwidget = QtWidgets.QWidget(NewPatientWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pLastLine = QtWidgets.QLineEdit(self.centralwidget)
        self.pLastLine.setGeometry(QtCore.QRect(310, 140, 141, 21))
        self.pLastLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.pLastLine.setObjectName("pLastLine")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 441, 31))
        self.label.setStyleSheet("QLabel {\n"
"    background-color: rgb(158, 160, 255);\n"
"    font: 25 18pt \"Calibri Light\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pDOBLine = QtWidgets.QLineEdit(self.centralwidget)
        self.pDOBLine.setGeometry(QtCore.QRect(310, 180, 141, 21))
        self.pDOBLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.pDOBLine.setText("")
        self.pDOBLine.setObjectName("pDOBLine")
        self.pPhoneLine = QtWidgets.QLineEdit(self.centralwidget)
        self.pPhoneLine.setGeometry(QtCore.QRect(310, 220, 141, 21))
        self.pPhoneLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.pPhoneLine.setObjectName("pPhoneLine")
        self.pEmailLine = QtWidgets.QLineEdit(self.centralwidget)
        self.pEmailLine.setGeometry(QtCore.QRect(310, 260, 141, 21))
        self.pEmailLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.pEmailLine.setObjectName("pEmailLine")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 140, 71, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 180, 71, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 220, 71, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 260, 71, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 60, 191, 201))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("images/generic-person-silhouette.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pProvinceBox = QtWidgets.QComboBox(self.centralwidget)
        self.pProvinceBox.setGeometry(QtCore.QRect(310, 300, 141, 21))
        self.pProvinceBox.setObjectName("pProvinceBox")
        self.pProvinceBox.addItem("")
        self.pProvinceBox.addItem("")
        self.pProvinceBox.addItem("")
        self.pProvinceBox.addItem("")
        self.pProvinceBox.addItem("")
        self.pProvinceBox.addItem("")
        self.pProvinceBox.addItem("")
        self.pProvinceBox.addItem("")
        self.pProvinceBox.addItem("")
        self.pProvinceBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 300, 71, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.pCityLine = QtWidgets.QLineEdit(self.centralwidget)
        self.pCityLine.setGeometry(QtCore.QRect(310, 340, 141, 21))
        self.pCityLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.pCityLine.setObjectName("pCityLine")
        self.pAddressLine = QtWidgets.QLineEdit(self.centralwidget)
        self.pAddressLine.setGeometry(QtCore.QRect(310, 380, 141, 21))
        self.pAddressLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.pAddressLine.setObjectName("pAddressLine")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 340, 71, 21))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(230, 380, 71, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(30, 290, 191, 41))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pFirstLine = QtWidgets.QLineEdit(self.centralwidget)
        self.pFirstLine.setGeometry(QtCore.QRect(310, 100, 141, 21))
        self.pFirstLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.pFirstLine.setObjectName("pFirstLine")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(230, 100, 71, 21))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.pIDLine = QtWidgets.QLineEdit(self.centralwidget)
        self.pIDLine.setGeometry(QtCore.QRect(310, 60, 141, 21))
        self.pIDLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.pIDLine.setObjectName("pIDLine")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(230, 60, 71, 21))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        NewPatientWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NewPatientWindow)
        self.statusbar.setObjectName("statusbar")
        NewPatientWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NewPatientWindow)
        QtCore.QMetaObject.connectSlotsByName(NewPatientWindow)

    def retranslateUi(self, NewPatientWindow):
        _translate = QtCore.QCoreApplication.translate
        NewPatientWindow.setWindowTitle(_translate("NewPatientWindow", "MainWindow"))
        self.label.setText(_translate("NewPatientWindow", "New Patient"))
        self.label_2.setText(_translate("NewPatientWindow", "Last Name:"))
        self.label_3.setText(_translate("NewPatientWindow", "Date of Birth:"))
        self.label_4.setText(_translate("NewPatientWindow", "Phone:"))
        self.label_5.setText(_translate("NewPatientWindow", "Email:"))
        self.pProvinceBox.setItemText(0, _translate("NewPatientWindow", "Alberta"))
        self.pProvinceBox.setItemText(1, _translate("NewPatientWindow", "British Columbia"))
        self.pProvinceBox.setItemText(2, _translate("NewPatientWindow", "Manitoba"))
        self.pProvinceBox.setItemText(3, _translate("NewPatientWindow", "New Brunswick"))
        self.pProvinceBox.setItemText(4, _translate("NewPatientWindow", "Newfound and Labrador"))
        self.pProvinceBox.setItemText(5, _translate("NewPatientWindow", "Nova Scotia"))
        self.pProvinceBox.setItemText(6, _translate("NewPatientWindow", "Ontario"))
        self.pProvinceBox.setItemText(7, _translate("NewPatientWindow", "Prince Edward Island"))
        self.pProvinceBox.setItemText(8, _translate("NewPatientWindow", "Quebec"))
        self.pProvinceBox.setItemText(9, _translate("NewPatientWindow", "Saskatchewan"))
        self.label_7.setText(_translate("NewPatientWindow", "Province:"))
        self.label_8.setText(_translate("NewPatientWindow", "City:"))
        self.label_9.setText(_translate("NewPatientWindow", "Address:"))
        self.label_10.setText(_translate("NewPatientWindow", "First Name:"))
        self.label_11.setText(_translate("NewPatientWindow", "ID:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewPatientWindow = QtWidgets.QMainWindow()
    ui = Ui_NewPatientWindow()
    ui.setupUi(NewPatientWindow)
    NewPatientWindow.show()
    sys.exit(app.exec_())
