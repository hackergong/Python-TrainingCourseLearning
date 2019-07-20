import socket
 # AF_INET == ipV4, SOCK_DGRAM == udp协议
udpServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpServer.bind(('172.18.81.188',8900))
while True:
    data,addr =udpServer.recvfrom(1024)
    print("客户端说：",data.decode("utf-8"))
    info = input("服务端说：")
    udpServer.sendto(info.encode("utf-8"),addr)














