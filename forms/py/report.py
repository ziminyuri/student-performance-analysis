from PyQt5 import QtCore, QtWidgets


class form_report(object):
    def __init__(self, MainWindow):
        self.report_window = MainWindow.report_window
        self.report_window.setObjectName("MainWindow")
        self.report_window.resize(581, 159)
        self.centralwidget = QtWidgets.QWidget(self.report_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 30, 551, 32))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 90, 181, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 90, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close_window)
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
        self.pushButton.setText(_translate("MainWindow", "Сохранить в .docx"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))

    def close_window(self):
        self.report_window.close()