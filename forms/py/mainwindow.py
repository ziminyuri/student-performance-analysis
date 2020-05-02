from PyQt5 import QtCore, QtWidgets
from forms.py.login import form_login
from forms.py.choice_analytics import form_choice_analytics_window
from forms.py.subject.subject_list import form_subject_list
from forms.py.student.group_choice import form_group_choice
from forms.py.report import form_report
from forms.py.grades import form_grade
from forms.py.not_submitted_work import form_not_submitted_work
from db.models import Group


class form_mainwindow(object):
    def __init__(self, MainWindow, session):
        self.session = session
        self.main_window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_reports = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reports.setObjectName("pushButton_reports")
        self.pushButton_reports.clicked.connect(self.show_report_window)
        self.gridLayout.addWidget(self.pushButton_reports, 0, 4, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_close.clicked.connect(self.close_window)
        self.gridLayout.addWidget(self.pushButton_close, 0, 5, 1, 1)
        self.pushButton_analytics = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_analytics.setObjectName("pushButton_analytics")
        self.pushButton_analytics.clicked.connect(self.show_choice_analytics_window)
        self.gridLayout.addWidget(self.pushButton_analytics, 0, 3, 1, 1)
        self.pushButton_student = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_student.setObjectName("pushButton_student")
        self.pushButton_student.clicked.connect(self.show_group_choice_window)
        self.gridLayout.addWidget(self.pushButton_student, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["ФИО", "Группа", "Дисциплина", "Процент отставания"])
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Иванов Иван Иванович"))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("123432"))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem("Операционные системы"))
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem("60%"))
        self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("Петров Дмитрий Константинович"))
        self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem("123432"))
        self.tableWidget.setItem(1, 2, QtWidgets.QTableWidgetItem("Операционные системы"))
        self.tableWidget.setItem(1, 3, QtWidgets.QTableWidgetItem("40%"))
        self.tableWidget.resizeColumnsToContents()
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 6)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 6)
        self.pushButton_lesson = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_lesson.setObjectName("pushButton_lesson")
        self.pushButton_lesson.clicked.connect(self.show_subject_window)
        self.gridLayout.addWidget(self.pushButton_lesson, 0, 0, 1, 1)
        self.pushButton_grade = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_grade.setObjectName("pushButton_grade")
        self.pushButton_grade.clicked.connect(self.show_grade_window)
        self.gridLayout.addWidget(self.pushButton_grade, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 2, 1, 4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_not_submitted_work_window)
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Инициализируем окна
        self.login_window = QtWidgets.QMainWindow()
        self.login_ui = form_login(self)

        self.subject_window = QtWidgets.QMainWindow()
        self.subject_ui = form_subject_list(self)

        self.group_choice_window = QtWidgets.QMainWindow()
        self.group_choice_ui = form_group_choice(self)

        self.grade_window = QtWidgets.QMainWindow()
        self.grade_ui = form_grade(self)

        self.choice_analytics_window = QtWidgets.QMainWindow()
        self.choice_analytics_ui = form_choice_analytics_window(self)

        self.report_window = QtWidgets.QMainWindow()
        self.report_ui = form_report(self)

        self.not_submitted_work_window = QtWidgets.QMainWindow()
        self.not_submitted_work_ui = form_not_submitted_work(self)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        self.main_window.show()
        self.show_login_window()
        self.main_window.hide()

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
        self.grade_window.show()

    def show_choice_analytics_window(self):
        self.choice_analytics_window.show()

    def show_report_window(self):
        self.report_window.show()

    def show_not_submitted_work_window(self):
        self.not_submitted_work_window.show()

    def close_window(self):
        self.main_window.close()
