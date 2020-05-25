from PyQt5 import QtCore, QtGui, QtWidgets
from db.models import Student


class FormUpdateStudent(object):
    def __init__(self, main_window):
        self.session = main_window.session
        self.table = main_window.tableWidget

        self.update_value: str = ''
        self.row: int = 0

        self.update_student_window = main_window.update_student_window
        self.update_student_window.setObjectName("MainWindow")
        self.update_student_window.setFixedSize(405, 238)
        self.update_student_window.setStyleSheet("background-color: #1a222c")
        self.centralwidget = QtWidgets.QWidget(self.update_student_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 58, 16))
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 12px; color: #c2cdd9;")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 361, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet(
            "color: #c2cdd9; background-color: #344c68; border-width: 1px; border-radius: 10px; border-color: #24303f;")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 171, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("font: 12px; color: #c2cdd9;")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 100, 361, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet(
            "color: #c2cdd9; background-color: #344c68; border-width: 1px; border-radius: 10px; border-color: #24303f;")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 160, 112, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; margin:5px; color: #c2cdd9;")
        self.pushButton.clicked.connect(self.update)
        self.update_student_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.update_student_window)
        self.statusbar.setObjectName("statusbar")
        self.update_student_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.update_student_window)
        QtCore.QMetaObject.connectSlotsByName(self.update_student_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Обновить сведения  о студенте"))
        self.label.setText(_translate("MainWindow", "ФИО "))
        self.label_2.setText(_translate("MainWindow", "Номер зачетной книжки"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))

    def update(self):
        name = self.lineEdit.text()
        record_book = self.lineEdit_2.text()

        student = Student()
        student.update(self.session, self.update_value, name, record_book)

        self.table.setItem(self.row, 0, QtWidgets.QTableWidgetItem(name))
        self.table.setItem(self.row, 1, QtWidgets.QTableWidgetItem(record_book))

        self.update_student_window.close()