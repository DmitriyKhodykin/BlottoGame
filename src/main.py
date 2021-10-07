"""
Main module.
"""

from PyQt5.QtWidgets import QApplication
from src.gui import UserWindow

app = QApplication([])
window = UserWindow()
app.exec_()
