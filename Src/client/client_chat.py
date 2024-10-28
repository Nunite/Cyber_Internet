from client_chat_ui import Ui_Ui
import pickle
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6 import QtWidgets
import socket
import time
import os
import sys
import threading

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Setting import until

# from PySide6.QtCore import Qt


class ClientToServer:
    def __init__(self, ServerIP, ServerPort, Username):
        self.s = socket.socket()

        self.ServerIP = ServerIP
        self.ServerPort = ServerPort
        self.ClientUserName = Username
        self.ChunkSize = until.Chunk_Size

    def Connect(self):
        self.s.connect((self.ServerIP, self.ServerPort))
        self.s.sendall(self.ClientUserName.encode("utf-8"))

    def SendChatData(self, Data):
        self.s.sendall(Data.encode("utf-8"))

    def Receive_messages(self, RenderChat, GenerateUser):
        while True:
            try:
                Data = self.s.recv(self.ChunkSize)
                try:
                    message = Data.decode("utf-8")
                    RenderChat(message)
                except UnicodeDecodeError:
                    Current_users = pickle.loads(Data)
                    GenerateUser(Current_users)
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

        self.BindButton()  # 绑定按钮
        self.BindShortcut()  # 绑定快捷键

        threading.Thread(
            target=client.Receive_messages,
            args=(self.RenderChat, self.GenerateUser),
        ).start()  # 确保线程启动

    def Sendclick(self):
        # 获取输入框信息:
        TextData = self.ui.plainTextEdit.toPlainText()
        if not TextData:
            return
        # 用户信息获取:
        UserData = self.client.ClientUserName
        Current_Time = self.GetTime()
        # 构建消息:
        SendData = f"{UserData} {Current_Time}\n{TextData}\n"
        # 发生消息:
        # self.ui.textEdit.append(SendData)
        self.client.SendChatData(SendData)
        print(SendData)
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

    def BindButton(self):
        self.ui.SendButton.clicked.connect(self.Sendclick)
        self.ui.ClearButton.clicked.connect(self.Clearclick)

    def BindShortcut(self):
        send_shortcut = QShortcut(QKeySequence("Ctrl+S"), self.ui.plainTextEdit)
        send_shortcut.activated.connect(self.Sendclick)

        clear_shortcut = QShortcut(QKeySequence("Ctrl+L"), self.ui.plainTextEdit)
        clear_shortcut.activated.connect(self.Clearclick)

    def GenerateUser(self, users):
        self.ui.tableWidget.setRowCount(len(users))
        for row, user in enumerate(users):
            self.ui.tableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(user["name"])
            )
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(user["ip"]))

    def RenderChat(self, ChatData):
        self.ui.textEdit.append(ChatData)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Current_users = []
    # User_Lws = until.User("Lws", "192.168.1.1")
    # User_Lwx = until.User("Lwx", "192.168.1.2")
    # Current_users.append(User_Lws)
    # Current_users.append(User_Lwx)
    Username = "Lws"
    UserClient = ClientToServer(
        ServerIP=until.Testhost, ServerPort=until.Serverport, Username=Username
    )
    UserClient.Connect()
    win = MainWindow(client=UserClient)
    win.setWindowTitle("Qt ChatRoom")
    win.show()
    app.exec()
