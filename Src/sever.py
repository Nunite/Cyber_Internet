import socket
import setting  # 确保这个模块存在并且正确地导入了

def opensever():
    ip = setting.get_host_ip()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((f'{ip}', 7230))
    s.listen(5)
    # 建立连接并接受数据:
    while True:
        sock, addr = s.accept()
        print('有人来连接了...')
        sock.sendall("这里是智能客服，请问有什么能帮助你？".encode("utf-8"))
        while True:
            data = sock.recv(1024)
            if not data :
                break
            print("客户说:", data.decode("utf-8"))  # 将接收到的字节解码为字符串
            sock.sendall("你说啥？".encode("utf-8"))
        s.close()
        print('服务器已关闭。') 
        break

opensever()
