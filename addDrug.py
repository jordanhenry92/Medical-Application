# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addDrug.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewDrugWindow(object):
    def setupUi(self, NewDrugWindow):
        NewDrugWindow.setObjectName("NewDrugWindow")
        NewDrugWindow.resize(496, 428)
        self.centralwidget = QtWidgets.QWidget(NewDrugWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 441, 31))
        self.label.setStyleSheet("QLabel {\n"
"    background-color: rgb(158, 160, 255);\n"
"    font: 25 18pt \"Calibri Light\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 60, 191, 201))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("images/medicine-silhouette.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(30, 300, 191, 41))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.dNameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.dNameLine.setGeometry(QtCore.QRect(330, 60, 141, 21))
        self.dNameLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.dNameLine.setObjectName("dNameLine")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(250, 60, 71, 21))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.dStrengthLine = QtWidgets.QLineEdit(self.centralwidget)
        self.dStrengthLine.setGeometry(QtCore.QRect(330, 100, 141, 21))
        self.dStrengthLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.dStrengthLine.setText("")
        self.dStrengthLine.setObjectName("dStrengthLine")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(240, 100, 81, 21))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(250, 140, 71, 21))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(250, 180, 71, 21))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.dDurationLine = QtWidgets.QLineEdit(self.centralwidget)
        self.dDurationLine.setGeometry(QtCore.QRect(330, 140, 141, 21))
        self.dDurationLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.dDurationLine.setText("")
        self.dDurationLine.setObjectName("dDurationLine")
        self.dTTPLine = QtWidgets.QLineEdit(self.centralwidget)
        self.dTTPLine.setGeometry(QtCore.QRect(330, 180, 141, 21))
        self.dTTPLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.dTTPLine.setText("")
        self.dTTPLine.setObjectName("dTTPLine")
        self.dNoteEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.dNoteEdit.setGeometry(QtCore.QRect(250, 240, 231, 161))
        self.dNoteEdit.setObjectName("dNoteEdit")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(240, 210, 91, 21))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        NewDrugWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NewDrugWindow)
        self.statusbar.setObjectName("statusbar")
        NewDrugWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NewDrugWindow)
        QtCore.QMetaObject.connectSlotsByName(NewDrugWindow)

    def retranslateUi(self, NewDrugWindow):
        _translate = QtCore.QCoreApplication.translate
        NewDrugWindow.setWindowTitle(_translate("NewDrugWindow", "MainWindow"))
        self.label.setText(_translate("NewDrugWindow", "New Drug"))
        self.label_10.setText(_translate("NewDrugWindow", "Drug Name:"))
        self.label_11.setText(_translate("NewDrugWindow", "Drug Strength:"))
        self.label_12.setText(_translate("NewDrugWindow", "Duration:"))
        self.label_13.setText(_translate("NewDrugWindow", "Time to Peak:"))
        self.label_14.setText(_translate("NewDrugWindow", "Doctor\'s notes:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewDrugWindow = QtWidgets.QMainWindow()
    ui = Ui_NewDrugWindow()
    ui.setupUi(NewDrugWindow)
    NewDrugWindow.show()
    sys.exit(app.exec_())
