from PyQt5 import QtCore, QtGui, QtWidgets


class FormReport(object):
    def __init__(self, main_window):
        self.report_window = main_window.report_window
        self.report_window.setObjectName("MainWindow")
        self.report_window.resize(581, 188)
        self.centralwidget = QtWidgets.QWidget(self.report_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 30, 551, 32))
        self.comboBox.setObjectName("comboBox")
        ls = ['Оценки | Группа №342342',
              'Количество сданных лабораторных точек | Группа №342342']
        self.comboBox.addItems(ls)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 90, 171, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 120, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close_window)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 60, 171, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.report_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.report_window)
        self.statusbar.setObjectName("statusbar")
        self.report_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.report_window)
        QtCore.QMetaObject.connectSlotsByName(self.report_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сохранить отчет"))
        self.label.setText(_translate("MainWindow", "Выберите отчет"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить отчет"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))
        self.pushButton_3.setText(_translate("MainWindow", "Показать отчет"))

    def close_window(self):
        self.report_window.close()