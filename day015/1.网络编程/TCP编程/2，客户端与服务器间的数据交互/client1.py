import socket

client1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client1.connect(('172.18.81.188',8084))


while True:
    data = input("Please enter the data sent to the server:")
    client1.send(data.encode("utf-8"))
    info = client1.recv(1024)
    print("server：%s" % (info.decode("utf-8")))














