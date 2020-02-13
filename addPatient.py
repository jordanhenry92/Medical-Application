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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 70, 141, 21))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 441, 31))
        self.label.setStyleSheet("QLabel {\n"
"    background-color: rgb(158, 160, 255);\n"
"    font: 25 18pt \"Calibri Light\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 120, 141, 21))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 170, 141, 21))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 220, 141, 21))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 70, 71, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 120, 71, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 170, 71, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 220, 71, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 60, 191, 201))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("images/generic-person-silhouette.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(310, 270, 141, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 270, 71, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 310, 141, 21))
        self.lineEdit_5.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(310, 350, 141, 21))
        self.lineEdit_6.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(230, 310, 71, 21))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(230, 350, 71, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(30, 290, 191, 41))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
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
        self.label_2.setText(_translate("NewPatientWindow", "Name:"))
        self.label_3.setText(_translate("NewPatientWindow", "Date of Birth:"))
        self.label_4.setText(_translate("NewPatientWindow", "Phone:"))
        self.label_5.setText(_translate("NewPatientWindow", "Email:"))
        self.comboBox.setItemText(0, _translate("NewPatientWindow", "Alberta"))
        self.comboBox.setItemText(1, _translate("NewPatientWindow", "British Columbia"))
        self.comboBox.setItemText(2, _translate("NewPatientWindow", "Manitoba"))
        self.comboBox.setItemText(3, _translate("NewPatientWindow", "New Brunswick"))
        self.comboBox.setItemText(4, _translate("NewPatientWindow", "Newfound and Labrador"))
        self.comboBox.setItemText(5, _translate("NewPatientWindow", "Nova Scotia"))
        self.comboBox.setItemText(6, _translate("NewPatientWindow", "Ontario"))
        self.comboBox.setItemText(7, _translate("NewPatientWindow", "Prince Edward Island"))
        self.comboBox.setItemText(8, _translate("NewPatientWindow", "Quebec"))
        self.comboBox.setItemText(9, _translate("NewPatientWindow", "Saskatchewan"))
        self.label_7.setText(_translate("NewPatientWindow", "Province:"))
        self.label_8.setText(_translate("NewPatientWindow", "City:"))
        self.label_9.setText(_translate("NewPatientWindow", "Address:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewPatientWindow = QtWidgets.QMainWindow()
    ui = Ui_NewPatientWindow()
    ui.setupUi(NewPatientWindow)
    NewPatientWindow.show()
    sys.exit(app.exec_())
