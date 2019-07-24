from pymongo import MongoClient

#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.test

#获取结合
collection = db.student

#添加文档
#插入一个
# collection.insert_one({"name":"lili","age":19,"gender":1,"address":"北京","isDelete":0})
#插入多个
collection.insert_many([{"name":"baidu","age":12,"gender":1,"address":"北京","isDelete":0},{"name":"souhu","age":17,"gender":0,"address":"北京","isDelete":0},{"name":"aiqiyi","age":10,"gender":0,"address":"广东","isDelete":0}])
#断开
conn.close()





















