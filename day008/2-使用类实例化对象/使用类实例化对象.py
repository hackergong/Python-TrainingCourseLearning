class Person(object):
    name = ""
    age = 9
    height = 0
    wight = 0
    def run(self):
        print("run")
    def eat(self,food):
        print("eat"+food)
    def openDoor(self):
        print("open the door")
    def fillEle(self):
        print("I have filled it")
    def closeDoor(self):
        print("I have colsed the door")



'''
实例化对象
格式：对象名 = 类名(参数列表)
注意：没有参数，小括号也不能省略

'''
#实例化一个对象
per1 = Person()
print(per1)
print(type(per1))
print(id(per1))
#<__main__.Person object at 0x036650B0> 即为内存地址

per2 = Person()
print(per2)
print(type(per2))
print(id(per2))
#per1和per2是两个不同的对象






















































