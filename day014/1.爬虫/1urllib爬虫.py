'''
百度的站长工具
'''

import urllib.request

#向指定的url地址发起请求，并返回服务器响应的数据(文件的对象)
# response = urllib.request.urlopen("http://www.baidu.com")

'''
#1
#读取文件的全部内容，会把读取到的数据赋值给一个字符串变量
# data = response.read()
# data = response.read().decode("utf-8")  #可以查看以utf-8形式，但是不能写入
print(data)
print(type(data)) #bytes是字节类型，可以以二进制类型写入
# data =data.encode(data)
'''





'''
#2
#读取一行
# data = response.readline()
#读取文件的全部内容，会把读取到的数据赋值给一个列表变量
data =response.readlines()
print(data)
print("\n")
print(type(data))
print(len(data))
print(type(data[100])) #字节类型
print(type(data[100].decode("utf-8"))) #解码为字符串类型
'''


'''
#3
#将爬取到的网页写入文件
data = response.read()
path = r"G:\python_learn\pycharm_learn\pythonlearn\day014\file\file1.html"
with open(path,"wb") as f:
    f.write(data)
'''


'''
#4
# data = response.read()
#response 属性
#返回当前环境的有关信息
print(response.info())

#返回状态码
print(response.getcode())  #200  成功访问
# if response.getcode() == 200 or response.getcode() == 304:
    #处理网页信息
    # pass

#返回当前正在爬取的url地址
print(response.geturl())
'''


'''
#5
url = r"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=97011255_hao_pg&wd=%E5%8D%83%E5%B3%B0%E6%95%99%E8%82%B2&rsv_pq=9cd08caa00081b17&rsv_t=84dftstxYHl77KxkBSr9RrjHPjMAVlglQg%2FOGrsOZ%2BHFZmIj3T31qzM71YJwnOhjnef8pmb5&rqlang=cn&rsv_enter=1&rsv_sug3=25&rsv_sug1=5&rsv_sug7=101&rsv_sug2=0&rsv_dl=tb&inputT=8357&rsv_sug4=12532"

# url = "http://www.baidu.com"

#解码
newurl = urllib.request.unquote(url)
print(newurl)
#编码
print("\n")
newurl2 = urllib.request.quote(newurl)
print(newurl2)
'''




