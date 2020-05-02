from PyQt5 import QtCore, QtGui, QtWidgets
from forms.py.student.add_group import FormAddGroup
from forms.py.student.update_group import FormUpdateGroup
from db.models import Specialty


class form_group_window(object):
    def __init__(self, MainWindow):
        self.combo = MainWindow.comboBox
        self.session = MainWindow.session
        self.group_window = MainWindow.group_window
        self.group_window.setObjectName("MainWindow")
        self.group_window.resize(661, 498)
        self.centralwidget = QtWidgets.QWidget(self.group_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 360, 151, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_update_group)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 430, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close_window)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 631, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Специальность", "Номер группы"])

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 360, 151, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.show_add_group)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 390, 151, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 420, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.group_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.group_window)
        self.statusbar.setObjectName("statusbar")
        self.group_window.setStatusBar(self.statusbar)

        self.add_group_window = QtWidgets.QMainWindow()
        self.add_group_ui = FormAddGroup(self)

        self.update_group_window = QtWidgets.QMainWindow()
        self.update_group_ui = FormUpdateGroup(self)

        self.retranslateUi(self.group_window)
        QtCore.QMetaObject.connectSlotsByName(self.group_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Группы"))
        self.pushButton.setText(_translate("MainWindow", "Редактировать"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_4.setText(_translate("MainWindow", "Удалить"))

    def close_window(self):
        self.group_window.close()

    def show_add_group(self):
        specialty = Specialty()
        ls_name = specialty.show_name(self.session)
        self.add_group_ui.comboBox.addItems(ls_name)
        self.add_group_window.show()

    def show_update_group(self):
        self.update_group_window.show()
