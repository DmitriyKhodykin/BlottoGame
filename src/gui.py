"""
Game user interface.

Docs: https://doc.qt.io/qtforpython/
      https://ravesli.com/urok-8-upravlenie-komponovkoj-vidzhetov-v-qt5/
"""

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QLineEdit, QPushButton,
                             QLabel, QHBoxLayout, QVBoxLayout, QGridLayout)

from src.algorithm import blotto_algorithm


class UserWindow(QWidget):
    """
    User's Resource value input window.
    """
    _user_score = 0
    _computer_score = 0

    def __init__(self):
        super().__init__()
        self.textbox = None
        self.user_positions_grid = None
        self.guess_button = None
        self.clear_button = None
        self.result_window = None
        self.init_gui()

    def init_gui(self):
        """
        Resource allocation window.
        :return: None
        """
        # WIDGETS:
        # Game rules
        rules = "Rules. You have 100 resource units. " \
                "Distribute resources by " \
                "position in such a way that you are quantitatively " \
                "superior to your opponent in as many positions as possible."

        self.textbox = TextBox(rules, self)

        # User positions
        self.user_positions_grid = QGridLayout()
        for i in range(5):
            position = Position(self)
            self.user_positions_grid.addWidget(position, 0, i)

        # Main button for user guess
        self.guess_button = OkButton('Make a guess', self)
        self.guess_button.clicked.connect(self.click_method)

        # Button to clear user input
        self.clear_button = OkButton('Clear', self)
        self.clear_button.clicked.connect(self.clear_method)

        # WINDOW LAYOUTS:
        vertical_layouts = QVBoxLayout(self)
        vertical_layouts.setSpacing(10)
        horizontal_layouts_rules = QHBoxLayout(self)
        self.user_positions_grid.setContentsMargins(0, 0, 0, 110)
        horizontal_layouts_buttons = QHBoxLayout(self)

        # The first row - game rules
        horizontal_layouts_rules.addWidget(self.textbox)

        # The second row - user_positions_grid
        # The third row - buttons
        horizontal_layouts_buttons.addWidget(self.guess_button)
        horizontal_layouts_buttons.addWidget(self.clear_button)

        # Put the horizontal layouts in the vertical layouts
        vertical_layouts.addStretch(1)
        vertical_layouts.addLayout(horizontal_layouts_rules)
        vertical_layouts.addLayout(self.user_positions_grid)
        vertical_layouts.addLayout(horizontal_layouts_buttons)

        # FINAL LAYOUT
        self.setLayout(vertical_layouts)

        # WINDOW GEOMETRY:
        self.setGeometry(500, 300, 600, 300)
        self.setWindowTitle('Blotto Game')
        self.show()

    def get_user_guess(self) -> list:
        """
        Get list with user positions.
        :return: List like [20, 20, 20, 20, 20]
        """
        user_guess: list = []

        for i in range(5):
            widget_of_grid = self.user_positions_grid.itemAtPosition(0, i)
            widget = widget_of_grid.widget()
            num_of_widget = int(widget.text())
            user_guess.append(num_of_widget)

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

    def clear_method(self):
        """
        Clear data from user positions.
        :return: None
        """
        for i in range(5):
            widget_of_grid = self.user_positions_grid.itemAtPosition(0, i)
            widget = widget_of_grid.widget()
            widget.clear()


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

        # WIDGETS AND LAYOUTS:
        # Main vertical layout for align others layouts
        vertical_layouts = QVBoxLayout(self)

        # The first row - computer guess
        horizontal_layouts_comp_guess = QHBoxLayout(self)

        for i in self.computer_result_box:
            comp_position = ResultTile(str(i), self)
            horizontal_layouts_comp_guess.addWidget(comp_position)

        # The second row - user guess
        horizontal_layouts_user_guess = QHBoxLayout(self)

        for i in self.user_result_box:
            user_position = ResultTile(str(i), self)
            horizontal_layouts_user_guess.addWidget(user_position)

        horizontal_layouts_user_guess.setContentsMargins(0, 0, 0, 80)

        # The third row - results
        horizontal_layouts_result = QHBoxLayout(self)
        horizontal_layouts_score = QHBoxLayout(self)

        result_message = ResultTile(f'Result: {self.result_message_box}', self)
        user_score = ResultTile(f'User: {self.user_score}', self)
        computer_score = ResultTile(f'Computer: {self.computer_score}', self)

        horizontal_layouts_result.addWidget(result_message)
        horizontal_layouts_score.addWidget(user_score)
        horizontal_layouts_score.addWidget(computer_score)

        # FINAL LAYOUT:
        # Put the horizontal layouts in the vertical layouts
        vertical_layouts.addStretch(1)
        vertical_layouts.addWidget(QLabel('Computer:'))
        vertical_layouts.addLayout(horizontal_layouts_comp_guess)
        vertical_layouts.addWidget(QLabel('User:'))
        vertical_layouts.addLayout(horizontal_layouts_user_guess)
        vertical_layouts.addLayout(horizontal_layouts_result)
        vertical_layouts.addLayout(horizontal_layouts_score)

        self.setLayout(vertical_layouts)

        # WINDOW GEOMETRY:
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
        self.setFrameShape(QLabel.Box)
        self.setFont(QFont('Arial', 20))
        self.setAlignment(Qt.AlignCenter)


class OkButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFont(QFont('Arial', 11))
