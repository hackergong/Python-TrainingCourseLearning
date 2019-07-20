import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('172.18.81.188',8084))


while True:
    data = input("client:")
    client.send(data.encode("utf-8"))
    info = client.recv(1024)
    print("server：%s" % (info.decode("utf-8")))














