import numpy as np
from PyQt5 import QtWidgets


def set_items_to_table(table, items: np.ndarray):
    try:
        rows, columns = items.shape
    except:
        return table

    table.setRowCount(rows)

    for i in range(rows):
        for j in range(columns):
            table.setItem(i, j, QtWidgets.QTableWidgetItem(items[i][j]))

    return table