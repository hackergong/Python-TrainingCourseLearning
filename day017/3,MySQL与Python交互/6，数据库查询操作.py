import  pymysql

# db = pymysql.connect("localhost","root","tracy","eddy")
db = pymysql.connect("172.18.81.188","root","tracy","eddy")
#创建一个cursor对象
cursor = db.cursor()

#检查表是否存在，如果存在则删除
# cursor.execute("drop table if exists bankcard")

sql = 'select * from bankcard where money>400'
try:
    cursor.execute(sql)

    reslist = cursor.fetchall()
    for row in reslist:
        print("%d--%d" % (row[0],row[1]))
except:
    #如果提交失败，回滚到上一次数据
    db.rollback()


#断开
cursor.close()
db.close()

