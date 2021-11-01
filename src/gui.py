"""
Game user interface.

Docs: https://doc.qt.io/qtforpython/
      https://ravesli.com/urok-8-upravlenie-komponovkoj-vidzhetov-v-qt5/
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QLineEdit, QPushButton,
                             QLabel, QHBoxLayout, QVBoxLayout)

from src.algorithm import blotto_algorithm


class UserWindow(QWidget):
    """
    User's Resource value input window.
    """
    _user_score = 0
    _computer_score = 0

    def __init__(self):
        super().__init__()
        self.textbox = None  # Textbox with game's rules
        self.position_one = None
        self.position_two = None
        self.position_three = None
        self.position_four = None
        self.position_five = None
        self.guess_button = None
        self.clear_button = None
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

        # User positions
        self.position_one = Position(self)
        self.position_two = Position(self)
        self.position_three = Position(self)
        self.position_four = Position(self)
        self.position_five = Position(self)

        # BUTTONS:
        # Main button for user guess
        self.guess_button = OkButton('Make a guess', self)
        self.guess_button.clicked.connect(self.click_method)

        # Button to clear user input
        self.clear_button = OkButton('Clear', self)

        # Window layouts
        vertical_layouts = QVBoxLayout(self)
        vertical_layouts.setSpacing(10)
        horizontal_layouts_rules = QHBoxLayout(self)
        horizontal_layouts_positions = QHBoxLayout(self)
        horizontal_layouts_positions.setContentsMargins(0, 0, 0, 110)
        horizontal_layouts_buttons = QHBoxLayout(self)

        # The first row - game rules
        horizontal_layouts_rules.addWidget(self.textbox)

        # The second row - user positions
        horizontal_layouts_positions.addWidget(self.position_one)
        horizontal_layouts_positions.addWidget(self.position_two)
        horizontal_layouts_positions.addWidget(self.position_three)
        horizontal_layouts_positions.addWidget(self.position_four)
        horizontal_layouts_positions.addWidget(self.position_five)

        # The third row - buttons
        horizontal_layouts_buttons.addWidget(self.guess_button)
        horizontal_layouts_buttons.addWidget(self.clear_button)

        # Put the horizontal layouts in the vertical layouts
        vertical_layouts.addStretch(1)
        vertical_layouts.addLayout(horizontal_layouts_rules)
        vertical_layouts.addLayout(horizontal_layouts_positions)
        vertical_layouts.addLayout(horizontal_layouts_buttons)

        self.setLayout(vertical_layouts)

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
            self._user_score = self._user_score + 1
        elif result_message == 'You are lose':
            self._computer_score = self._computer_score + 1

        # Activate the Window with game result
        self.result_window = ResultWindow(user_guess, computer_guess, result_message,
                                          self._user_score, self._computer_score)
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
        """
        Widgets window and their layouts.
        :return: Window
        """

        # WIDGETS
        # The first row - computer guess
        comp_position_0 = ResultTile(str(self.computer_result_box[0]), self)
        comp_position_1 = ResultTile(str(self.computer_result_box[1]), self)
        comp_position_2 = ResultTile(str(self.computer_result_box[2]), self)
        comp_position_3 = ResultTile(str(self.computer_result_box[3]), self)
        comp_position_4 = ResultTile(str(self.computer_result_box[4]), self)

        # The second row - user guess
        user_position_0 = ResultTile(str(self.user_result_box[0]), self)
        user_position_1 = ResultTile(str(self.user_result_box[1]), self)
        user_position_2 = ResultTile(str(self.user_result_box[2]), self)
        user_position_3 = ResultTile(str(self.user_result_box[3]), self)
        user_position_4 = ResultTile(str(self.user_result_box[4]), self)

        # Results
        result_message = ResultTile(f'Result: {self.result_message_box}', self)
        user_score = ResultTile(f'User: {self.user_score}', self)
        computer_score = ResultTile(f'Computer: {self.computer_score}', self)

        # WIDGETS LAYOUTS
        vertical_layouts = QVBoxLayout(self)
        horizontal_layouts_comp_guess = QHBoxLayout(self)
        horizontal_layouts_user_guess = QHBoxLayout(self)
        horizontal_layouts_result = QHBoxLayout(self)
        horizontal_layouts_score = QHBoxLayout(self)

        # Computer positions
        horizontal_layouts_comp_guess.addWidget(comp_position_0)
        horizontal_layouts_comp_guess.addWidget(comp_position_1)
        horizontal_layouts_comp_guess.addWidget(comp_position_2)
        horizontal_layouts_comp_guess.addWidget(comp_position_3)
        horizontal_layouts_comp_guess.addWidget(comp_position_4)

        # User positions
        horizontal_layouts_user_guess.addWidget(user_position_0)
        horizontal_layouts_user_guess.addWidget(user_position_1)
        horizontal_layouts_user_guess.addWidget(user_position_2)
        horizontal_layouts_user_guess.addWidget(user_position_3)
        horizontal_layouts_user_guess.addWidget(user_position_4)
        horizontal_layouts_user_guess.setContentsMargins(0, 0, 0, 50)

        # Result message
        horizontal_layouts_result.addWidget(result_message)

        # Game score
        horizontal_layouts_score.addWidget(user_score)
        horizontal_layouts_score.addWidget(computer_score)

        # Put the horizontal layouts in the vertical layouts
        vertical_layouts.addStretch(1)
        vertical_layouts.addWidget(QLabel('Computer:'))
        vertical_layouts.addLayout(horizontal_layouts_comp_guess)
        vertical_layouts.addWidget(QLabel('User:'))
        vertical_layouts.addLayout(horizontal_layouts_user_guess)
        vertical_layouts.addLayout(horizontal_layouts_result)
        vertical_layouts.addLayout(horizontal_layouts_score)

        self.setLayout(vertical_layouts)

        # Window size and borders
        self.setGeometry(550, 350, 600, 300)
        self.setWindowTitle('Blotto Game Result')
        self.show()


class Position(QLineEdit):
    """
    Position configuration.
    """
    def __init__(self, *args):
        super().__init__(*args)
        self.setFont(QFont('Arial', 30))
        self.setAlignment(Qt.AlignCenter)


class TextBox(QLabel):
    """
    Text box with game rules configuration.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWordWrap(True)
        self.setFont(QFont('Arial', 12))


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
