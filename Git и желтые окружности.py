import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Git и желтые окружности.ui', self)
        self.go_draw = False

        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.go_draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.go_draw:
            qp = QPainter()
            qp.begin(self)
            self.drawEllipses(event, qp)
            qp.end()
            self.go_draw = False

    def drawEllipses(self, event, qp):
        cor = self.circle_cor()
        qp.setPen(QPen(Qt.yellow, cor[2]))
        qp.drawEllipse(cor[0], cor[1], cor[2], cor[2])

    def circle_cor(self):
        x_center, y_center, size = randint(1, 600), randint(1, 500), randint(1, 600)
        while x_center + size > 600 or y_center + size > 500:
            x_center, y_center, size = randint(1, 600), randint(1, 500), randint(1, 600)
        return [x_center, y_center, size]


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
