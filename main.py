"""
Main module.
"""

from PyQt5.QtWidgets import QApplication
from src.gui import Window


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    app.exec_()
