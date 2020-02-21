import sys
from PyQt5 import QtSql, QtCore

# Create a connection to the database and insert elements
def createConnection():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("db/medical.db")
    db.open()

    if not db.open():
        print("Unable to establish a database connection.")
        return False

    query = QtSql.QSqlQuery()
    query.exec_("CREATE TABLE IF NOT EXISTS patients(id int primary key, firstname VARCHAR(20), lastname VARCHAR(20), dob VARCHAR(10), phone VARCHAR(14), email TEXT, province TEXT, city TEXT, address TEXT)")
    query.exec_("INSERT INTO patients VALUES(101, 'Roger', 'Federer', '1982/03/15', '(613) 869-1234', 'rogerfederer@gmail.com', 'Ontario', 'Ottawa', '789 Twist Way')")
    query.exec_("INSERT INTO patients VALUES(102, 'Christiano', 'Ronaldo', '1985/09/23', '(613) 346-3456', 'cr7@hotmail.com', 'Alberta', 'Edmonton', '842 Maloja Way')")
    query.exec_("INSERT INTO patients VALUES(103, 'Usain', 'Bolt', '1990/01/04', '(613) 876-4782', 'thebolt@gmail.com', 'British Columbia', 'Vancouver', '14 Sterling Close')")
    query.exec_("INSERT INTO patients VALUES(104, 'Michael', 'Scott', '1978/06/28', '(613) 757-1432', 'dundermifflin@gmail.com', 'Ontario', 'Scranton', '111 Scranton Way')")
    query.exec_("INSERT INTO patients VALUES(105, 'Conor', 'McGregor', '1987/11/23', '(613) 205-9362', 'notorious@hotmail.com', 'Newfoundland', 'Labrador', '287 Shamrock Street')")

    db.close()
    exit()

# Update the tableview with the database table
def updatePatientsView(tableView):
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("db/medical.db")
    db.open()

    model = QtSql.QSqlTableModel()
    model.setTable("patients")
    model.select()
    tableView.setModel(model)

    db.close()

def updateDrugsView(tableView):
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("db/medical.db")
    db.open()

    model = QtSql.QSqlTableModel()
    model.setTable("drugs")
    model.select()
    tableView.setModel(model)

    db.close()

def removePatient(id):
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("db/medical.db")
    db.open()

    query = QtSql.QSqlQuery()
    query.prepare("DELETE FROM patients WHERE id = ?")
    query.addBindValue(id)
    query.exec()

    db.close()

def removeDrug(din):
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("db/medical.db")
    db.open()

    query = QtSql.QSqlQuery()
    query.prepare("DELETE FROM drugs WHERE DIN = ?")
    query.addBindValue(din)
    query.exec()

    db.close()

def addDrug(din, name, drugclass, admin, ingredients, dosage):
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("db/medical.db")
    db.open()

    query = QtSql.QSqlQuery()
    query.prepare("INSERT INTO drugs VALUES(?,?,?,?,?,?)")
    query.addBindValue(din)
    query.addBindValue(name)
    query.addBindValue(drugclass)
    query.addBindValue(admin)
    query.addBindValue(ingredients)
    query.addBindValue(dosage)
    query.exec()

    db.close()

def addPatient(pid, fname, lname, dob, phone, province, email, city, address):
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("db/medical.db")
    db.open()

    query = QtSql.QSqlQuery()
    query.prepare("INSERT INTO patients VALUES(?,?,?,?,?,?,?,?,?)")
    query.addBindValue(pid)
    query.addBindValue(fname)
    query.addBindValue(lname)
    query.addBindValue(dob)
    query.addBindValue(phone)
    query.addBindValue(province)
    query.addBindValue(email)
    query.addBindValue(city)
    query.addBindValue(address)
    query.exec()

    db.close()


if __name__ == "__main__":
    app = QtCore.QCoreApplication(sys.argv)
    createConnection()
    sys.exit(app.exec_())

