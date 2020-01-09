import sys
from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import *
import time
from random import randint as r


class MyWidget(QWidget):
    def __init__(self, parent=None):
        try:
            super().__init__(parent)
            #uic.loadUi('UI.ui', self)
            self.x = r(0, 200)
            self.y = r(0, 200)
            self.z = r(0, 200)
            self.p = r(0, 200)
            box = QVBoxLayout(self)
            self.setGeometry(150, 150, 400, 400)
            self.pushButton = QPushButton('Нажми на меня')
            box.addWidget(self.pushButton)
            self.pushButton.clicked.connect(self.draw)
        except Exception as e:
            print(str(e))

    def draw(self):
        dr = Drawer()
        dr.start()


class Drawer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def start(self):
        self.x = r(0, 200)
        self.y = r(0, 200)
        self.z = r(0, 200)
        self.p = r(0, 200)
        self.update()

    def paintEvent(self, e):
        try:
            qp = QPainter()
            qp.begin(self)
            new_change = False
            color = QColor(0, 0, 0)
            color.setNamedColor('#ffff00')
            qp.setPen(color)
            qp.setBrush(color)
            qp.drawEllipse(self.x, self.y, self.z, self.p)
            qp.end()
        except Exception as e:
            print(str(e))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())