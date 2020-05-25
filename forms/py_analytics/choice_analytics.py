from PyQt5 import QtCore, QtGui, QtWidgets
from forms.py.analytics import FormAnalytics
from db.models import Group, Discipline
from forms.py_analytics.choice_group import FormChoiceGroup
from forms.py_analytics.group_analytics import FormGroupAnalytics


class FormChoiceAnalyticsWindow(object):
    def __init__(self, main_window):
        self.session = main_window.session
        self.choice_analytics_window = main_window.choice_analytics_window
        self.choice_analytics_window.setObjectName("MainWindow")
        self.choice_analytics_window.setFixedSize(349, 172)
        self.choice_analytics_window.setStyleSheet(
            "background-color: #1a222c; border-color: #24303f; border-width: 1px;")
        self.centralwidget = QtWidgets.QWidget(self.choice_analytics_window)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 311, 32))
        self.comboBox.setObjectName("comboBox")
        ls = ["Группа", 'Дисциплина', "Студент"]
        self.comboBox.addItems(ls)
        self.comboBox.setStyleSheet(
            "color: #c2cdd9; background-color: #344c68; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; margin:2px; selection-color: white; selection-background-color: #1a222c;")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 171, 16))
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 12px; color: #c2cdd9;")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 100, 112, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; margin:5px; color: #c2cdd9;")
        self.pushButton.clicked.connect(self.choice_analytics)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 100, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; margin:5px; color: #c2cdd9;")
        self.pushButton_2.clicked.connect(self.close_window)
        self.choice_analytics_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.choice_analytics_window)
        self.statusbar.setObjectName("statusbar")
        self.choice_analytics_window.setStatusBar(self.statusbar)

        self.analytics_window = QtWidgets.QMainWindow()
        self.analytics_ui = FormAnalytics(self)

        self.choice_group_window = QtWidgets.QMainWindow()
        self.choice_group_ui = FormChoiceGroup(self)

        self.group_analytics_window = QtWidgets.QMainWindow()
        self.group_analytics_ui = FormGroupAnalytics(self)

        self.retranslateUi(self.choice_analytics_window)
        QtCore.QMetaObject.connectSlotsByName(self.choice_analytics_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Выберите объект анализа"))
        self.label.setText(_translate("MainWindow", "Объект анализа"))
        self.pushButton.setText(_translate("MainWindow", "Далее"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))

    def choice_analytics(self):
        choice = self.comboBox.currentText()

        if choice == 'Студент':
            self.show_student_analytics_window()
        elif choice == 'Дисциплина':
            self.show_analytics_window()
        else:
            self.show_group_analytics_window()

    # Аналитика по дисциплинам
    def show_analytics_window(self):
        group = Group()
        ls_name = group.show_name(self.session)
        self.analytics_ui.comboBox_2.addItems(ls_name)

        discipline = Discipline
        d_name = discipline.show_name(self.session)
        self.analytics_ui.comboBox.addItems(d_name)

        self.analytics_window.show()
        self.choice_analytics_window.hide()

    # Аналитика по группам
    def show_group_analytics_window(self):
        group = Group()
        ls_name = group.show_name(self.session)
        self.group_analytics_ui.comboBox.addItems(ls_name)

        self.choice_analytics_window.hide()
        self.group_analytics_window.show()

    # Аналитика по студенту
    def show_student_analytics_window(self):
        group = Group()
        ls_name = group.show_name(self.session)
        self.choice_group_ui.comboBox.addItems(ls_name)
        self.choice_analytics_window.hide()
        self.choice_group_window.show()

    def close_window(self):
        self.choice_analytics_window.close()