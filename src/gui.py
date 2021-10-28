"""
Game user interface.

Docs: https://doc.qt.io/qtforpython/
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QLineEdit,
                             QPushButton, QLabel,
                             QSplitter, QHBoxLayout)

from src.algorithm import blotto_algorithm


class UserWindow(QWidget):
    """
    User's Resource value input window.
    """
    user_score = 0
    computer_score = 0

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
        # TODO: Make automatic layout
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

        if result_message == 'You are win':
            self.user_score = self.user_score + 1
        elif result_message == 'You are lose':
            self.computer_score = self.computer_score + 1

        # Activate the Window with game result
        self.result_window = ResultWindow(user_guess, computer_guess, result_message,
                                          self.user_score, self.computer_score)
        self.result_window.show()


class ResultWindow(QWidget):
    """
    Window with game result.
    """
    def __init__(self, user_result_box,
                 computer_result_box,
                 result_message_box,
                 user_score,
                 computer_score):
        super().__init__()
        self.user_result_box = user_result_box
        self.computer_result_box = computer_result_box
        self.result_message_box = result_message_box
        self.user_score = user_score
        self.computer_score = computer_score
        self.init_gui()

    def init_gui(self):

        # Lines up widgets horizontally
        horizontal_box = QHBoxLayout(self)

        # Widgets
        # TODO: Add 10 windows to compare results element by element
        #   winning windows must have a green fill
        top_left = ResultTile(f'User Guess: \n {self.user_result_box}', self)
        top_right = ResultTile(f'Computer Guess: \n {self.computer_result_box}', self)
        bottom = ResultTile(f'Result: {self.result_message_box}', self)
        basement_user_score = ResultTile(f'User: {self.user_score}', self)
        basement_computer_score = ResultTile(f'Computer: {self.computer_score}', self)

        # Divide the window into parts
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(top_left)
        splitter1.addWidget(top_right)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        splitter2.addWidget(basement_user_score)
        splitter2.addWidget(basement_computer_score)

        horizontal_box.addWidget(splitter2)
        self.setLayout(horizontal_box)

        # Window size and borders
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


class ResultTile(QLabel):
    """
    Text box with game result.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWordWrap(True)
        self.setFrameShape(QLabel.StyledPanel)
        self.setFont(QFont('Arial', 20))
        self.setAlignment(Qt.AlignCenter)


class OkButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFont(QFont('Arial', 11))
        self.move(190, 250)
        self.resize(200, 32)
