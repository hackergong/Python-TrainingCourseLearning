class Person(object):
    name = "xia"
    age = 9
    height = 2
    weight = 1
    def run(self):
        print("run")
    def eat(self,food):
        print("I have eat "+food)
    def openDoor(self):
        print("open the door")
    def fillEle(self):
        print("I have filled it")
    def closeDoor(self):
        print("I have colsed the door")

per1 = Person()

'''
访问属性
格式：对象名.属性名
赋值：对象名.属性名 = 新值
'''

per1.name = "tom"
per1.age = 18
per1.height = 170
per1.weight = 80
print(per1.name,per1.age,per1.height,per1.weight)

'''
访问方法
格式：对象名.方法名(参数列表)  #必须要有小括号
#self不需要传参数
'''
per1.openDoor()
per1.fillEle()
per1.closeDoor()

per1.eat("apple")

#问题：目前来看Person的所有对象属性都是一样的
per2 = Person()
print(per2.age)


#






































