from PyQt5 import QtWidgets, QtSql
import mainWindow, addPatient, addDrug, dbManager
import sys

# Initiliaze the main window and setup buttons for adding patients and drugs
class MainWindow(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("My Medical App")

        # Add all buttons in main window
        self.addPatientButton.clicked.connect(self.on_addPatient_clicked)
        self.addDrugButton.clicked.connect(self.on_addDrug_clicked)
        self.remPatientButton.clicked.connect(self.on_remove_patient_clicked)
        self.remDrugButton.clicked.connect(self.on_remove_drug_clicked)
        self.drugRefresh.clicked.connect(self.refreshDrugsTable)
        self.patientRefresh.clicked.connect(self.refreshPatientsTable)
        self.drugSearchButton.clicked.connect(self.searchDrugs)

        # Update tableviews on initialization
        dbManager.updateDrugsView(self.drugsTable)
        dbManager.updatePatientsView(self.patientsTable)

        #self.prescriptionsTab.hide()
        
    # Opens the interface to add a patient  
    def on_addPatient_clicked(self):
        self.w = AddPatientWindow()
        self.w.show()

    # Opens the interface to add a drug
    def on_addDrug_clicked(self):
        self.w = AddDrugWindow()
        self.w.show()

    # Function to remove patient from table by id number
    def on_remove_patient_clicked(self):
        index = self.patientsTable.selectionModel().currentIndex()
        currID = index.sibling(index.row(), 0).data()
        dbManager.removePatient(currID)
        dbManager.updatePatientsView(self.patientsTable)

    # Function to remove drug from table by drug identification number (din)
    def on_remove_drug_clicked(self):
        index = self.drugsTable.selectionModel().currentIndex()
        currID = index.sibling(index.row(), 0).data()
        dbManager.removeDrug(currID)
        dbManager.updateDrugsView(self.drugsTable)

    def refreshDrugsTable(self):
        dbManager.updateDrugsView(self.drugsTable)

    def refreshPatientsTable(self):
        dbManager.updatePatientsView(self.patientsTable)

    def searchDrugs(self):
        search = self.drugSearchBar.text()
        dbManager.searchDrugs(search)



# Set up the window for adding a patient
class AddPatientWindow(QtWidgets.QMainWindow, addPatient.Ui_NewPatientWindow):
    def __init__(self, parent=None):
        super(AddPatientWindow, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.on_addPatient_confirm)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.on_addPatient_cancel)
    
    def on_addPatient_confirm(self):
        # Get user input from form
        pid = self.pIDLine.text()
        fname = self.pFirstLine.text()
        lname = self.pLastLine.text()
        dob = self.pDOBLine.text()
        province = self.pProvinceBox.currentText()
        phone = self.pPhoneLine.text()
        email = self.pEmailLine.text()
        city = self.pCityLine.text()
        address = self.pAddressLine.text()

        # Check for any blank form entries
        if pid == "" or fname == "" or lname == "" or dob == "" or phone == "" or email == "" or city == "" or address =="":
            QtWidgets.QMessageBox.about(self, "Error", "Please fill out the information fully!")
        else:
            dbManager.addPatient(pid, fname, lname, dob, phone, email, province, city, address)
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

        # Get user input from form
        din = self.dinLine.text()
        name = self.dNameLine.text()
        drugclass = self.dClassLine.text()
        admin = self.dAdminLine.text()
        ingredients = self.dIngredBox.currentText()
        dosage = self.dDosageLine.text()

        # Check for any blank form entries
        if din == "" or name == "" or drugclass == "" or admin == "" or dosage == "":
            QtWidgets.QMessageBox.about(self, "Error", "Please fill out the information fully!")
        else:
            dbManager.addDrug(din, name, drugclass, admin, ingredients, dosage)
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
