import socket, os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Setting import setting


def OpenServer():
    # 创建socket:
    s = socket.socket()
    s.bind((setting.Serverhost, setting.Serverport))
    s.listen(5)
    print(f"客户端监听:{setting.Serverhost}:{setting.Serverport}")
    # 获取信息:
    client_socket, addr = s.accept()
    print(f"接受客户端{addr}的连接")
    FileInfo = client_socket.recv(setting.Chunk_Size).decode()
    FileName, FileSize = FileInfo.split(setting.SEPARATOR)
    FileSize = int(FileSize)
    # 获取当前工作目录
    current_directory = os.getcwd()
    # 拼接文件路径
    file_path = os.path.join(current_directory, FileName)
    # 接受并创建文件:
    with open(file_path, "+wb") as f:
        while True:
            FileContent = client_socket.recv(setting.Chunk_Size)
            if not FileContent:
                break
            f.write(FileContent)
    client_socket.close()
    s.close()


OpenServer()
