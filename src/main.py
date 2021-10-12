"""
Main module.
"""

from PyQt5.QtWidgets import QApplication
from src.gui import UserWindow, Window

# app = QApplication([])
# window = UserWindow()
# app.exec_()

app = QApplication([])
window = Window()
app.exec_()
