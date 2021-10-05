"""
Game user interface.

Docs: https://wiki.python.org/moin/PyQt
"""

from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])
window = QWidget()
window.setGeometry(500, 200, 600, 300)
window.setWindowTitle("Blotto Game")
window.show()
app.exec()
