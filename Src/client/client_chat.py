import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

from client_chat_ui import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click)

    def click(self):
        print("Hello World!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("Qt Application")
    win.show()
    app.exec()
