import sys, time
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow

from client_chat_ui import Ui_Ui


class MainWindow(QMainWindow):
    def __init__(self, parent=None, Client_User=None):
        super().__init__(parent)
        self.User = Client_User if Client_User else User("Guest", "127.0.0.1")
        self.ui = Ui_Ui()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        # 绑定按钮:
        self.ui.SendButton.clicked.connect(self.Sendclick)
        self.ui.ClearButton.clicked.connect(self.Clearclick)

        # 绑定快捷键:
        send_shortcut = QShortcut(QKeySequence("Ctrl+S"), self.ui.plainTextEdit)
        send_shortcut.activated.connect(self.Sendclick)

        clear_shortcut = QShortcut(QKeySequence("Ctrl+L"), self.ui.plainTextEdit)
        clear_shortcut.activated.connect(self.Clearclick)
        # 添加右侧用户:
        self.ui.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(self.User.name))
        self.ui.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(self.User.ip))

    def Sendclick(self):
        # 获取输入框信息:
        TextData = self.ui.plainTextEdit.toPlainText()
        if not TextData:
            return
        # 用户信息获取:
        UserData = self.User.name
        Current_Time = self.GetTime()
        # 构建消息:
        SendData = f"{UserData} {Current_Time}\n{TextData}\n"
        # 发生消息:
        self.ui.textEdit.append(SendData)
        self.ui.plainTextEdit.setPlainText("")

    def Clearclick(self):
        self.ui.plainTextEdit.setPlainText("")

    def GetTime(self):
        # 时间获取:
        CurrentTime = time.time()
        local_time = time.localtime(CurrentTime)
        # Y-year m-month d-day H-hour M-minute S-second
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        return formatted_time


class User:
    def __init__(self, name="", ip=""):
        self.name = name
        self.ip = ip

    def GetName(self):
        return self.name

    def GetIp(self):
        return self.Ip


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Current_user = User("Lws", "192.168.1.1")
    win = MainWindow(Client_User=Current_user)
    win.setWindowTitle("Qt ChatRoom")
    win.show()
    app.exec()
