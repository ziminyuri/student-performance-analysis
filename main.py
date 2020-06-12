import sys

from PyQt5 import QtWidgets
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

from connecting import my_databases
from forms.py.mainwindow import FormMainwindow

# engine = create_engine(my_databases, pool_size=10, max_overflow=20)
engine = create_engine(my_databases)

Session = sessionmaker(bind=engine)

Base = declarative_base()


def main():
    app = QtWidgets.QApplication(sys.argv)

    session = Session()

    main_window = QtWidgets.QMainWindow()
    main_window_ui = FormMainwindow(main_window, session)
    main_window_ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
