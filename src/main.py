"""
Main module.
"""

from PyQt5.QtWidgets import QApplication
from src.gui import UserWindow, Window

app = QApplication([])
window = Window()
app.exec_()
