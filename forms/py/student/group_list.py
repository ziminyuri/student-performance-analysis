from PyQt5 import QtCore, QtGui, QtWidgets
from forms.py.student.add_group import FormAddGroup
from forms.py.student.update_group import FormUpdateGroup
from db.models import Specialty, Group


class FormGroupWindow(object):
    def __init__(self, main_window):
        self.combo = main_window.comboBox
        self.session = main_window.session
        self.group_window = main_window.group_window
        self.group_window.setObjectName("MainWindow")
        self.group_window.setFixedSize(661, 498)
        self.group_window.setStyleSheet("background-color: #1a222c")
        self.centralwidget = QtWidgets.QWidget(self.group_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 360, 151, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; margin:5px; color: #c2cdd9;")
        self.pushButton.clicked.connect(self.show_update_group)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 430, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; margin:5px; color: #c2cdd9;")
        self.pushButton_2.clicked.connect(self.close_window)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 631, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setStyleSheet("color: #c2cdd9; font: 12px;")
        self.tableWidget.horizontalHeader().setStyleSheet("background-color: #344c68; font: 14px;")
        self.tableWidget.verticalHeader().setStyleSheet("background-color: #344c68; font: 14px; ")
        self.tableWidget.setHorizontalHeaderLabels(["Специальность", "Номер группы"])

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 360, 151, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; margin:5px; color: #c2cdd9;")
        self.pushButton_3.clicked.connect(self.show_add_group)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 390, 151, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; margin:5px; color: #c2cdd9;")
        self.pushButton_4.clicked.connect(self.delete)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 420, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.group_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.group_window)
        self.statusbar.setObjectName("statusbar")
        self.group_window.setStatusBar(self.statusbar)

        self.add_group_window = QtWidgets.QMainWindow()
        self.add_group_ui = FormAddGroup(self)

        self.update_group_window = QtWidgets.QMainWindow()
        self.update_group_ui = FormUpdateGroup(self)

        self.retranslateUi(self.group_window)
        QtCore.QMetaObject.connectSlotsByName(self.group_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Группы"))
        self.pushButton.setText(_translate("MainWindow", "Редактировать"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_4.setText(_translate("MainWindow", "Удалить"))

    def close_window(self):
        self.group_window.close()

    def show_add_group(self):
        specialty = Specialty()
        ls_name = specialty.show_name(self.session)
        self.add_group_ui.comboBox.addItems(ls_name)
        self.add_group_window.show()

    def show_update_group(self):
        items = self.tableWidget.selectedItems()

        for i in items:
            row = self.tableWidget.row(i)

            specialty = self.tableWidget.item(row, 0).text()
            number = self.tableWidget.item(row, 1).text()
            self.update_group_ui.lineEdit.setText(number)

            s = Specialty()
            ls_name = s.show_name(self.session)
            self.update_group_ui.comboBox.addItems(ls_name)
            current_index = ls_name.index(specialty)
            self.update_group_ui.comboBox.setCurrentIndex(current_index)

            self.update_group_ui.update_value = number
            self.update_group_ui.row = row

            self.update_group_window.show()
            break

    def delete(self):
        items = self.tableWidget.selectedItems()
        for i in items:
            row = self.tableWidget.row(i)
            number = self.tableWidget.item(row, 1).text()

            group = Group()
            group.delete(self.session, number)

            self.tableWidget.removeRow(row)
            self.combo.clear()
            ls_name = group.show_name(self.session)
            self.combo.addItems(ls_name)
