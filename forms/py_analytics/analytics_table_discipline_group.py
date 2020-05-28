from PyQt5 import QtCore, QtGui, QtWidgets
from forms.py_analytics.group_diagram_discipline import FormGroupDiagramDiscipline
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarSeries, QValueAxis
from PyQt5.QtCore import Qt


class FormAnalyticsTableDisciplineGroup(object):
    def __init__(self, main_window):
        self.dark_theme = False
        self.choice_discipline_group_window = main_window.choice_discipline_group_window
        self.session = main_window.session
        self.analytics_table_discipline_group_window = main_window.analytics_table_discipline_group_window
        self.analytics_table_discipline_group_window.setObjectName("MainWindow")
        self.analytics_table_discipline_group_window.setFixedSize(800, 437)
        self.centralwidget = QtWidgets.QWidget(self.analytics_table_discipline_group_window)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 751, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 10, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 30, 400, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 370, 191, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_diagram)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 370, 111, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.previous_page)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 370, 112, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.close_window)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 10, 300, 16))
        self.label_6.setObjectName("label_6")
        self.analytics_table_discipline_group_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.analytics_table_discipline_group_window)
        self.statusbar.setObjectName("statusbar")
        self.analytics_table_discipline_group_window.setStatusBar(self.statusbar)

        self.group_diagram_discipline_window = QtWidgets.QMainWindow()
        self.group_diagram_discipline_ui = FormGroupDiagramDiscipline(self)

        self.retranslateUi(self.analytics_table_discipline_group_window)
        QtCore.QMetaObject.connectSlotsByName(self.analytics_table_discipline_group_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализ успеваемости групп"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Тип анализа:"))
        self.pushButton.setText(_translate("MainWindow", "Отобразить диаграмму"))
        self.pushButton_2.setText(_translate("MainWindow", "Назад"))
        self.pushButton_3.setText(_translate("MainWindow", "Закрыть"))
        self.label_5.setText(_translate("MainWindow", "Дисциплина:"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))

    def previous_page(self):
        self.choice_discipline_group_window.show()
        self.analytics_table_discipline_group_window.hide()

    def close_window(self):
        self.analytics_table_discipline_group_window.close()

    def show_diagram(self):
        self.group_diagram_discipline_ui.label_4.setText(self.label_6.text())
        self.group_diagram_discipline_ui.label_10.setText(self.label_2.text())

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
        centralwidget = self.group_diagram_discipline_ui.centralwidget
        self.group_diagram_discipline_ui.chartview = QChartView(chart, centralwidget)
        self.group_diagram_discipline_ui.chartview.setGeometry(QtCore.QRect(10, 110, 880, 371))
        self.group_diagram_discipline_ui.pushButton_3.setText("Отобразить диаграмму в круговом виде")
        self.group_diagram_discipline_ui.pushButton_3.show()
        self.group_diagram_discipline_ui.data = self.result
        self.group_diagram_discipline_window.show()

    def update(self, dark_theme):
        if dark_theme:

            self.dark_theme = True
        else:
            self.dark_theme = False