#服务器端

import socket

#socket 套接字
#创建一个socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP和端口 1024以上的端口随便用
# 本机IP可以在命令指示符中输入ipconfig查看
server.bind(('172.18.81.188',8084))
#监听
server.listen(5)
print("----Server Start Successfully-----")
#等待连接
#可以获得客户端socket和地址
clientSocket,clientAddress = server.accept()  #目前只是一个客户端与服务器联系，无法两个一块儿联系。
print("%s -- %s Successful connection" % (str(clientSocket),clientAddress))

while True:
    data = clientSocket.recv(1024)
    print("client：" + data.decode("utf-8"))
    sendData = input("server：")
    clientSocket.send(sendData.encode("utf-8"))







