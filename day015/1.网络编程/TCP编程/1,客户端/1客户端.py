'''
客户端：创建TCP链接时，主动发起链接的叫做客户端
服务端：接受客户端的链接
'''
#相当于浏览器去访问网站，然后返回数据头和页面
import socket
#1，创建一个socket
#参数1：指定协议 AF_INET(IPV4) 或AF_INET6(IPv6)
#参数2：SOCK_STREAM执行使用面向流的TCP协议
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2，建立连接
#参数：是一个元组，第一个元素为要连接的服务器的IP地址，第二个参数为端口号。地址是一个元组，最后一个数为端口，一般是80
sk.connect(("www.baidu.com",80))

#b为字节码,发送请求，分多次发送
sk.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')

#等待接收数据
data = []
while True:
    #接收数据，每次接收1K的数据
    tempData = sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break

dataStr = (b''.join(data)).decode("utf-8")

#断开连接
sk.close()
# print(dataStr)

headers,HTML = dataStr.split('\r\n\r\n',1)
print(headers)
print(HTML)



































