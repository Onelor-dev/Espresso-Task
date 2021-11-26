import sys

from PyQt5 import uic
from PyQt5.QtSql import *
from PyQt5.QtWidgets import QWidget, QTableView, QApplication
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('Coffee.sqlite')
        db.open()

        view = QTableView(self)
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()

        view.setModel(model)
        view.move(10, 10)
        view.resize(617, 315)

        view.setModel(model)
        self.setWindowTitle('Espresso')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
