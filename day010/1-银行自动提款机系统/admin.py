import time

class Admin(object):
    #类变量
    admin = "1"
    passwd = "1"

    def printAdminView(self):
        print("*******************************************************")
        print("*                                                     *")
        print("*                                                     *")
        print("*               欢迎登录银行系统                       *")
        print("*                                                     *")
        print("*                                                     *")
        print("*******************************************************")

    def printsysFunctionView(self):
        print("*******************************************************")
        print("*      开户(1)                       查询(2)            *")
        print("*      取款(3)                       存款(4)            *")
        print("*      转账(5)                       改密(6)            *")
        print("*      锁定(7)                       解锁(8)            *")
        print("*      补卡(9)                       销户(10)           *")
        print("*                      退出(quit)                       *")
        print("*******************************************************")

    def adminOption(self):
        inputAdmin = input("请输入管理员账号：")
        if self.admin != inputAdmin:
            print("账号输入错误！")
            return -1  ##结束程序，主函数main也会结束
        inputPasswd = input("请输入管理员密码：")
        if self.passwd != inputPasswd:
            print("密码输入有误！")
            return -1  #结束程序，主函数main也会结束

        #能执行到这儿，说明账号密码正确
        print("操作成功，请稍等...")
        time.sleep(2)
        return 0




































