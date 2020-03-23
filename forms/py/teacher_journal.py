from PyQt5 import QtCore, QtWidgets


class form_teacher_journal(object):
    def __init__(self, MainWindow):
        self.teacher_journal_window = MainWindow.teacher_journal_window
        self.teacher_journal_window.setObjectName("MainWindow")
        self.teacher_journal_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self.teacher_journal_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setStyleSheet("t")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.close_window)
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.teacher_journal_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.teacher_journal_window)
        self.statusbar.setObjectName("statusbar")
        self.teacher_journal_window.setStatusBar(self.statusbar)

        self.retranslateUi(self.teacher_journal_window)
        QtCore.QMetaObject.connectSlotsByName(self.teacher_journal_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Оценки"))
        self.pushButton.setText(_translate("MainWindow", "Закрыть"))

    def close_window(self):
        self.teacher_journal_window.close()
