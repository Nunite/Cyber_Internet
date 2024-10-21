import socket,os,tqdm


def SendFile():
    # 获取文件:
    print("请输入要传输的文件地址:")
    filename = input()
    filename_base = os.path.basename(filename)
    print(f"filename={filename}")
    print(f"filename_bsae={filename_base}")
"""     # 建立连接:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.43.130', 7230)) """
    
SendFile()
#connect()
