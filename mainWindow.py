# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medical.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 781, 561))
        self.tabWidget.setStyleSheet("QTabWidget {\n"
"    \n"
"    font: 25 18pt \"Calibri Light\";\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setIconSize(QtCore.QSize(40, 40))
        self.tabWidget.setObjectName("tabWidget")
        self.homeTab = QtWidgets.QWidget()
        self.homeTab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.homeTab.setObjectName("homeTab")
        self.tabWidget.addTab(self.homeTab, "")
        self.drugsTab = QtWidgets.QWidget()
        self.drugsTab.setObjectName("drugsTab")
        self.tableView = QtWidgets.QTableView(self.drugsTab)
        self.tableView.setGeometry(QtCore.QRect(10, 211, 751, 291))
        self.tableView.setObjectName("tableView")
        self.lineEdit = QtWidgets.QLineEdit(self.drugsTab)
        self.lineEdit.setGeometry(QtCore.QRect(60, 30, 113, 20))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.drugsTab)
        self.label.setGeometry(QtCore.QRect(60, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.drugsTab)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 111, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.drugsTab)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 80, 113, 20))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.drugsTab)
        self.label_3.setGeometry(QtCore.QRect(240, 10, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.drugsTab)
        self.label_4.setGeometry(QtCore.QRect(240, 60, 111, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.drugsTab)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 30, 113, 20))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.drugsTab)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 80, 113, 20))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.drugsTab)
        self.label_5.setGeometry(QtCore.QRect(430, 10, 111, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.drugsTab)
        self.textEdit.setGeometry(QtCore.QRect(430, 30, 311, 151))
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.drugsTab)
        self.buttonBox.setGeometry(QtCore.QRect(60, 120, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget.addTab(self.drugsTab, "")
        self.patientsTab = QtWidgets.QWidget()
        self.patientsTab.setObjectName("patientsTab")
        self.tableView_2 = QtWidgets.QTableView(self.patientsTab)
        self.tableView_2.setGeometry(QtCore.QRect(10, 210, 751, 291))
        self.tableView_2.setObjectName("tableView_2")
        self.addPatientButton = QtWidgets.QPushButton(self.patientsTab)
        self.addPatientButton.setGeometry(QtCore.QRect(200, 50, 121, 41))
        self.addPatientButton.setObjectName("addPatientButton")
        self.tabWidget.addTab(self.patientsTab, "")
        self.prescriptionsTab = QtWidgets.QWidget()
        self.prescriptionsTab.setObjectName("prescriptionsTab")
        self.tableView_3 = QtWidgets.QTableView(self.prescriptionsTab)
        self.tableView_3.setGeometry(QtCore.QRect(10, 210, 751, 291))
        self.tableView_3.setObjectName("tableView_3")
        self.tabWidget.addTab(self.prescriptionsTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), _translate("MainWindow", "Home"))
        self.label.setText(_translate("MainWindow", "Drug Name:"))
        self.label_2.setText(_translate("MainWindow", "Time to Peak:"))
        self.label_3.setText(_translate("MainWindow", "Drug Strength:"))
        self.label_4.setText(_translate("MainWindow", "Drug Duration:"))
        self.label_5.setText(_translate("MainWindow", "Notes:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.drugsTab), _translate("MainWindow", "Drugs"))
        self.addPatientButton.setText(_translate("MainWindow", "Add Patient"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.patientsTab), _translate("MainWindow", "Patients"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.prescriptionsTab), _translate("MainWindow", "Prescriptions"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
