
import  pymysql

# db = pymysql.connect("localhost","root","tracy","eddy")
db = pymysql.connect("172.18.81.188","root","tracy","eddy")
#创建一个cursor对象
cursor = db.cursor()

#更新语句
sql = 'update bankcard set money=2000 where id=1'
try:
    cursor.execute(sql)
    db.commit() #提交事务
except:
    #如果提交失败，回滚到上一次数据
    db.rollback()


#断开
cursor.close()
db.close()

