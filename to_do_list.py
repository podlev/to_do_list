import sys
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem


from db_opertions import add_user, login, load_tasks, load_task_detail


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
        self.tasks_list.itemClicked.connect(self.load_task_detail)

    def load_tasks(self):
        tasks = load_tasks()
        self.tasks_list.clear()
        for task in tasks:
            self.tasks_list.addItem(QListWidgetItem(f'{task[0]} {task[2]}'))

    def load_task_detail(self, item):
        id = item.text().split()[0]
        task = load_task_detail(id)
        print(task)


def main():
    app = QtWidgets.QApplication(sys.argv)
    auth_window = AuthWindow()
    auth_window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
