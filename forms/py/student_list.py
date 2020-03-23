from PyQt5 import QtCore, QtWidgets



class form_student_list(object):
    def __init__(self, MainWindow):
        self.student_window = MainWindow.student_list_window
        self.student_window.setObjectName("MainWindow")
        self.student_window.resize(676, 530)
        self.centralwidget = QtWidgets.QWidget(self.student_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 241, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 390, 141, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 460, 141, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close_window)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 30, 641, 321))
        self.listWidget.setObjectName("listWidget")
        ls = ["Антонов Варлам Парфеньевич",
              "Гусев Гаянэ Ростиславович",
              "Иванов Оскар Иосифович",
              "Лыткин Герман Олегович",
              "Носов Мечислав Яковович",
              "Силин Тарас Якунович",
              "Ширяев Яков Филиппович"
              ]
        self.listWidget.addItems(ls)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 360, 141, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 440, 641, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 360, 141, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 390, 141, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.student_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.student_window)
        self.statusbar.setObjectName("statusbar")
        self.student_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.student_window)
        QtCore.QMetaObject.connectSlotsByName(self.student_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список группы"))
        self.label.setText(_translate("MainWindow", "Список группы"))
        self.pushButton.setText(_translate("MainWindow", "Редактировать"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_4.setText(_translate("MainWindow", "Импорт из .csv"))
        self.pushButton_5.setText(_translate("MainWindow", "Импорт из Moodle"))

    def close_window(self):
        self.student_window.close()
