from card import Card
from user import User
import random

class ATM(object):
    def __init__(self,allUsers):
        self.allUsers = allUsers #卡号-用户

    #开户
    def createUser(self):
        #目标：向用户字典中添加一对键值对(卡号-用户)，用户为一个对象
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号码：")
        phone = input("请输入您的电话号码：")
        prestoreMoney = int(input("请输入预存款金额："))
        if prestoreMoney < 0 :
            print("预存款输入有误！开户失败...")
            return -1
        onePasswd = input("请设置密码：")
        #验证密码
        if not self.checkPasswd(onePasswd):
            print("密码输入错误！开户失败...")
            return -1  #结束while，下面的不执行
        #所有需要的信息就全了
        #生成卡号
        cardStr = self.randomCardId()
        #建立card对象
        card = Card(cardStr,onePasswd,prestoreMoney)
        #建立用户对象
        user = User(name,idCard,phone,card)
        #将user作为card的子类，user继承了card的所有属性
        #存字典 将卡号作为key，user作为value
        #生成用户和卡的信息
        self.allUsers[cardStr]=user
        print("开户成功，请牢记卡号：%s" % (cardStr))



    #查询
    def searchUserInfo(self):
        cardNum = input("请输入您的卡号：")
        #验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！查询失败")
            return -1

        #判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定，请解锁后再进行其他操作")

        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！该卡已被锁定，请解锁后再进行其他操作失败...")
            user.card.cardLock = True
            return -1
        #不适用self.user.card.cardId,因为已经调用了user，直接可以使用
        print("账号：%s  余额：%d" % (user.card.cardId,user.card.cardMoney))


    #取款
    def getMoney(self):
        cardNum = input("请输入您的卡号：")
        #验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！取款失败")
            return -1

        #判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定，请解锁后再进行其他操作")
            return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！该卡已被锁定，请解锁后再进行其他操作失败...")
            user.card.cardLock = True
            return -1
        #取款验证
        money = int(input("请输入取款金额:"))
        if money > user.card.cardMoney:
            print("余额不足，取款失败...")
            return -1
        if money <= 0:
            print("输入错误，取款失败...")
            return -1
        #取款成功
        user.card.cardMoney -= money
        print("取款成功！！余额：%d" % (user.card.cardMoney))

    #存款
    def saveMoney(self):
        cardNum = input("请输入您的卡号：")
        #验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！取款失败")
            return -1

        #判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定，请解锁后再进行其他操作")

        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！该卡已被锁定，请解锁后再进行其他操作失败...")
            user.card.cardLock = True
            return -1
        #存款验证
        money = int(input("请输入存款额:"))
        # if money > user.card.cardMoney:
        #     print("余额不足，取款失败")
        #     return -1
        #存款成功
        user.card.cardMoney += money
        print("存款成功！！余额：%d" % (user.card.cardMoney))


    #转账
    def transferMoney(self):
        cardNum1 = input("请输入您的卡号：")
        #验证是否存在该卡号
        user1 = self.allUsers.get(cardNum1)
        if not user1:
            print("该卡号不存在！！转失败")
            return -1

        #判断是否锁定
        if user1.card.cardLock:
            print("该卡已被锁定，请解锁后再进行其他操作")
            return -1

        #验证密码
        if not self.checkPasswd(user1.card.cardPasswd):
            print("密码输入错误！！该卡已被锁定，请解锁后再进行其他操作失败...")
            user1.card.cardLock = True
            return -1
        cardNum2 = input("请输入您要转的卡号：")
        #验证是否存在该卡号
        user2 = self.allUsers.get(cardNum2)
        if not user2:
            print("该卡号不存在！！转失败")
            return -1

        #判断是否锁定
        if user2.card.cardLock:
            print("该卡已被锁定，请解锁后再进行其他操作")

        #验证密码
        if not self.checkPasswd(user2.card.cardPasswd):
            print("密码输入错误！！该卡已被锁定，请解锁后再进行其他操作失败...")
            user2.card.cardLock = True
            return -1
        #转账金额
        money = int(input("请输入转账金额:"))
        if money > user1.card.cardMoney or money < 0:
            print("转账失败，请输入正确的金额")
            return -1
        #转账成功
        user2.card.cardMoney += money
        user1.card.cardMoney -= money
        print("转账成功！！用户%s 余额：%d，用户%s 余额：%d" % (cardNum1,user1.card.cardMoney,cardNum2,user2.card.cardMoney))

    #改密
    def changePassed(self):
        cardNum = input("请输入您的卡号：")
        #验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！查询失败")
            return -1
        #判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定，请解锁后再进行其他操作")
            return
        #验证身份证号
        tempIdCard = input("请输入身份证号：")
        if tempIdCard != user.idCard:
            print("身份证输入错误，验证失败")
            return -1
        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！该卡已被锁定，请解锁后再进行其他操作失败...")
            user.card.cardLock = True
            return -1
        tempPasswd=[]
        for i in range(2):
            tempPasswd.append(input("请输入新密码:"))
        if not tempPasswd[0] == tempPasswd[1] :
            return -1
        user.card.cardPasswd = tempPasswd[1]
        print("密码修改成功！！！")


    #锁定
    def lockUser(self):
        cardNum = input("请输入您的卡号：")
        #验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！锁定失败")
            return -1
        if user.card.cardLock:
            print("该卡已经被锁定，请解锁后再使用其他功能...")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！锁定失败...")
            return -1
        tempIdCard = input("请输入身份证号：")
        if tempIdCard != user.idCard:
            print("身份证输入错误，验证失败")
            return -1
        #锁它
        user.card.cardLock = True
        print("锁定成功！！")

    #解锁
    def unlockUser(self):
        cardNum = input("请输入您的卡号：")
        #验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！解锁失败")
            return -1
        if not user.card.cardLock:
            print("该卡没有锁定！！无需解锁...")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！解锁失败...")
            return -1
        tempIdCard = input("请输入身份证号：")
        if tempIdCard != user.idCard:
            print("身份证输入错误，解锁失败")
            return -1
        #解锁它
        user.card.cardLock = False
        print("解锁成功！！")


    #补卡
    def newCard(self):
        cardNum = input("请输入您的卡号：")
        #验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！查询失败")
            return -1
        #判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定，请解锁后再进行其他操作")
            return
        #验证身份证号
        tempIdCard = input("请输入身份证号：")
        if tempIdCard != user.idCard:
            print("身份证输入错误，验证失败")
            return -1
        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！该卡已被锁定，请解锁后再进行其他操作失败...")
            user.card.cardLock = True
            return -1
        tempUserCardMoney=user.card.cardMoney
        self.allUsers.pop(cardNum)
        print("-----请重新输入您的信息-----")
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号码：")
        phone = input("请输入您的电话号码：")
        prestoreMoney = tempUserCardMoney
        onePasswd = input("请设置密码：")
        #验证密码
        if not self.checkPasswd(onePasswd):
            print("密码输入错误！补卡失败...")
            return -1
        cardStr = self.randomCardId()
        card = Card(cardStr,onePasswd,prestoreMoney)
        user = User(name,idCard,phone,card)
        self.allUsers[cardStr]=user
        print("补卡成功,新卡号为：%s " %(cardStr))
    #销户
    def killUser(self):
        cardNum = input("请输入您的卡号：")
        #验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！转失败")
            return -1
        #判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定，请解锁后再进行其他操作")
            return -1
        #验证身份证
        tempIdcard = input("请输入身份证号：")
        if tempIdcard != user.idCard:
            print("身份证输入错误，验证失败！")
            return -1
        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！该卡已被锁定，请解锁后再进行其他操作失败...")
            user.card.cardLock = True
            return -1
        self.allUsers.pop(cardNum)
        print("用户 %s 已经被注销" % (cardNum))

    #验证密码
    def checkPasswd(self,realPasswd):
        for i in range(3):
            tempPasswd = input("请输入密码:")
            if tempPasswd == realPasswd:
                return True
        return False
    #生成卡号
    def randomCardId(self):
        while True:
            str = ""
            for i in range(4):
                ch = chr(random.randrange(ord('0'),ord('9')+1))
                str += ch
            #判断是否重复
            if not self.allUsers.get(str):
                return str














































