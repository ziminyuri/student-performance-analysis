from PyQt5 import QtCore, QtWidgets


class form_add_group(object):
    def __init__(self, MainWindow):
        self.add_group_window = MainWindow.add_group_window
        self.add_group_window.setObjectName("MainWindow")
        self.add_group_window.resize(338, 125)
        self.centralwidget = QtWidgets.QWidget(self.add_group_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 311, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 60, 112, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_group)
        self.add_group_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.add_group_window)
        self.statusbar.setObjectName("statusbar")
        self.add_group_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.add_group_window)
        QtCore.QMetaObject.connectSlotsByName(self.add_group_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить группу"))
        self.label.setText(_translate("MainWindow", "Номер группы"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))

    def add_group(self):
        self.add_group_window.close()