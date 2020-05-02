from PyQt5 import QtCore, QtGui, QtWidgets


class FormUpdateGroup(object):
    def __init__(self, main_window):
        self.update_group_window = main_window.update_group_window
        self.update_group_window.setObjectName("MainWindow")
        self.update_group_window.resize(410, 197)
        self.centralwidget = QtWidgets.QWidget(self.update_group_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 131, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 371, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 120, 191, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.update)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 391, 32))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 131, 16))
        self.label_2.setObjectName("label_2")
        self.update_group_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.update_group_window)
        self.statusbar.setObjectName("statusbar")
        self.update_group_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.update_group_window)
        QtCore.QMetaObject.connectSlotsByName(self.update_group_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить группу"))
        self.label.setText(_translate("MainWindow", "Номер группы"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить изменения"))
        self.label_2.setText(_translate("MainWindow", "Специальность"))

    def update(self):
        pass