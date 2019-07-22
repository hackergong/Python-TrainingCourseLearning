import pymysql

class MySqlAll():
    def __init__(self,host,user,passwd,dbName):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbName = dbName

    def __connect(self):
        self.db = pymysql.connect(self.host,self.user,self.passwd,self.dbName)
        self.cursor = self.db.cursor()

    def __close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self,sql):#sql为要执行的sql语句
        res = None
        try:
            self.__connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.__close()
        except:
            print("查询失败")
        return res

    def get_all(self,sql):
        res = ()
        try:
            self.__connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.__close()
        except:
            print("查询失败")
        return res

    def insert(self,sql):
        return self.__edit(sql)

    def update(self,sql):
        return self.__edit(sql)

    def delete(self,sql):
        return self.__edit(sql)

    def __edit(self,sql):
        count = 0
        try:
            self.__connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.__close()
        except:
            print("提交事务失败")
            self.db.rollback()
        return count