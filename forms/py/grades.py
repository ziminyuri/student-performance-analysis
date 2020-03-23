from PyQt5 import QtCore, QtWidgets
from forms.py.teacher_journal import form_teacher_journal


class form_grade(object):
    def __init__(self, MainWindow):
        self.grade_window = MainWindow.grade_window
        self.grade_window.setObjectName("MainWindow")
        self.grade_window.resize(458, 158)
        self.centralwidget = QtWidgets.QWidget(self.grade_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_teacher_journal_window)
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        ls = ['Алгоритмы и сруктуры данных', 'Операционные системы']
        self.comboBox.addItems(ls)
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close_window)
        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        ls_2 = ['324234', '423234']
        self.comboBox_2.addItems(ls_2)
        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.grade_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.grade_window)
        self.statusbar.setObjectName("statusbar")
        self.grade_window.setStatusBar(self.statusbar)

        self.teacher_journal_window = QtWidgets.QMainWindow()
        self.teacher_journal_window_ui = form_teacher_journal(self)

        self.retranslateUi(self.grade_window)
        QtCore.QMetaObject.connectSlotsByName(self.grade_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Выбрать группу"))
        self.pushButton.setText(_translate("MainWindow", "Открыть журнал"))
        self.label_2.setText(_translate("MainWindow", "Группа"))
        self.label.setText(_translate("MainWindow", "Дисциплина"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))

    def show_teacher_journal_window(self):
        self.teacher_journal_window.show()
        self.grade_window.hide()

    def close_window(self):
        self.grade_window.close()
