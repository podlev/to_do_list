import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem

from db_opertions import add_user, login, load_tasks, load_task_detail, delete_task, add_task


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

sys.excepthook = except_hook


class AuthWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('registration.ui', self)
        self.reg_button.clicked.connect(self.registration)
        self.auth_button.clicked.connect(self.auth)


    def registration(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        add_user(username, password)
        dialog = QMessageBox()
        dialog.setText('Успешная регистрация')
        dialog.setIcon(1)
        dialog.exec()

    def auth(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        if login(username, password):
            self.tasks_window = TasksWindow()
            self.tasks_window.show()
            self.hide()
        else:
            dialog = QMessageBox()
            dialog.setText('Вход не выполнен')
            dialog.setIcon(3)
            dialog.exec()


class TasksWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('tasks.ui', self)
        self.load_tasks_button.clicked.connect(self.load_tasks)
        self.delete_task_button.clicked.connect(self.delete_task)
        self.add_task_button.clicked.connect(self.add_task)
        self.tasks_list.itemClicked.connect(self.load_task_detail)


    def load_tasks(self):
        self.tasks = load_tasks()
        self.tasks_list.clear()
        for task in self.tasks:
            self.tasks_list.addItem(QListWidgetItem(task[2]))

    def load_task_detail(self):
        id = self.tasks[self.tasks_list.currentRow()][0]
        task = load_task_detail(id)
        self.task_title.setText(task[2])
        self.task_description.setText(task[3])

    def delete_task(self):
        id = self.tasks[self.tasks_list.currentRow()][0]
        delete_task(id)
        self.load_tasks()
        self.task_title.setText('')
        self.task_description.setText('')

    def add_task(self):
        title = self.task_title.text()
        description = self.task_description.toPlainText()
        add_task(1, title, description)
        self.load_tasks()
        self.task_title.setText('')
        self.task_description.setText('')

def main():
    app = QtWidgets.QApplication(sys.argv)
    auth_window = AuthWindow()
    auth_window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
