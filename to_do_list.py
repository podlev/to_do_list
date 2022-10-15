import sys
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QMessageBox

from db_opertions import add_user, login


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
            dialog = QMessageBox()
            dialog.setText('Вход выполнен')
            dialog.setIcon(1)
            dialog.exec()
        else:
            dialog = QMessageBox()
            dialog.setText('Вход не выполнен')
            dialog.setIcon(3)
            dialog.exec()

def main():
    app = QtWidgets.QApplication(sys.argv)
    auth_window = AuthWindow()
    auth_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
