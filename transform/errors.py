from PyQt5.QtWidgets import QMessageBox


def login_error():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Ошибка")
    msg.setInformativeText('Не правильная пара логин/пароль')
    msg.setWindowTitle("Ошибка")
    msg.exec_()


def bd_error():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Ошибка синхронизации с БД")
    msg.setInformativeText('Попробуйте открыть окно еще раз.')
    msg.setWindowTitle("Ошибка синхронизации с БД")
    msg.exec_()
