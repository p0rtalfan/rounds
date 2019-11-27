import sys
from PyQt5.QtWidgets import QApplication,\
    QMainWindow,\
    QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import uic, \
    QtCore, \
    QtMultimedia
import sqlite3
from random import randint


class MainWidget(QMainWindow):
    # initialization
    def __init__(self):
        super().__init__()
        uic.loadUi('ui forms/UI.ui', self)
        self.setWindowTitle('rounds')
        self.pushButton.connect(self.a)
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)
        self.show()

    def a(self):
        x, y = [randint(10, 500) for i in range(2)]
        w, h = [randint(10, 100) for i in range(2)]
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(yellow)
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()

app = QApplication(sys.argv)
ex = MainWidget()
sys.exit(app.exec_())