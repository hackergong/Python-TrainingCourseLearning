from pymongo import MongoClient

#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.test

#获取结合
collection = db.student


#replace_one,update_one,update_many
collection.update_one({"name":"lilie"},{"$set":{"age":25}})






#断开
conn.close()





















