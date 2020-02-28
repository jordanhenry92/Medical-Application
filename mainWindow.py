# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #1B262C")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 80, 801, 521))
        self.tabWidget.setStyleSheet("QTabWidget {\n"
"    font: 25 16pt \"Calibri Light\" bold;\n"
"}\n"
"\n"
"QTabBar::tab::selected {\n"
"    background-color: #3282B8;\n"
"    color: white;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #BBE1FA\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: none;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setIconSize(QtCore.QSize(70, 70))
        self.tabWidget.setObjectName("tabWidget")
        self.homeTab = QtWidgets.QWidget()
        self.homeTab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.homeTab.setStyleSheet("background-color: #3282B8")
        self.homeTab.setObjectName("homeTab")
        self.label_2 = QtWidgets.QLabel(self.homeTab)
        self.label_2.setGeometry(QtCore.QRect(80, 60, 431, 121))
        self.label_2.setStyleSheet("font: 25 26pt \"Calibri Light\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.homeTab)
        self.label_3.setGeometry(QtCore.QRect(80, 170, 201, 51))
        self.label_3.setStyleSheet("font: 25 18pt \"Calibri Light\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.homeTab)
        self.label_4.setGeometry(QtCore.QRect(90, 250, 131, 41))
        self.label_4.setStyleSheet("font: 25 18pt \"Calibri Light\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.homeTab)
        self.label_5.setGeometry(QtCore.QRect(90, 290, 131, 41))
        self.label_5.setStyleSheet("font: 25 18pt \"Calibri Light\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.homeTab)
        self.label_6.setGeometry(QtCore.QRect(90, 330, 161, 41))
        self.label_6.setStyleSheet("font: 25 18pt \"Calibri Light\";")
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.homeTab, "")
        self.drugsTab = QtWidgets.QWidget()
        self.drugsTab.setStyleSheet("QWidget {\n"
"    background-color: #3282B8\n"
"}\n"
"QPushButton {\n"
"    background-color: #BBE1FA\n"
"}")
        self.drugsTab.setObjectName("drugsTab")
        self.drugsTable = QtWidgets.QTableView(self.drugsTab)
        self.drugsTable.setGeometry(QtCore.QRect(20, 90, 761, 381))
        self.drugsTable.setStyleSheet("background-color: white;")
        self.drugsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.drugsTable.setObjectName("drugsTable")
        self.addDrugButton = QtWidgets.QPushButton(self.drugsTab)
        self.addDrugButton.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.addDrugButton.setObjectName("addDrugButton")
        self.drugSearchBar = QtWidgets.QLineEdit(self.drugsTab)
        self.drugSearchBar.setGeometry(QtCore.QRect(190, 20, 211, 31))
        self.drugSearchBar.setStyleSheet("QLineEdit {\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.drugSearchBar.setObjectName("drugSearchBar")
        self.drugSearchButton = QtWidgets.QPushButton(self.drugsTab)
        self.drugSearchButton.setGeometry(QtCore.QRect(410, 20, 111, 31))
        self.drugSearchButton.setObjectName("drugSearchButton")
        self.remDrugButton = QtWidgets.QPushButton(self.drugsTab)
        self.remDrugButton.setGeometry(QtCore.QRect(570, 20, 111, 31))
        self.remDrugButton.setObjectName("remDrugButton")
        self.drugRefresh = QtWidgets.QPushButton(self.drugsTab)
        self.drugRefresh.setGeometry(QtCore.QRect(730, 20, 41, 41))
        self.drugRefresh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/refresh_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.drugRefresh.setIcon(icon)
        self.drugRefresh.setIconSize(QtCore.QSize(30, 30))
        self.drugRefresh.setObjectName("drugRefresh")
        self.tabWidget.addTab(self.drugsTab, "")
        self.patientsTab = QtWidgets.QWidget()
        self.patientsTab.setStyleSheet("QWidget {\n"
"    background-color: #3282B8\n"
"}\n"
"QPushButton {\n"
"    background-color: #BBE1FA\n"
"}")
        self.patientsTab.setObjectName("patientsTab")
        self.patientsTable = QtWidgets.QTableView(self.patientsTab)
        self.patientsTable.setGeometry(QtCore.QRect(20, 90, 761, 381))
        self.patientsTable.setStyleSheet("background-color: white;")
        self.patientsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.patientsTable.setObjectName("patientsTable")
        self.addPatientButton = QtWidgets.QPushButton(self.patientsTab)
        self.addPatientButton.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.addPatientButton.setObjectName("addPatientButton")
        self.patientSearchBar = QtWidgets.QLineEdit(self.patientsTab)
        self.patientSearchBar.setGeometry(QtCore.QRect(190, 20, 211, 31))
        self.patientSearchBar.setStyleSheet("QLineEdit {\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    border-radius: 5px;\n"
"}")
        self.patientSearchBar.setObjectName("patientSearchBar")
        self.patientSearchButton = QtWidgets.QPushButton(self.patientsTab)
        self.patientSearchButton.setGeometry(QtCore.QRect(410, 20, 111, 31))
        self.patientSearchButton.setObjectName("patientSearchButton")
        self.remPatientButton = QtWidgets.QPushButton(self.patientsTab)
        self.remPatientButton.setGeometry(QtCore.QRect(570, 20, 111, 31))
        self.remPatientButton.setObjectName("remPatientButton")
        self.patientRefresh = QtWidgets.QPushButton(self.patientsTab)
        self.patientRefresh.setGeometry(QtCore.QRect(730, 20, 41, 41))
        self.patientRefresh.setText("")
        self.patientRefresh.setIcon(icon)
        self.patientRefresh.setIconSize(QtCore.QSize(30, 30))
        self.patientRefresh.setObjectName("patientRefresh")
        self.tabWidget.addTab(self.patientsTab, "")
        self.prescriptionsTab = QtWidgets.QWidget()
        self.prescriptionsTab.setStyleSheet("QWidget {\n"
"    background-color: #3282B8\n"
"}\n"
"QPushButton {\n"
"    background-color: #BBE1FA\n"
"}")
        self.prescriptionsTab.setObjectName("prescriptionsTab")
        self.tableView_3 = QtWidgets.QTableView(self.prescriptionsTab)
        self.tableView_3.setGeometry(QtCore.QRect(20, 90, 761, 381))
        self.tableView_3.setStyleSheet("background-color: white;")
        self.tableView_3.setObjectName("tableView_3")
        self.tabWidget.addTab(self.prescriptionsTab, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/ecg_banner.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Welcome to my Medical App!"))
        self.label_3.setText(_translate("MainWindow", "There are currently:"))
        self.label_4.setText(_translate("MainWindow", "0 Drugs"))
        self.label_5.setText(_translate("MainWindow", "0 Patients"))
        self.label_6.setText(_translate("MainWindow", "In the database"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), _translate("MainWindow", "Home"))
        self.addDrugButton.setText(_translate("MainWindow", "Add Drug"))
        self.drugSearchButton.setText(_translate("MainWindow", "Search"))
        self.remDrugButton.setText(_translate("MainWindow", "Remove Drug"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.drugsTab), _translate("MainWindow", "Drugs"))
        self.addPatientButton.setText(_translate("MainWindow", "Add Patient"))
        self.patientSearchButton.setText(_translate("MainWindow", "Search"))
        self.remPatientButton.setText(_translate("MainWindow", "Remove Patient"))
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
