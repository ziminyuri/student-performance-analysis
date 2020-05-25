from PyQt5 import QtCore, QtGui, QtWidgets
from forms.py_analytics.group_diagram import FormGroupDiagram
import numpy as np
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarSeries, QValueAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class FormAnalyticsTableGroup(object):
    def __init__(self, main_window):
        self.session = main_window.session
        self.result: str = ''
        self.group_analytics_window = main_window.group_analytics_window
        self.analytics_table_group_window = main_window.analytics_table_group_window
        self.analytics_table_group_window.setObjectName("MainWindow")
        self.analytics_table_group_window.setFixedSize(800, 437)
        self.analytics_table_group_window.setStyleSheet("background-color: #1a222c; border-color: #24303f; border-width: 1px;")
        self.centralwidget = QtWidgets.QWidget(self.analytics_table_group_window)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 751, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setStyleSheet("color: #c2cdd9; font: 12px;")
        self.tableWidget.horizontalHeader().setStyleSheet("background-color: #344c68; font: 14px;")
        self.tableWidget.verticalHeader().setStyleSheet("background-color: #344c68; font: 14px; ")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.label.setObjectName("label")
        self.label.setStyleSheet("font: 12px; color: #c2cdd9;")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(125, 10, 291, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("font: 12px; color: #c2cdd9;")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("font: 12px; color: #c2cdd9;")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 30, 291, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("font: 12px; color: #c2cdd9;")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 370, 191, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; min-width: 10em; padding: 6px; margin:5px; color: #c2cdd9;")

        self.pushButton.clicked.connect(self.show_diagram)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 370, 111, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; min-width: 10em; padding: 6px; margin:5px; color: #c2cdd9;")

        self.pushButton_2.clicked.connect(self.previous_page)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 370, 112, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(
            "background-color: #24303f; border-width: 1px; border-radius: 10px; border-color: #24303f; font: 12px; min-width: 10em; padding: 6px; margin:5px; color: #c2cdd9;")

        self.pushButton_3.clicked.connect(self.close_window)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 10, 58, 16))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("font-weight: bold")
        self.label_5.setStyleSheet("font: 12px; color: #c2cdd9;")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(510, 10, 150, 16))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("font: 12px; color: #c2cdd9;")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 30, 58, 16))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("font-weight: bold")
        self.label_7.setStyleSheet("font: 12px; color: #c2cdd9;")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(510, 30, 58, 16))
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet("font: 12px; color: #c2cdd9;")
        self.analytics_table_group_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.analytics_table_group_window)
        self.statusbar.setObjectName("statusbar")
        self.analytics_table_group_window.setStatusBar(self.statusbar)

        self.group_diagram_window = QtWidgets.QMainWindow()
        self.group_diagram_ui = FormGroupDiagram(self)

        self.retranslateUi(self.analytics_table_group_window)
        QtCore.QMetaObject.connectSlotsByName(self.analytics_table_group_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализ успеваемости группы"))
        self.label.setText(_translate("MainWindow", "Номер группы:"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Тип анализа:"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "Отобразить диаграмму"))
        self.pushButton_2.setText(_translate("MainWindow", "Назад"))
        self.pushButton_3.setText(_translate("MainWindow", "Закрыть"))
        self.label_5.setText(_translate("MainWindow", "Период:"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "Сессия:"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))

    def close_window(self):
        self.analytics_table_group_window.close()

    def previous_page(self):
        self.analytics_table_group_window.hide()
        self.group_analytics_window.show()

    def show_diagram(self):
        self.group_diagram_ui.label_4.setText(self.label_2.text())
        self.group_diagram_ui.label_7.setText(self.label_8.text())
        self.group_diagram_ui.label_8.setText(self.label_6.text())
        self.group_diagram_ui.label_10.setText(self.label_4.text())

        max_value = 0
        series = QBarSeries()
        for i in self.result:
            set0 = QBarSet(i[0])
            set0.append(float(i[1]))
            series.append(set0)
            if max_value < (float(i[1])):
                max_value = float(i[1])

        axisY = QValueAxis()
        axisY.setRange(0, max_value)

        chart = QChart()
        series.attachAxis(axisY)
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.SeriesAnimations)

        chart.addAxis(axisY, Qt.AlignLeft)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        centralwidget = self.group_diagram_ui.centralwidget
        self.group_diagram_ui.chartview = QChartView(chart, centralwidget)
        self.group_diagram_ui.chartview.setGeometry(QtCore.QRect(10, 110, 551, 371))
        self.group_diagram_ui.pushButton_3.show()
        self.group_diagram_window.show()



