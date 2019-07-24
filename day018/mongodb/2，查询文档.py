from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId  #用于Id查询

#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.test

#获取结合
collection = db.student

'''
#查询所有文档
res = collection.find()
res = collection.find()
for row in res:
    print(row)
    print(type(row))

#查询部分文档
# $gt 大于
res = collection.find({"age":{"$gt":18}})
for row in res:
    print(row)
    print(type(row))

#统计查询
res = collection.find({"age":{"$gt":18}}).count()
print(res)




#排序
# res =collection.find().sort("age") #升序
res =collection.find().sort("age",pymongo.DESCENDING)
for row in res:
    print(row)



#分页查询
res = collection.find().skip(3).limit(5)
for row in res:
    print(row)


'''
#更具id查询
res = collection.find({"_id":ObjectId("5d37ba69780308a76f2f8fef")})
print(res[0])



#断开
conn.close()





















