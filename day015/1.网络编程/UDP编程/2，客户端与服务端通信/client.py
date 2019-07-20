import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data = input("客户端说：")
    client.sendto(data.encode("utf-8"),('172.18.81.188',8900))
    info = (client.recv(1024)).decode("utf-8")
    print("服务器说：%s" % (info))
