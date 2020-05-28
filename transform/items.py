import numpy as np
from PyQt5 import QtWidgets, QtGui
from settings import DARK_THEME


def set_items_to_table(table, items: np.ndarray):
    try:
        rows, columns = items.shape
    except:
        return table

    table.setRowCount(rows)
    table.setColumnCount(columns)
    flag = 0
    for i in range(rows):
        if i%2 == 0:
            flag = 1
        for j in range(columns):
            newitem = QtWidgets.QTableWidgetItem(items[i][j])
            if flag == 0 and DARK_THEME is True:
                newitem.setBackground(QtGui.QColor(36, 48, 63))
            table.setItem(i, j, QtWidgets.QTableWidgetItem(newitem))
        flag = 0

    return table