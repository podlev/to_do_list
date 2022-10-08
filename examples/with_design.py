import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QTableView


def except_hook(cls, exception, traceback):
    """
    Printing the traceback to stdout/stderr.
    """
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.pushButton.clicked.connect(self.click)

    def click(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('to_do_list.sqlite')
        db.open()
        model = QSqlTableModel()
        model.setTable("tasks")
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.select()
        self.tableView.setModel(model)
        self.tableView.resizeColumnsToContents()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
