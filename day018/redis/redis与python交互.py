'''
pip install redis




'''


import redis

# print(dir(redis))
#连接
r = redis.StrictRedis(host="localhost",port=6379,password="tracy")

#方法1：根据数据类型的不同，调用相应的方法
#写
# r.set("p0","good")

#读
# print(r.get("p0").decode("utf-8"))


#方法2
#pipline 缓冲多条命令，然后依次执行，减少服务器-客户端之间的TCP数据包

pipe = r.pipeline()

pipe.set("p3","nice")
pipe.set("p4","handsome")

pipe.execute()

print(pipe.get("p3"))




# 用作缓冲

'''
12306
客户端：输入账号密码

到

服务器：传输到服务器

服务器到redis先验证

redis：key：value  账号：密码，在redis中存储经常访问的

若redis中无账号缓冲，则在mysql中寻找，

mysql


'''

'''
前端

读取redis中的用户名，

后端





'''














