from PyQt5 import QtCore, QtWidgets
from forms.py.diagram import form_diagram


class form_analytics(object):
    def __init__(self, MainWindow):
        self.analytics_window = MainWindow.analytics_window
        self.analytics_window.setObjectName("MainWindow")
        self.analytics_window.resize(589, 306)
        self.centralwidget = QtWidgets.QWidget(self.analytics_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(12, 12, 561, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        ls = ['Алгоритмы и сруктуры данных', 'Операционные системы']
        self.comboBox.addItems(ls)
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 4, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        ls_3 = ['Круговая', 'Столбчатая']
        self.comboBox_3.addItems(ls_3)
        self.gridLayout.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        ls_2 = ['324234', '423234']
        self.comboBox_2.addItems(ls_2)
        self.gridLayout.addWidget(self.comboBox_2, 3, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 5, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 240, 191, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_diagram_window)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 240, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close_window)
        self.analytics_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.analytics_window)
        self.statusbar.setObjectName("statusbar")
        self.analytics_window.setStatusBar(self.statusbar)

        self.diagram_window = QtWidgets.QMainWindow()
        self.diagram_ui = form_diagram(self)

        self.retranslateUi(self.analytics_window)
        QtCore.QMetaObject.connectSlotsByName(self.analytics_window)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Аналитика"))
        self.label.setText(_translate("MainWindow", "Дисциплина"))
        self.label_2.setText(_translate("MainWindow", "Группа"))
        self.radioButton_2.setText(_translate("MainWindow", "Количество сданных лабораторных точек"))
        self.radioButton.setText(_translate("MainWindow", "Оценки"))
        self.label_3.setText(_translate("MainWindow", "Вид диаграммы"))
        self.label_4.setText(_translate("MainWindow", "Категория"))
        self.radioButton_3.setText(_translate("MainWindow", "Количество сданных контрольный точек"))
        self.pushButton.setText(_translate("MainWindow", "Построить диаграмму"))
        self.pushButton_2.setText(_translate("MainWindow", "Закрыть"))

    def show_diagram_window(self):
        self.diagram_window.show()
        self.analytics_window.hide()

    def close_window(self):
        self.analytics_window.close()