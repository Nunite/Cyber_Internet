import socket
import threading
import os
import sys
import pickle

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Setting import until


class ServerToClient:
    def __init__(self, ServerIP, ServerPort):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((ServerIP, ServerPort))
        self.s.listen(5)
        self.clients = []  # socket列表
        self.user_data = []  # 保存所有连接用户的名称和地址

    def broadcast(self, message):
        """发送消息给所有已连接的客户端"""
        for client in self.clients:
            try:
                client.sendall(message)
            except:
                self.clients.remove(client)

    def send_user_list(self):
        """发送用户列表给所有客户端"""
        data = pickle.dumps(self.user_data)
        self.broadcast(data)

    def handle_client(self, client_socket, client_addr):
        """处理单个客户端连接"""
        try:
            user_name = client_socket.recv(1024).decode("utf-8")
            user = {"name": user_name, "ip": client_addr[0]}
            self.user_data.append(user)
            self.clients.append(client_socket)  # 压入所有的socket通道

            # 向所有客户端发送用户列表
            self.send_user_list()

            # 循环接收并广播消息
            while True:
                message = client_socket.recv(1024)
                if message:
                    self.broadcast(message)
                else:
                    break
        except:
            pass
        finally:
            client_socket.close()
            self.clients.remove(client_socket)
            self.user_data = [u for u in self.user_data if u["ip"] != client_addr[0]]
            """for u in self.user_data:
                if u["ip"]==client_addr[0]:
                    self.user_data.remove(u)"""
            self.send_user_list()  # 更新用户列表并广播

    def start(self):
        print("服务器已启动，等待客户端连接...")
        while True:
            client_socket, client_addr = self.s.accept()
            threading.Thread(
                target=self.handle_client, args=(client_socket, client_addr)
            ).start()

    def __del__(self):
        self.s.close()


if __name__ == "__main__":
    server = ServerToClient(ServerIP=until.Testhost, ServerPort=until.Serverport)
    server.start()
