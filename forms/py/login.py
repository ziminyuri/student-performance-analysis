from PyQt5 import QtCore, QtWidgets


class form_login(object):
    def __init__(self, MainWindow):
        self.login_window = MainWindow.login_window
        self.main_window = MainWindow.main_window
        self.login_window.setObjectName("Личный кабинет преподавателя")
        self.login_window.resize(431, 342)
        self.centralwidget = QtWidgets.QWidget(self.login_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 240, 112, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.auth)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 100, 241, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 180, 241, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 70, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 58, 16))
        self.label_2.setObjectName("label_2")
        self.login_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.login_window)
        self.statusbar.setObjectName("statusbar")
        self.login_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.login_window)
        QtCore.QMetaObject.connectSlotsByName(self.login_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Авторизация"))
        self.pushButton.setText(_translate("MainWindow", "Войти"))
        self.label.setText(_translate("MainWindow", "Имя пользователя"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))

    def auth(self):
        self.main_window.show()
        self.login_window.hide()


