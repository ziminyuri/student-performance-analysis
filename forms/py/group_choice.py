from PyQt5 import QtCore, QtWidgets
from forms.py.student_list import form_student_list


class form_group_choice(object):
    def __init__(self, MainWindow):
        self.group_choice_window = MainWindow.group_choice_window
        self.group_choice_window.setObjectName("MainWindow")
        self.group_choice_window.resize(510, 187)
        self.centralwidget = QtWidgets.QWidget(self.group_choice_window)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 241, 32))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 120, 121, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close_window)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 50, 221, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.show_student_list)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 20, 221, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 100, 471, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.group_choice_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.group_choice_window)
        self.statusbar.setObjectName("statusbar")
        self.group_choice_window.setStatusBar(self.statusbar)

        self.student_list_window = QtWidgets.QMainWindow()
        self.student_list_ui = form_student_list(self)

        self.retranslateUi(self.group_choice_window)
        QtCore.QMetaObject.connectSlotsByName(self.group_choice_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Выберите группу"))
        self.label.setText(_translate("MainWindow", "Выберите группу"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))
        self.pushButton_3.setText(_translate("MainWindow", "Просмотреть список группы"))
        self.pushButton_4.setText(_translate("MainWindow", "Добавить группу"))

    def show_student_list(self):
        self.student_list_window.show()
        self.group_choice_window.hide()

    def close_window(self):
        self.group_choice_window.close()