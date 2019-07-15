'''
人
类名：Person
属性：姓名，身份证号，电话号，卡
行为：(开户，查询，取款，存款，转账，改密码，锁定，解锁，补卡，销户，退出)



卡
类名：Card
属性：卡号，密码，余额
行为：


银行
类名：Bank
属性：用户列表，提款机
行为：


提款机
类名：ATM
属性：用户字典
行为：开户，查询，取款，存款，转账，改密码，锁定，解锁，补卡，销户


管理员
类名：admin
属性：
行为：管理员界面，系统功能界面，管理员验证

'''
from admin import Admin
import time
from atm import ATM
import pickle
import os



def main():
    #界面对象
    admin = Admin()

    #管理员开机
    admin.printAdminView()
    #python中0和空值表示False，其它表示True
    #判断返回值是否是-1，如果是-1，则返回-1.如果是0，则不会执行
    if admin.adminOption():
        return -1

    #提款机对象
    filePath = os.path.join(os.getcwd(),"allusers.txt")
    f = open(filePath,"rb")
    allUsers = pickle.load(f)
    print(allUsers)
    # allUsers = {}
    atm = ATM(allUsers)

    while True:
        admin.printsysFunctionView()
        #死循环等待用户的操作
        option = input("请输入您的操作：")
        if option == "1":
            #开户
            atm.createUser()
        elif option == "2":
            #查询
            atm.searchUserInfo()
        elif option == "3":
            #取款
            atm.getMoney()
        elif option == "4":
            #存款
            atm.saveMoney()
        elif option == "5":
            atm.transferMoney()
        elif option == "6":
            #改密
            atm.changePassed()
        elif option == "7":
            #锁定
            atm.lockUser()
        elif option == "8":
            #解锁
            atm.unlockUser()
        elif option == "9":
            #补卡
            atm.newCard()
            #重新生成新的卡号
        elif option == "10":
            atm.killUser()
            #删除allUsers的键值对
        elif option == "quit":
            #python中0和None表示False，其它值表示True
            if not admin.adminOption(): #返回一个0，not 0 就是True。

                #将当前系统中的用户信息保存到文件中
                f = open(filePath,"wb")
                pickle.dump(atm.allUsers,f)
                f.close()
                return -1


        time.sleep(1)


if __name__ ==  "__main__":
    main()







































































