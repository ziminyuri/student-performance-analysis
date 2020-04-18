from PyQt5 import QtCore, QtGui, QtWidgets
from forms.py.analytics import form_analytics


class form_choice_analytics_window(object):
    def __init__(self, MainWindow):
        self.choice_analytics_window = MainWindow.choice_analytics_window
        self.choice_analytics_window.setObjectName("MainWindow")
        self.choice_analytics_window.resize(349, 172)
        self.centralwidget = QtWidgets.QWidget(self.choice_analytics_window)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 311, 32))
        self.comboBox.setObjectName("comboBox")
        ls = ["Группа", "Студент"]
        self.comboBox.addItems(ls)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 171, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 100, 112, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_analytics_window)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 100, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.choice_analytics_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.choice_analytics_window)
        self.statusbar.setObjectName("statusbar")
        self.choice_analytics_window.setStatusBar(self.statusbar)

        self.analytics_window = QtWidgets.QMainWindow()
        self.analytics_ui = form_analytics(self)

        self.retranslateUi(self.choice_analytics_window)
        QtCore.QMetaObject.connectSlotsByName(self.choice_analytics_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Выберите объект анализа"))
        self.label.setText(_translate("MainWindow", "Объект анализа"))
        self.pushButton.setText(_translate("MainWindow", "Далее"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))

    def show_analytics_window(self):
        self.analytics_window.show()
        self.choice_analytics_window.hide()
