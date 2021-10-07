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
        self.position1 = None
        self.position2 = None
        self.position3 = None
        self.position4 = None
        self.position5 = None
        self.button = None
        self.init_gui()

    def init_gui(self):
        """
        Window for entering user suggestion.
        :return: None
        """
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

        # Positions
        self.position1 = QLineEdit(self)
        self.position1.setFont(QFont('Arial', 25))
        self.position1.setAlignment(Qt.AlignCenter)
        self.position1.move(left_border, top_border)
        self.position1.resize(position_width, position_height)

        self.position2 = QLineEdit(self)
        self.position2.setFont(QFont('Arial', 25))
        self.position2.setAlignment(Qt.AlignCenter)
        self.position2.move(left_border + position_width, top_border)
        self.position2.resize(position_width, position_height)

        self.position3 = QLineEdit(self)
        self.position3.setFont(QFont('Arial', 25))
        self.position3.setAlignment(Qt.AlignCenter)
        self.position3.move(left_border + position_width * 2, top_border)
        self.position3.resize(position_width, position_height)

        self.position4 = QLineEdit(self)
        self.position4.setFont(QFont('Arial', 25))
        self.position4.setAlignment(Qt.AlignCenter)
        self.position4.move(left_border + position_width * 3, top_border)
        self.position4.resize(position_width, position_height)

        self.position5 = QLineEdit(self)
        self.position5.setFont(QFont('Arial', 25))
        self.position5.setAlignment(Qt.AlignCenter)
        self.position5.move(left_border + position_width * 4, top_border)
        self.position5.resize(position_width, position_height)

        # Ok Button
        self.button = QPushButton('Make a guess', self)
        self.button.setFont(QFont('Arial', 11))
        self.button.clicked.connect(self.click_method)
        self.button.move(190, 250)
        self.button.resize(200, 32)

        # Window Geometry
        self.setGeometry(500, 300, 600, 300)
        self.setWindowTitle('Blotto Game')
        self.show()

    def click_method(self):
        """
        How to proceed after clicking.
        :return:
        """
        position_number_1 = int(self.position1.text())
        position_number_2 = int(self.position2.text())
        position_number_3 = int(self.position3.text())
        position_number_4 = int(self.position4.text())
        position_number_5 = int(self.position5.text())
        user_guess = [position_number_1,
                      position_number_2,
                      position_number_3,
                      position_number_4,
                      position_number_5]
        print(user_guess)


if __name__ == '__main__':
    app = QApplication([])
    window = UserWindow()
    app.exec_()
