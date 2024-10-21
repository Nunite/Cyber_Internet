import socket,os,tqdm

#1:connect
#2:get filename and fill <SEPARATOR>
def connect():
    # 建立连接:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.43.130', 7230))


connect()
