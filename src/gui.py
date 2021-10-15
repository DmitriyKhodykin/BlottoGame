"""
Game user interface.

Docs: https://doc.qt.io/qtforpython/
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QLineEdit,
                             QPushButton, QLabel)

from src.algorithm import blotto_algorithm


class UserWindow(QWidget):
    """
    User's Resource value input window.
    """
    def __init__(self):
        super().__init__()
        self.textbox = None  # Textbox with game's rules
        self.position_one = None
        self.position_two = None
        self.position_three = None
        self.position_four = None
        self.position_five = None
        self.button = None
        self.left_border = 45  # Border for all elements
        self.top_border_human = 130  # Border for human positions
        self.result_window = None
        self.init_gui()

    def init_gui(self):
        """
        Basic Window layout.
        :return: None
        """

        # Game rules
        rules = "Rules. You have 100 resource units. " \
                "Distribute resources by " \
                "position in such a way that you are quantitatively " \
                "superior to your opponent in as many positions as possible."

        self.textbox = TextBox(rules, self)
        self.textbox.move(self.left_border, 10)

        # User positions
        self.position_one = Position(self)
        self.position_one.move(self.left_border, self.top_border_human)

        self.position_two = Position(self)
        self.position_two.move(self.left_border + 100, self.top_border_human)

        self.position_three = Position(self)
        self.position_three.move(self.left_border + 200, self.top_border_human)

        self.position_four = Position(self)
        self.position_four.move(self.left_border + 300, self.top_border_human)

        self.position_five = Position(self)
        self.position_five.move(self.left_border + 400, self.top_border_human)

        # Ok Button
        self.button = OkButton('Make a guess', self)
        self.button.clicked.connect(self.click_method)

        # Window Geometry
        self.setGeometry(500, 300, 600, 300)
        self.setWindowTitle('Blotto Game')
        self.show()

    def get_user_guess(self) -> list:
        """
        Get list with user positions.
        :return: List like [20, 20, 20, 20, 20]
        """
        position_number_6 = int(self.position_one.text())
        position_number_7 = int(self.position_two.text())
        position_number_8 = int(self.position_three.text())
        position_number_9 = int(self.position_four.text())
        position_number_10 = int(self.position_five.text())
        user_guess = [position_number_6,
                      position_number_7,
                      position_number_8,
                      position_number_9,
                      position_number_10]
        return user_guess

    def click_method(self):
        """
        How to proceed after clicking.
        :return: None
        """
        user_guess: list = self.get_user_guess()    # Like [20, 20, 20, 20, 20]
        game_result = blotto_algorithm(user_guess)  # Calculate the result
        computer_guess: list = game_result[0]       # Like [20, 20, 20, 20, 20]
        result_message: str = game_result[1]        # Like "You are win"

        # Activate the Window with game result
        self.result_window = ResultWindow(user_guess, computer_guess, result_message)
        self.result_window.show()


class ResultWindow(QWidget):
    """
    Window with game result.
    """
    def __init__(self, user_result_box,
                 computer_result_box,
                 result_message_box):
        super().__init__()
        self.user_guess = user_result_box
        self.computer_guess = computer_result_box
        self.result_message_box = result_message_box
        self.textbox = None
        self.init_gui()

    def init_gui(self):
        result = f'Result: {self.result_message_box} \n' \
                 f'Computer guess:  {self.computer_guess} \n' \
                 f'User guess: {self.user_guess}'
        self.textbox = TextBox(result, self)
        self.textbox.move(10, 10)

        # Window Geometry
        self.setGeometry(550, 350, 600, 300)
        self.setWindowTitle('Blotto Game Result')
        self.show()


class Position(QLineEdit):
    """
    Position configuration.
    """
    position_width = 100  # Position's size
    position_height = 100

    def __init__(self, *args):
        super().__init__(*args)
        self.setFont(QFont('Arial', 25))
        self.setAlignment(Qt.AlignCenter)
        self.resize(self.position_width, self.position_height)


class TextBox(QLabel):
    """
    Text box with game rules configuration.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWordWrap(True)
        self.setFont(QFont('Arial', 11))
        self.resize(500, 100)


class OkButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFont(QFont('Arial', 11))
        self.move(190, 250)
        self.resize(200, 32)
