from PyQt5 import QtCore, QtGui, QtWidgets
from forms.py.diagram import FormDiagram


class FormAnalytics(object):
    def __init__(self, main_window):
        self.analytics_window = main_window.analytics_window
        self.analytics_window.setObjectName("MainWindow")
        self.analytics_window.setFixedSize(589, 350)
        self.analytics_window.setStyleSheet(
            "background-color: #1a222c; border-color: #24303f; border-width: 1px;")
        self.centralwidget = QtWidgets.QWidget(self.analytics_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(12, 12, 561, 229))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        ls_3 = ['Столбчатая', 'Круговая']
        self.comboBox_3.addItems(ls_3)
        self.gridLayout.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_diagram_window)
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        ls_4 = ['Оценки', 'Количество сданных лабораторных работ', 'Количество сданных контрольных работ',
                'Результаты экзамена/зачета']
        self.comboBox_4.addItems(ls_4)
        self.gridLayout.addWidget(self.comboBox_4, 5, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 280, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close_window)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 280, 221, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.analytics_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.analytics_window)
        self.statusbar.setObjectName("statusbar")
        self.analytics_window.setStatusBar(self.statusbar)

        self.diagram_window = QtWidgets.QMainWindow()
        self.diagram_ui = FormDiagram(self)

        self.retranslateUi(self.analytics_window)
        QtCore.QMetaObject.connectSlotsByName(self.analytics_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Аналитика"))
        self.label_2.setText(_translate("MainWindow", "Номер группы"))
        self.label.setText(_translate("MainWindow", "Дисциплина"))
        self.label_4.setText(_translate("MainWindow", "Категория анализа"))
        self.pushButton.setText(_translate("MainWindow", "Построить диаграмму"))
        self.label_3.setText(_translate("MainWindow", "Вид диаграммы"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))
        self.pushButton_3.setText(_translate("MainWindow", "Вывести результаты анализа"))

    def show_diagram_window(self):
        self.diagram_window.show()
        self.analytics_window.hide()

    def close_window(self):
        self.analytics_window.close()

