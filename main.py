import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem

from db_opertions import load_tasks, load_task_detail


def except_hook(cls, exception, traceback):
    """
    Printing the traceback to stdout/stderr.
    """
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('to_do_list.ui', self)
        self.add_task_button.clicked.connect(self.add_task)
        self.delete_task_button.clicked.connect(self.delete_task)
        self.load_tasks()
        self.tableWidget.clicked.connect(self.task_detail)

    def load_tasks(self):
        tasks = load_tasks()
        print(tasks)
        if tasks is not None:
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setRowCount(len(tasks))
            self.tableWidget.setHorizontalHeaderLabels(('№', 'Автор', 'Название', 'Описание', 'Дата'))
            self.tableWidget.setVerticalHeaderLabels([str(i) for i in range(1, len(tasks) + 1)])
            for i, row in enumerate(tasks):
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
            self.tableWidget.resizeColumnsToContents()

    def task_detail(self, item):
        task_id = self.tableWidget.model().index(item.row(), 0).data()
        task = load_task_detail(task_id)
        self.task_name.setText(task[2])
        self.task_description.setText(task[3])

    def add_task(self):
        pass

    def delete_task(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
