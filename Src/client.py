import socket

def connect():
    # 建立连接:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.43.130', 7230))
    data =s.recv(1024).decode("utf-8")
    print("从服务器接收到的数据:", data)  # 解码接收到的数据
    while True:
        sendcontent = input("请输入要发送的内容(如果输入Quit则表示退出): ")
        if sendcontent == "Quit":
            # 关闭连接
            s.close()   
            break
        # 发送数据:
        s.sendall(sendcontent.encode("utf-8"))
        # 接收数据:
        data =s.recv(1024).decode("utf-8")
        print("从服务器接收到的数据:", data)  # 解码接收到的数据

connect()
