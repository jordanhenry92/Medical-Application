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
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(30, 10, 441, 31))
        self.titleLabel.setStyleSheet("QLabel {\n"
"    background-color: rgb(158, 160, 255);\n"
"    font: 25 18pt \"Calibri Light\";\n"
"}")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.drugImage = QtWidgets.QLabel(self.centralwidget)
        self.drugImage.setGeometry(QtCore.QRect(30, 60, 191, 201))
        self.drugImage.setText("")
        self.drugImage.setPixmap(QtGui.QPixmap("images/medicine-silhouette.jpg"))
        self.drugImage.setScaledContents(True)
        self.drugImage.setObjectName("drugImage")
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
        self.drugNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.drugNameLabel.setGeometry(QtCore.QRect(250, 60, 71, 21))
        self.drugNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drugNameLabel.setObjectName("drugNameLabel")
        self.dinLine = QtWidgets.QLineEdit(self.centralwidget)
        self.dinLine.setGeometry(QtCore.QRect(330, 100, 141, 21))
        self.dinLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.dinLine.setText("")
        self.dinLine.setMaxLength(7)
        self.dinLine.setObjectName("dinLine")
        self.dinLabel = QtWidgets.QLabel(self.centralwidget)
        self.dinLabel.setGeometry(QtCore.QRect(240, 100, 81, 21))
        self.dinLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dinLabel.setObjectName("dinLabel")
        self.drugClassLabel = QtWidgets.QLabel(self.centralwidget)
        self.drugClassLabel.setGeometry(QtCore.QRect(250, 140, 71, 21))
        self.drugClassLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drugClassLabel.setObjectName("drugClassLabel")
        self.drugAdminLabel = QtWidgets.QLabel(self.centralwidget)
        self.drugAdminLabel.setGeometry(QtCore.QRect(240, 180, 81, 21))
        self.drugAdminLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drugAdminLabel.setObjectName("drugAdminLabel")
        self.dClassLine = QtWidgets.QLineEdit(self.centralwidget)
        self.dClassLine.setGeometry(QtCore.QRect(330, 140, 141, 21))
        self.dClassLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.dClassLine.setText("")
        self.dClassLine.setObjectName("dClassLine")
        self.dAdminLine = QtWidgets.QLineEdit(self.centralwidget)
        self.dAdminLine.setGeometry(QtCore.QRect(330, 180, 141, 21))
        self.dAdminLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.dAdminLine.setText("")
        self.dAdminLine.setObjectName("dAdminLine")
        self.numIngredLabel = QtWidgets.QLabel(self.centralwidget)
        self.numIngredLabel.setGeometry(QtCore.QRect(210, 260, 111, 21))
        self.numIngredLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numIngredLabel.setObjectName("numIngredLabel")
        self.dIngredBox = QtWidgets.QComboBox(self.centralwidget)
        self.dIngredBox.setGeometry(QtCore.QRect(330, 260, 141, 22))
        self.dIngredBox.setFrame(True)
        self.dIngredBox.setObjectName("dIngredBox")
        self.dIngredBox.addItem("")
        self.dIngredBox.addItem("")
        self.dIngredBox.addItem("")
        self.dIngredBox.addItem("")
        self.dIngredBox.addItem("")
        self.dIngredBox.addItem("")
        self.dIngredBox.addItem("")
        self.dIngredBox.addItem("")
        self.dDosageLine = QtWidgets.QLineEdit(self.centralwidget)
        self.dDosageLine.setGeometry(QtCore.QRect(330, 220, 141, 21))
        self.dDosageLine.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.dDosageLine.setText("")
        self.dDosageLine.setObjectName("dDosageLine")
        self.drugDosageLabel = QtWidgets.QLabel(self.centralwidget)
        self.drugDosageLabel.setGeometry(QtCore.QRect(240, 220, 81, 21))
        self.drugDosageLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drugDosageLabel.setObjectName("drugDosageLabel")
        NewDrugWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NewDrugWindow)
        self.statusbar.setObjectName("statusbar")
        NewDrugWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NewDrugWindow)
        QtCore.QMetaObject.connectSlotsByName(NewDrugWindow)

    def retranslateUi(self, NewDrugWindow):
        _translate = QtCore.QCoreApplication.translate
        NewDrugWindow.setWindowTitle(_translate("NewDrugWindow", "MainWindow"))
        self.titleLabel.setText(_translate("NewDrugWindow", "New Drug"))
        self.drugNameLabel.setText(_translate("NewDrugWindow", "Drug Name:"))
        self.dinLine.setInputMask(_translate("NewDrugWindow", "9999999"))
        self.dinLabel.setText(_translate("NewDrugWindow", "DIN:"))
        self.drugClassLabel.setText(_translate("NewDrugWindow", "Class:"))
        self.drugAdminLabel.setText(_translate("NewDrugWindow", "Administration:"))
        self.numIngredLabel.setText(_translate("NewDrugWindow", "# Active Ingredients:"))
        self.dIngredBox.setItemText(0, _translate("NewDrugWindow", "1"))
        self.dIngredBox.setItemText(1, _translate("NewDrugWindow", "2"))
        self.dIngredBox.setItemText(2, _translate("NewDrugWindow", "3"))
        self.dIngredBox.setItemText(3, _translate("NewDrugWindow", "4"))
        self.dIngredBox.setItemText(4, _translate("NewDrugWindow", "5"))
        self.dIngredBox.setItemText(5, _translate("NewDrugWindow", "6"))
        self.dIngredBox.setItemText(6, _translate("NewDrugWindow", "7"))
        self.dIngredBox.setItemText(7, _translate("NewDrugWindow", "8"))
        self.drugDosageLabel.setText(_translate("NewDrugWindow", "Dosage form:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewDrugWindow = QtWidgets.QMainWindow()
    ui = Ui_NewDrugWindow()
    ui.setupUi(NewDrugWindow)
    NewDrugWindow.show()
    sys.exit(app.exec_())
