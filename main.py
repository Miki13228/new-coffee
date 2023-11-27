import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QVBoxLayout
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.uic import loadUi


class CoffeeInfoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)

        self.initDB()

        self.loadTableData()

        self.addButton.clicked.connect(self.showAddEditForm)

    def initDB(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')

    def loadTableData(self):
        model = QSqlTableModel()
        model.setTable('coffees')
        model.select()

        self.tableView.setModel(model)

    def showAddEditForm(self):
        form = AddEditCoffeeForm(self)

        if form.exec() == QDialog.DialogCode.Accepted:
            self.loadTableData()


class AddEditCoffeeForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('addEditCoffeeForm.ui', self)

        self.saveButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeInfoApp()
    window.show()
    sys.exit(app.exec())
