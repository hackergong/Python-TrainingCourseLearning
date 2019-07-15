'''
特点：将参数进行打包，单独传输
优点：承载数据量大，安全(当对服务器数据进行修改时建议使用post)
缺点：速度慢

'''

import urllib.request
import urllib.parse

url = "http://www.ahnu.edu.cn"
#将要发送的数据合成一个字典
#字典的键值去网址里取找，一般为input标签的name属性的值
data = {
    "username":"admin",
    "passwd":"123456"
}

#对要发送的数据进行打包,记住编码
postData = urllib.parse.urlencode(data).encode("utf-8")
#创建请求体
req = urllib.request.Request(url,data=postData)
# req.add_header("")
#请求
req.add_header("User-Agent","Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/54.0.2840.99 Safari/537.36")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))




'''
GET POST两种请求方法的区别
最直观的区别就是GET把参数包含在URL中，POST通过request传递参数

GET在浏览器回退时是无害的，而POST会再次提交请求
GET产生的URL地址可以被Bookmark，而POST不可以
GET请求会被浏览器主动cache，而POST不会，除非手动设置
GET请求只能进行URL编码，而POST支持多种编码方式
GET请求参数会被完整保留在浏览器历史记录里，而POST中的参数不会被保留
GET请求在URL中传递的参数是有长度限制的，而POST没有
对参数的数据类型，GET只接受ASCLL字符，而POST没有限制
GET比POST更不安全，因为参数直接暴露在URL上，所以不能用来传递敏感信息
GET参数通过URL传递，POST放在Request中

GET请求时，HTTP规定设置标签GET，要求把数据放在URL中，以方便记录
POST请求时，HTTP规定设置标签POST，把数据放在post内，

不同浏览器发起请求和服务器接收请求就是不同的运输公司，大多数浏览器都会限制url长度在2k个字节，大多数服务器处理64k大小的url
GET产生一个TCP数据包，浏览器会把http header和data一并发送出去，服务器响应200（返回数据）

POST产生两个TCP数据包，浏览器先发送header，服务器响应100，continue，浏览器再发送data，服务器响应200（返回数据）

GET只需一辆汽车送到，
POST需要先敲门，后送货


'''














