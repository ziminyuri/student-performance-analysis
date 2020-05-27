from PyQt5 import QtCore, QtGui, QtWidgets


class FormChoiceDisciplineGroup(object):
    def __init__(self, main_window):
        self.discipline = ""
        self.session = main_window.session
        self.choice_discipline_group_or_student_window = main_window.choice_discipline_group_or_student_window
        self.choice_discipline_group_window = main_window.choice_discipline_group_window
        self.choice_discipline_group_window.setObjectName("MainWindow")
        self.choice_discipline_group_window.setFixedSize(417, 194)
        self.centralwidget = QtWidgets.QWidget(self.choice_discipline_group_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 120, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.previous_page)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 120, 121, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.analysis)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 80, 391, 32))
        self.comboBox_2.setObjectName("comboBox_2")
        ls = ['Средняя оценка по итогам сессии', 'Средняя оценка за работы в семестре',
                'Максимальная оценка по итогам сессии', 'Максимальная оценка по итогам работы в семестре',
                'Минимальная оценка по итогам сессии', 'Минимальная оценка по итогам работы в семестре',
                'Количество сданных работ в семестре']
        self.comboBox_2.clear()
        self.comboBox_2.addItems(ls)
        self.choice_discipline_group_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.choice_discipline_group_window)
        self.statusbar.setObjectName("statusbar")
        self.choice_discipline_group_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.choice_discipline_group_window)
        QtCore.QMetaObject.connectSlotsByName(self.choice_discipline_group_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Аналитика"))
        self.pushButton_2.setText(_translate("MainWindow", "Назад"))
        self.pushButton_3.setText(_translate("MainWindow", "Далее"))
        self.label_2.setText(_translate("MainWindow", "Тип анализа"))

    def previous_page(self):
        self.choice_discipline_group_window.hide()
        self.choice_discipline_group_or_student_window.show()

    def analysis(self):
        pass