'''
特点：把数据拼接到请求路径的后，传递给服务器
优点：速度快
缺陷：承载的数据量小，不安全

'''


import urllib.request

url ="http://www.Alibaba.com/robots.txt"
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")
print(data)
print(type(data))

#网络传输的是json文件，将json的字符串转为python的list或dict类型
#jsonView


































