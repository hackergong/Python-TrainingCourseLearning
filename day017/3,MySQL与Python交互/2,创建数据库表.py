import  pymysql

# db = pymysql.connect("localhost","root","tracy","eddy")
db = pymysql.connect("172.18.81.188","root","tracy","eddy")
#创建一个cursor对象
cursor = db.cursor()


#建表
sql = 'create table bankcards(id int auto_increment primary key,money int not null)'
cursor.execute(sql)



#断开
cursor.close()
db.close()

