"""
Game user interface.

Docs: https://doc.qt.io/qtforpython/,
      https://doc.qt.io/qt-5/qtexamplesandtutorials.html
"""

import sys

from PyQt5.QtGui import QTextTableFormat
from PyQt5.QtWidgets import (QWidget, QLineEdit, QInputDialog,
                             QApplication, QLabel, QPushButton, QDockWidget, QListWidget)
from PyQt5.uic.properties import QtWidgets, QtGui


class UserWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.init_gui()

    def init_gui(self):

        left_border = 45
        top_border = 120
        position_width = 100
        position_height = 100

        rule_table = QTextTableFormat()

        # rules = QListWidget(self)
        # rules.addItems("""
        # You have 100 resource units. Distribute resources by
        # position in such a way that you are quantitatively
        # superior to your opponent in as many positions as possible.
        # """)
        # rules.move(15, 5)

        position1 = QLineEdit(self)
        position1.move(left_border, top_border)
        position1.resize(position_width, position_height)

        position2 = QLineEdit(self)
        position2.move(left_border + position_width, top_border)
        position2.resize(position_width, position_height)

        position3 = QLineEdit(self)
        position3.move(left_border + position_width * 2, top_border)
        position3.resize(position_width, position_height)

        position4 = QLineEdit(self)
        position4.move(left_border + position_width * 3, top_border)
        position4.resize(position_width, position_height)

        position5 = QLineEdit(self)
        position5.move(left_border + position_width * 4, top_border)
        position5.resize(position_width, position_height)

        button = QPushButton('Make a guess', self)
        button.clicked.connect(self.click_method)
        button.move(190, 250)
        button.resize(200, 32)

        self.setGeometry(600, 300, 600, 300)
        self.setWindowTitle('Blotto Game')
        self.show()

    def click_method(self):
        print('Your name: ' + self.line.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UserWindow()
    sys.exit(app.exec_())
