from pymongo import MongoClient

#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.test

#获取结合
collection = db.student


#delete_one,delete_many
# collection.delete_one({"name":"lilie"})

#作业作业作业：：：全部封装






#断开
conn.close()





















