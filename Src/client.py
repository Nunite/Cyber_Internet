import socket
# 建立连接:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 7230))
# 发送数据:
s.sendall(b'Hello, world!')
# 接收数据:  
d = s.recv(1024)
print(d)
s.close()

