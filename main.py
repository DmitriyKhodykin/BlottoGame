"""
Main module.
"""

from PyQt5.QtWidgets import QApplication
from src.gui import UserWindow

if __name__ == '__main__':
    app = QApplication([])
    window = UserWindow()
    app.exec_()
