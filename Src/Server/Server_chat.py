import socket
import os
import sys
import pickle
import threading

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Setting import until


class ServerToClient:
    def __init__(self, ServerIP, ServerPort):
        self.s = socket.socket()
        self.s.bind((ServerIP, ServerPort))
        self.s.listen(5)
        self.ChunkSize = until.Chunk_Size  # 1024
        self.clients_socket = []  # 连接的客户端socket列表
        self.Users = []  # 用户组

    # 广播聊天信息：
    def Broadcast(self, message):
        for client in self.clients_socket:
            try:
                client.sendall(message.encode())
            except:
                self.clients_socket.remove(client)

    # 发送用户组:
    def SendUsers(self):
        data = pickle.dumps(self.Users)
        self.Broadcast(data)

    def handle_client(self, client_socket, addr):
        try:
            user_name = client_socket.recv(self.ChunkSize).decode("utf-8")

            User = {"name": user_name, "ip": addr[0]}
            self.Users.append(User)
            self.clients_socket.append(client_socket)
            self.SendUsers()
            while True:
                message = client_socket.recv(self.ChunkSize)
                if message:
                    self.Broadcast(message)
                else:
                    break
        except:
            pass
        finally:
            # 移除用户
            client_socket.close()
            # self.clients_socket.remove(client_socket)
            self.Users = [u for u in self.Users if u["ip"] != addr[0]]
            # for user in self.Users:
            #     if user["ip"] == addr[0]:
            #         self.Users.remove(user)
            self.SendUsers()

    def mainloop(self):
        print("服务器准备就绪，等待连接...")
        while True:
            client_socket, addr = self.s.accept()
            print("已连接")
            threading.Thread(
                target=self.handle_client, args=(client_socket, addr)
            ).start()

    def __del__(self):
        self.s.close()


if __name__ == "__main__":
    Server = ServerToClient(ServerIP=until.Serverhost, ServerPort=until.Serverport)
    Server.mainloop()
