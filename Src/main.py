import socket
def opensever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 7230))
    s.listen(5)
    # 建立连接并接受数据:
    while True:
        sock, addr = s.accept()
        data = sock.recv(1024)
        sock.sendall(b'hello')
        print(data)
opensever()