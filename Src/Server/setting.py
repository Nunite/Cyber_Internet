import socket

def get_host_ip():
    try:
        # 创建一个socket对象
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 尝试连接到一个遥远的地址，这里使用了Google的公共DNS服务器
        # 这个操作不会真正发送数据包，只会触发网络层寻找本机出口的IP地址
        s.connect(('8.8.8.8', 80))

        # 获取本机的IPv4地址
        ip = s.getsockname()[0]
    except Exception as e:
        ip = '127.0.0.1'
        print("获取本机IP地址失败，错误信息：", e)
    finally:
        s.close()

    return ip

