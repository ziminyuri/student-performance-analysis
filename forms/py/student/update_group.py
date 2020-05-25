from PyQt5 import QtCore, QtGui, QtWidgets
from db.models import Group


class FormUpdateGroup(object):
    def __init__(self, main_window):
        self.session = main_window.session
        self.row: int = 0
        self.update_value: str = ''
        self.table = main_window.tableWidget
        self.update_group_window = main_window.update_group_window
        self.update_group_window.setObjectName("MainWindow")
        self.update_group_window.setFixedSize(410, 197)
        self.update_group_window.setStyleSheet("background-color: #1a222c")
        self.centralwidget = QtWidgets.QWidget(self.update_group_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 131, 16))
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 12px; color: #c2cdd9;")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 371, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet(
            "color: #c2cdd9; background-color: #344c68; border-width: 1px; border-radius: 10px; border-color: #24303f;")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 120, 191, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; margin:5px; color: #c2cdd9;")
        self.pushButton.clicked.connect(self.update)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 391, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet(
            "color: #c2cdd9; background-color: #344c68; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; selection-color: white; selection-background-color: #1a222c;")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("font: 12px; color: #c2cdd9;")
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
        number = self.lineEdit.text()
        specialty: str = self.comboBox.currentText()

        group = Group()
        group.update(self.session, self.update_value, number, specialty)

        self.table.setItem(self.row, 0, QtWidgets.QTableWidgetItem(specialty))
        self.table.setItem(self.row, 1, QtWidgets.QTableWidgetItem(number))

        self.update_group_window.close()