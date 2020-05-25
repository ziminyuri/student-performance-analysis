from PyQt5 import QtCore, QtWidgets


class FormTeacherJournal(object):
    def __init__(self, main_window):
        self.teacher_journal_window = main_window.teacher_journal_window
        self.teacher_journal_window.setObjectName("MainWindow")
        self.teacher_journal_window.setFixedSize(800, 600)
        self.teacher_journal_window.setStyleSheet("background-color: #1a222c; border-color: #24303f; border-width: 1px;")
        self.centralwidget = QtWidgets.QWidget(self.teacher_journal_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.setStyleSheet("color: #c2cdd9; font: 12px;")
        self.tableWidget.horizontalHeader().setStyleSheet("background-color: #344c68; font: 14px;")
        self.tableWidget.verticalHeader().setStyleSheet("background-color: #344c68; font: 14px; ")
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
        self.pushButton.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; min-width: 10em; padding: 6px; margin:5px; color: #c2cdd9;")
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
        self.tableWidget.setRowCount(0)
        self.teacher_journal_window.close()
