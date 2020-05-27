from PyQt5 import QtCore, QtGui, QtWidgets
from forms.py_analytics.choice_discipline_group_or_student import FormChoiceDisciplineGroupOrStudent


class FormChoiceDiscipline(object):
    def __init__(self, main_window):
        self.choice_analytics_window = main_window.choice_analytics_window
        self.session = main_window.session
        self.choice_discipline_window = main_window.choice_discipline_window
        self.choice_discipline_window.setObjectName("MainWindow")
        self.choice_discipline_window.setFixedSize(417, 145)
        self.centralwidget = QtWidgets.QWidget(self.choice_discipline_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 80, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.previous_page)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 80, 121, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.next_page)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 181, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 381, 32))
        self.comboBox.setObjectName("comboBox")
        self.choice_discipline_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.choice_discipline_window)
        self.statusbar.setObjectName("statusbar")
        self.choice_discipline_window.setStatusBar(self.statusbar)

        self.choice_discipline_group_or_student_window = QtWidgets.QMainWindow()
        self.choice_discipline_group_or_student_ui = FormChoiceDisciplineGroupOrStudent(self)

        self.retranslateUi(self.choice_discipline_window)
        QtCore.QMetaObject.connectSlotsByName(self.choice_discipline_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Аналитика"))
        self.pushButton_2.setText(_translate("MainWindow", "Назад"))
        self.pushButton_3.setText(_translate("MainWindow", "Далее"))
        self.label.setText(_translate("MainWindow", "Дисципилина"))

    def previous_page(self):
        self.choice_discipline_window.hide()
        self.choice_analytics_window.show()

    def next_page(self):
        discipline = self.comboBox.currentText()
        self.choice_discipline_group_or_student_ui.discipline = discipline
        self.choice_discipline_group_or_student_window.show()
        self.choice_discipline_window.hide()