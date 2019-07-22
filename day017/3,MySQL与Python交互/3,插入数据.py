import  pymysql

# db = pymysql.connect("localhost","root","tracy","eddy")
db = pymysql.connect("172.18.81.188","root","tracy","eddy")

#创建一个cursor对象
cursor = db.cursor()


#插入语句
# sql = 'insert into bankcard values(0,300),(0,400),(0,500),(0,600)'
sql = 'insert into bankcards values(0,200)'
try:
    cursor.execute(sql)
    db.commit() #提交事务
except:
    #如果提交失败，回滚到上一次数据
    db.rollback()


#断开
cursor.close()
db.close()

