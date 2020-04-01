from PyQt5 import QtWidgets
from forms.py.mainwindow_2 import form_mainwindow
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    f = form_mainwindow(main_window)
    f.show()
    # main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()