from PyQt5 import QtWidgets
from forms.py.mainwindow import form_mainwindow
import sys

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from connecting import my_databases

engine = create_engine(my_databases, pool_size=10, max_overflow=20)

Session = sessionmaker(bind=engine)

Base = declarative_base()


def main():
    app = QtWidgets.QApplication(sys.argv)

    session = Session()

    main_window = QtWidgets.QMainWindow()
    f = form_mainwindow(main_window, session)
    f.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()