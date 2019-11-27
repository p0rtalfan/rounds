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
        self.pushButton.setFixedSize(100, 100)
        self.pushButton.clicked.connect(self.circle)

        self.label = QLabel()
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        x, y = [randint(10, 500) for i in range(2)]
        w, h = [randint(10, 100) for i in range(2)]
        # создаем экземпляр QPainter, передавая холст (self.label.pixmap())
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        a = QColor(*[randint(0, 255) for i in range(3)])
        pen.setColor(a)
        painter.setPen(pen)
        painter.drawEllipse((x, y, w, h), fill=a)
        painter.end()
        self.update()


app = QApplication(sys.argv)
ex = MainWidget()
sys.exit(app.exec_())