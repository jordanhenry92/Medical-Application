from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QApplication, QMainWindow
import mainWindow, addPatient
import sys

class MainWindow(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.addPatientButton.clicked.connect(self.on_addPatient_clicked)
        
    def on_addPatient_clicked(self):
        self.w = AddPatientWindow()
        self.w.show()
        #self.hide()
    
    
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

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
