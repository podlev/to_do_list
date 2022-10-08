import sys
from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QPushButton


def except_hook(cls, exception, traceback):
    """
    Printing the traceback to stdout/stderr.
    """
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 440, 500)
        self.tableView = QTableView(self)
        self.tableView.resize(400, 400)
        self.tableView.move(20, 20)
        self.pushButton = QPushButton('Кнопка', self)
        self.pushButton.move(20, 440)
        self.pushButton.clicked.connect(self.load_tasks)
        self.show()


    def load_tasks(self):
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
