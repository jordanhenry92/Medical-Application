from PyQt5 import QtWidgets, QtSql
#from PyQt5.QtWidgets import QApplication, QMainWindow
import mainWindow, addPatient, addDrug, dbManager
import sys

# Initiliaze the main window and setup buttons for adding patients and drugs
class MainWindow(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("My Medical App")
        self.addPatientButton.clicked.connect(self.on_addPatient_clicked)
        self.addDrugButton.clicked.connect(self.on_addDrug_clicked)
        dbManager.updateView(self.tableView_2)
        
        
    def on_addPatient_clicked(self):
        self.w = AddPatientWindow()
        self.w.show()

    def on_addDrug_clicked(self):
        self.w = AddDrugWindow()
        self.w.show()

    
    

# Set up the window for adding a patient
class AddPatientWindow(QtWidgets.QMainWindow, addPatient.Ui_NewPatientWindow):
    def __init__(self, parent=None):
        super(AddPatientWindow, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.on_addPatient_confirm)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.on_addPatient_cancel)
    
    def on_addPatient_confirm(self):
        print("Patient successfully added!")
        self.close()

    def on_addPatient_cancel(self):
        print("Patient not added.")
        self.close()


# Set up the window for adding a drug
class AddDrugWindow(QtWidgets.QMainWindow, addDrug.Ui_NewDrugWindow):
    def __init__(self, parent=None):
        super(AddDrugWindow, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.on_addDrug_confirm)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.on_addDrug_cancel)

    def on_addDrug_confirm(self):
        print("Drug successfully added!")
        self.close()

    def on_addDrug_cancel(self):
        print("Drug not added.")
        self.close()



def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
