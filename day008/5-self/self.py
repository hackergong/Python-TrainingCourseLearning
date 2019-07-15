'''
self 代表类的实例，而非类

哪个对象调用方法，那么该方法中的self就代表哪个对象

self.__class__  代表类名
'''

class Person(object):
    def run(self):
        print("run")
        #代表类名
        print(self.__class__)
        p = self.__class__("tt",30,10,40)
        print(p)
    def eat(self,food):
        print("I have eat "+food)
    # 默认存在，但不显示存在
    def say(self):#self代表类的实例
        #下面方法中self代表per1对象
        print("Hello! my name is %s,I am %d years old" % (self.name,self.age))#
    #self不是关键字，其他标识符也可以，但是统一用self
    def play(self):
        print("play"+self.name)
    def __init__(self,name,age,height,weight):
        #定义属性
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age


per1 = Person("tom",20,160,80)
per1.say()
per1.run()
per2 = Person("kindy",16,166,90)
per2.say()