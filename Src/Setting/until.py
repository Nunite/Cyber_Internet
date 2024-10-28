Serverhost = "192.168.43.130"
Testhost = "192.168.1.169"
Serverport = 7230
Chunk_Size = 1024
SEPARATOR = "<#>"


class User:
    def __init__(self, name="", ip=""):
        self.name = name
        self.ip = ip

    def GetName(self):
        return self.name

    def GetIp(self):
        return self.ip
