from PyQt5 import QtCore, QtGui, QtWidgets
from db.models import Discipline
from transform.query import query_to_list_of_name


class FormSubjectList(object):
    def __init__(self, main_window):
        self.session = main_window.session
        self.subject_window = main_window.subject_window
        self.subject_window.setObjectName("MainWindow")
        self.subject_window.setFixedSize(573, 314)
        self.subject_window.setStyleSheet("background-color: #1a222c")
        self.centralwidget = QtWidgets.QWidget(self.subject_window)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 551, 231))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setEditTriggers(QtWidgets.QListWidget.NoEditTriggers)
        self.listWidget.setStyleSheet("color: #c2cdd9; font: 12px;")

        discipline = Discipline()
        query_list = discipline.all(self.session)
        ls = query_to_list_of_name(query_list)
        self.listWidget.addItems(ls)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 12px; color: #c2cdd9;")
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
