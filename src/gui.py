"""
Game user interface.

Docs: https://doc.qt.io/qtforpython/,
      https://doc.qt.io/qt-5/qtexamplesandtutorials.html
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QLineEdit,
                             QApplication, QPushButton, QLabel)


class UserWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_gui()

    def init_gui(self):

        left_border = 45
        top_border = 130
        position_width = 100
        position_height = 100

        # Game rules
        rules = "Rules. You have 100 resource units. " \
                "Distribute resources by " \
                "position in such a way that you are quantitatively " \
                "superior to your opponent in as many positions as possible."

        textbox = QLabel(rules, self)
        textbox.setWordWrap(True)
        textbox.setFont(QFont('Arial', 11))
        textbox.move(left_border, 10)
        textbox.resize(500, 100)

        position1 = QLineEdit(self)
        position1.setFont(QFont('Arial', 25))
        position1.setAlignment(Qt.AlignCenter)
        position1.move(left_border, top_border)
        position1.resize(position_width, position_height)

        position2 = QLineEdit(self)
        position2.setFont(QFont('Arial', 25))
        position2.setAlignment(Qt.AlignCenter)
        position2.move(left_border + position_width, top_border)
        position2.resize(position_width, position_height)

        position3 = QLineEdit(self)
        position3.setFont(QFont('Arial', 25))
        position3.setAlignment(Qt.AlignCenter)
        position3.move(left_border + position_width * 2, top_border)
        position3.resize(position_width, position_height)

        position4 = QLineEdit(self)
        position4.setFont(QFont('Arial', 25))
        position4.setAlignment(Qt.AlignCenter)
        position4.move(left_border + position_width * 3, top_border)
        position4.resize(position_width, position_height)

        position5 = QLineEdit(self)
        position5.setFont(QFont('Arial', 25))
        position5.setAlignment(Qt.AlignCenter)
        position5.move(left_border + position_width * 4, top_border)
        position5.resize(position_width, position_height)

        button = QPushButton('Make a guess', self)
        button.setFont(QFont('Arial', 11))
        button.clicked.connect(self.click_method)
        button.move(190, 250)
        button.resize(200, 32)

        self.setGeometry(500, 300, 600, 300)
        self.setWindowTitle('Blotto Game')
        self.show()

    def click_method(self):
        print('Clicked')


if __name__ == '__main__':
    app = QApplication([])
    window = UserWindow()
    app.exec_()
