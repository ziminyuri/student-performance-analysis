from PyQt5 import QtCore, QtWidgets
from forms.py.add_subject import form_add_subject


class form_subject_list(object):
    def __init__(self, MainWindow):
        self.subject_window = MainWindow.subject_window
        self.subject_window.setObjectName("MainWindow")
        self.subject_window.resize(573, 394)
        self.centralwidget = QtWidgets.QWidget(self.subject_window)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 551, 231))
        self.listWidget.setObjectName("listWidget")
        ls = ["Операционные системы", "Алгоритмы и структуры данных"]
        self.listWidget.addItems(ls)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 280, 121, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_add_subject_window)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 280, 121, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 330, 121, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.close_window)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(391, 10, 171, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 310, 551, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.subject_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.subject_window)
        self.statusbar.setObjectName("statusbar")
        self.subject_window.setStatusBar(self.statusbar)

        self.add_subject_window = QtWidgets.QMainWindow()
        self.add_subject_ui = form_add_subject(self)

        self.retranslateUi(self.subject_window)
        QtCore.QMetaObject.connectSlotsByName(self.subject_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Дисциплины"))
        self.label.setText(_translate("MainWindow", "Диспциплины"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Редактировать"))
        self.pushButton_3.setText(_translate("MainWindow", "Закрыть"))
        self.pushButton_4.setText(_translate("MainWindow", "Показать расписание"))

    def show_add_subject_window(self):
        self.add_subject_window.show()

    def close_window(self):
        self.subject_window.close()
