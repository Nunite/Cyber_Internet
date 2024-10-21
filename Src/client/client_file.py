import socket, os, setting


def SendFile():
    # 连接服务器:
    s = socket.socket()
    print(f"服务器连接中{setting.Serverhost}:{setting.Serverport}")
    s.connect((setting.Serverhost, setting.Serverport))
    # 获取文件:
    print("请输入要传输的文件地址:")
    FileName = input()
    FileName_Base = os.path.basename(FileName)
    File_Size = os.path.getsize(FileName)
    # 构建前缀:
    datastr = f"{FileName_Base}{setting.SEPARATOR}{File_Size}"
    s.send(datastr.encode())

    with open(FileName, "rb") as f:
        while True:
            chunk = f.read(setting.Chunk_Size)
            if not chunk:
                break
            s.sendall(chunk)
    s.close()


SendFile()
# connect()
