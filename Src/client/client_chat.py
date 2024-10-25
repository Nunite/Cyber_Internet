import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

from client_chat_ui import Ui_Ui


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Ui()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("Lws"))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("192.168.1.1"))

        self.ui.tableWidget.setItem(1, 0, QTableWidgetItem("Lwx"))
        self.ui.tableWidget.setItem(1, 1, QTableWidgetItem("192.168.1.2"))

    def click(self):
        pass


class User:
    def __init__(self, name="", ip=""):
        self.name = name
        self.ip = ip


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("Qt Application")
    win.show()
    app.exec()
