# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/qt/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_reports = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reports.setObjectName("pushButton_reports")
        self.gridLayout.addWidget(self.pushButton_reports, 0, 4, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy)
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout.addWidget(self.pushButton_close, 0, 5, 1, 1)
        self.pushButton_analytics = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_analytics.setObjectName("pushButton_analytics")
        self.gridLayout.addWidget(self.pushButton_analytics, 0, 3, 1, 1)
        self.pushButton_student = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_student.setObjectName("pushButton_student")
        self.gridLayout.addWidget(self.pushButton_student, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 6)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 6)
        self.pushButton_lesson = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_lesson.setObjectName("pushButton_lesson")
        self.gridLayout.addWidget(self.pushButton_lesson, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 6)
        self.pushButton_grade = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_grade.setObjectName("pushButton_grade")
        self.gridLayout.addWidget(self.pushButton_grade, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_reports.setText(_translate("MainWindow", "Отчеты"))
        self.pushButton_close.setText(_translate("MainWindow", "Выход"))
        self.pushButton_analytics.setText(_translate("MainWindow", "Аналитика"))
        self.pushButton_student.setText(_translate("MainWindow", "Студенты"))
        self.pushButton_lesson.setText(_translate("MainWindow", "Дисциплины"))
        self.label.setText(_translate("MainWindow", "Отстаующие студенты"))
        self.pushButton_grade.setText(_translate("MainWindow", "Оценки"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
