from PyQt5 import QtCore, QtGui, QtWidgets
from forms.py_analytics.choice_discipline_student import FormChoiceDisciplineStudent
from db.models import Student


class FormChoiceDisciplineStudentGroup(object):
    def __init__(self, main_window):
        self.discipline = ""
        self.session = main_window.session
        self.choice_discipline_group_or_student_window = main_window.choice_discipline_group_or_student_window
        self.choice_discipline_student_group_window = main_window.choice_discipline_student_group_window
        self.choice_discipline_student_group_window.setObjectName("MainWindow")
        self.choice_discipline_student_group_window.setFixedSize(417, 145)
        self.centralwidget = QtWidgets.QWidget(self.choice_discipline_student_group_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 80, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.previous_page)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 80, 121, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.next_page)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 381, 32))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 130, 16))
        self.label.setObjectName("label")
        self.choice_discipline_student_group_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.choice_discipline_student_group_window)
        self.statusbar.setObjectName("statusbar")
        self.choice_discipline_student_group_window.setStatusBar(self.statusbar)

        self.choice_discipline_student_window = QtWidgets.QMainWindow()
        self.choice_discipline_student_ui = FormChoiceDisciplineStudent(self)

        self.retranslateUi(self.choice_discipline_student_group_window)
        QtCore.QMetaObject.connectSlotsByName(self.choice_discipline_student_group_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Аналитика"))
        self.pushButton_2.setText(_translate("MainWindow", "Назад"))
        self.pushButton_3.setText(_translate("MainWindow", "Далее"))
        self.label.setText(_translate("MainWindow", "Группа студента"))

    def previous_page(self):
        self.choice_discipline_student_group_window.hide()
        self.choice_discipline_group_or_student_window.show()

    def next_page(self):
        group_number = self.comboBox.currentText()
        student = Student()
        student_name = student.all_name(self.session, group_number)
        self.choice_discipline_student_ui.comboBox.clear()
        self.choice_discipline_student_ui.comboBox.addItems(student_name)
        self.choice_discipline_student_ui.group_number = group_number
        self.choice_discipline_student_ui.discipline = self.discipline
        self.choice_discipline_student_window.show()
        self.choice_discipline_student_group_window.hide()