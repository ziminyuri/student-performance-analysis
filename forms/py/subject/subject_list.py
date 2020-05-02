from PyQt5 import QtCore, QtGui, QtWidgets
from db.models import Discipline
from transform.query import query_to_list_of_name


class form_subject_list(object):
    def __init__(self, MainWindow):
        self.session = MainWindow.session
        self.subject_window = MainWindow.subject_window
        self.subject_window.setObjectName("MainWindow")
        self.subject_window.resize(573, 314)
        self.centralwidget = QtWidgets.QWidget(self.subject_window)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 551, 231))
        self.listWidget.setObjectName("listWidget")

        discipline = Discipline()
        query_list = discipline.all(self.session)
        ls = query_to_list_of_name(query_list)

        # ls = ["Операционные системы", "Алгоритмы и структуры данных"]
        self.listWidget.addItems(ls)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label.setObjectName("label")
        self.subject_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.subject_window)
        self.statusbar.setObjectName("statusbar")
        self.subject_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.subject_window)
        QtCore.QMetaObject.connectSlotsByName(self.subject_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Дисциплины"))
        self.label.setText(_translate("MainWindow", "Диспциплины"))
