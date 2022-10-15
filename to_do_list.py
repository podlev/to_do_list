import sys
from PyQt5 import QtWidgets, uic


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook


class AuthWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('registration.ui', self)
        # self.pushButton.clicked.connect(self.click)

    def click(self):
        print(1)


def main():
    app = QtWidgets.QApplication(sys.argv)
    auth_window = AuthWindow()
    auth_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
