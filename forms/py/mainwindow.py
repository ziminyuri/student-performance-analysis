from PyQt5 import QtCore, QtWidgets
from forms.py.login import FormLogin
from forms.py_analytics.choice_analytics import FormChoiceAnalyticsWindow
from forms.py.subject.subject_list import FormSubjectList
from forms.py.student.group_choice import FormGroupChoice
from forms.py.report import FormReport
from forms.py.grade.grades import FormGrade
from forms.py.not_submitted_work import form_not_submitted_work
from db.models import Group, Discipline, Grade
import numpy as np
from transform.items import set_items_to_table


class FormMainwindow(object):
    def __init__(self, main_window, session):
        self.session = session
        self.main_window = main_window
        self.main_window.setObjectName("MainWindow")
        self.main_window.setFixedSize(1120, 800)
        self.main_window.setStyleSheet("background-color: #1a222c; border-color: #24303f; border-width: 1px;")
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_reports = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reports.setObjectName("pushButton_reports")
        self.pushButton_reports.clicked.connect(self.show_report_window)
        self.pushButton_reports.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; min-width: 10em; padding: 6px; margin:5px; color: #c2cdd9;")
        self.gridLayout.addWidget(self.pushButton_reports, 0, 4, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_close.clicked.connect(self.close_window)
        self.pushButton_close.setStyleSheet("background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; min-width: 10em; padding: 6px; margin:5px; color: #c2cdd9;")
        self.gridLayout.addWidget(self.pushButton_close, 0, 5, 1, 1)
        self.pushButton_analytics = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_analytics.setObjectName("pushButton_analytics")
        self.pushButton_analytics.clicked.connect(self.show_choice_analytics_window)
        self.pushButton_analytics.setStyleSheet("background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; min-width: 10em; padding: 6px; margin:5px; color: #c2cdd9;")
        self.gridLayout.addWidget(self.pushButton_analytics, 0, 3, 1, 1)
        self.pushButton_student = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_student.setObjectName("pushButton_student")
        self.pushButton_student.clicked.connect(self.show_group_choice_window)
        self.pushButton_student.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; min-width: 10em; padding: 6px; margin:5px; color: #c2cdd9;")
        self.gridLayout.addWidget(self.pushButton_student, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setStyleSheet("color: #c2cdd9; font: 12px;")
        self.tableWidget.horizontalHeader().setStyleSheet("background-color: #344c68; font: 14px;")
        self.tableWidget.verticalHeader().setStyleSheet("background-color: #344c68; font: 14px; ")
        self.tableWidget.resizeColumnsToContents()
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 6)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line.setStyleSheet('background-color: #24303f;')
        self.gridLayout.addWidget(self.line, 1, 0, 1, 6)
        self.pushButton_lesson = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_lesson.setObjectName("pushButton_lesson")
        self.pushButton_lesson.clicked.connect(self.show_subject_window)
        self.pushButton_lesson.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; min-width: 10em; padding: 6px; margin:5px; color: #c2cdd9;")
        self.gridLayout.addWidget(self.pushButton_lesson, 0, 0, 1, 1)
        self.pushButton_grade = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_grade.setObjectName("pushButton_grade")
        self.pushButton_grade.clicked.connect(self.show_grade_window)
        self.pushButton_grade.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; min-width: 10em; padding: 6px; margin:5px; color: #c2cdd9;")
        self.gridLayout.addWidget(self.pushButton_grade, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 12px; color: #c2cdd9;")
        self.gridLayout.addWidget(self.label, 2, 2, 1, 4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_not_submitted_work_window)
        self.pushButton.hide()
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.main_window)
        self.statusbar.setObjectName("statusbar")
        self.main_window.setStatusBar(self.statusbar)

        # Инициализируем окна
        self.login_window = QtWidgets.QMainWindow()
        self.login_ui = FormLogin(self)

        self.subject_window = QtWidgets.QMainWindow()
        self.subject_ui = FormSubjectList(self)

        self.group_choice_window = QtWidgets.QMainWindow()
        self.group_choice_ui = FormGroupChoice(self)

        self.grade_window = QtWidgets.QMainWindow()
        self.grade_ui = FormGrade(self)

        self.choice_analytics_window = QtWidgets.QMainWindow()
        self.choice_analytics_ui = FormChoiceAnalyticsWindow(self)

        self.report_window = QtWidgets.QMainWindow()
        self.report_ui = FormReport(self)

        self.not_submitted_work_window = QtWidgets.QMainWindow()
        self.not_submitted_work_ui = form_not_submitted_work(self)

        self.retranslateUi(self.main_window)
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Личный кабинет"))
        self.pushButton_reports.setText(_translate("MainWindow", "Отчеты"))
        self.pushButton_close.setText(_translate("MainWindow", "Выход"))
        self.pushButton_analytics.setText(_translate("MainWindow", "Аналитика"))
        self.pushButton_student.setText(_translate("MainWindow", "Студенты"))
        self.pushButton_lesson.setText(_translate("MainWindow", "Дисциплины"))
        self.pushButton_grade.setText(_translate("MainWindow", "Оценки"))
        self.label.setText(_translate("MainWindow", "Отстающие студенты"))
        self.pushButton.setText(_translate("MainWindow", "Список не сданных работ студента"))

    def show(self):
        grade = Grade()
        result = grade.lagging_students(self.session)
        self.tableWidget = set_items_to_table(self.tableWidget, result)
        self.tableWidget.setHorizontalHeaderLabels(["ФИО", "Группа", "Дисциплина", "Список не сданных работ"])
        self.tableWidget.resizeColumnsToContents()
        self.main_window.show()

    def show_login_window(self):
        self.login_window.show()

    def show_subject_window(self):
        self.subject_window.show()

    def show_group_choice_window(self):
        group = Group()
        ls_name = group.show_name(self.session)
        self.group_choice_ui.comboBox.addItems(ls_name)
        self.group_choice_window.show()

    def show_grade_window(self):
        group = Group()
        ls_name = group.show_name(self.session)
        self.grade_ui.comboBox_2.clear()
        self.grade_ui.comboBox_2.addItems(ls_name)

        discipline = Discipline
        d_name = discipline.show_name(self.session)
        self.grade_ui.comboBox.clear()
        self.grade_ui.comboBox.addItems(d_name)

        self.grade_window.show()

    def show_choice_analytics_window(self):
        self.choice_analytics_window.show()

    def show_report_window(self):
        self.report_window.show()

    def show_not_submitted_work_window(self):
        self.not_submitted_work_window.show()

    def close_window(self):
        self.main_window.close()
