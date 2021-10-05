"""
Game user interface.

Docs: https://wiki.python.org/moin/PyQt
"""

import sys
from PyQt5.QtWidgets import (QWidget, QLineEdit,
                             QInputDialog, QApplication)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.init_gui()

    def init_gui(self):
        position = QLineEdit(self)
        position.move(20, 20)
        position.resize(150, 30)

        self.setGeometry(500, 300, 600, 300)
        self.setWindowTitle('Blotto Game')
        self.show()

    def show_dialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
