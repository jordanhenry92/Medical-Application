import sys
from PyQt5 import QtSql, QtCore
import mainWindow

# Create a connection to the database and insert elements
def createConnection():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("db/medical.db")
    db.open()

    if not db.open():
        print("Unable to establish a database connection.")
        return False

    query = QtSql.QSqlQuery()
    query.exec_("create table if not exists sportsmen(id int primary key, firstname varchar(20), lastname varchar(20))")
    query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
    query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
    query.exec_("insert into sportsmen values(103, 'Usain', 'Bolt')")
    query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
    query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")

    db.close()

# Update the tableview with the database table
def updateView(tableView):
    
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("db/medical.db")
    db.open()

    model = QtSql.QSqlTableModel()
    model.setTable("sportsmen")
    model.select()

    tableView.setModel(model)

    db.close()


if __name__ == "__main__":
    app = QtCore.QCoreApplication(sys.argv)
    createConnection()
    sys.exit(app.exec_())

