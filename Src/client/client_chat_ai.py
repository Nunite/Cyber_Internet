from client_chat_ui import Ui_Ui
import pickle
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6 import QtWidgets
import socket
import time
import threading
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Setting import until

# from PySide6.QtCore import Qt


class ClientToServer:
    def __init__(self, ServerIP, ServerPort, username):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ServerIP = ServerIP
        self.ServerPort = ServerPort
        self.username = username

    def connect_to_server(self):
        """连接到服务器并发送用户名"""
        self.s.connect((self.ServerIP, self.ServerPort))
        self.s.sendall(self.username.encode("utf-8"))

    def send_chat_message(self, message):
        """发送聊天消息给服务器"""
        self.s.sendall(message.encode("utf-8"))

    def receive_messages(self, update_chat, update_users):
        """接收服务器消息（包括用户列表和聊天消息）"""
        while True:
            try:
                data = self.s.recv(1024)
                try:
                    message = data.decode("utf-8")
                    update_chat(message)  # 更新聊天窗口
                except UnicodeDecodeError:
                    user_list = pickle.loads(data)
                    update_users(user_list)  # 更新用户列表
            except:
                break

    def __del__(self):
        self.s.close()


class MainWindow(QMainWindow):
    def __init__(self, client, parent=None):
        super().__init__(parent)
        self.client = client
        self.ui = Ui_Ui()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.bind_buttons()
        self.bind_shortcuts()

        threading.Thread(
            target=self.client.receive_messages,
            args=(self.update_chat, self.update_users),
        ).start()

    def bind_buttons(self):
        self.ui.SendButton.clicked.connect(self.send_click)
        self.ui.ClearButton.clicked.connect(lambda: self.ui.plainTextEdit.clear())

    def bind_shortcuts(self):
        QShortcut(QKeySequence("Ctrl+S"), self.ui.plainTextEdit).activated.connect(
            self.send_click
        )

    def send_click(self):
        """发送聊天信息"""
        text_data = self.ui.plainTextEdit.toPlainText()
        if text_data:
            message = f"{self.client.username}: {text_data}"
            self.client.send_chat_message(message)
            self.ui.plainTextEdit.clear()

    def update_chat(self, chat_data):
        """更新聊天窗口"""
        self.ui.textEdit.append(chat_data)

    def update_users(self, users):
        """更新用户列表"""
        self.ui.tableWidget.setRowCount(len(users))
        for row, user in enumerate(users):
            self.ui.tableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(user["name"])
            )
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(user["ip"]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    username = "ClientUser"  # 可以改为动态输入用户名
    client = ClientToServer(
        ServerIP=until.Testhost, ServerPort=until.Serverport, username=username
    )
    client.connect_to_server()
    win = MainWindow(client=client)
    win.setWindowTitle("Qt ChatRoom")
    win.show()
    app.exec()
