
'''
析构函数：__del__()   #释放对象是自动调用



'''
class Person(object):
    def run(self):
        print("run")
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
    def __del__(self):
        print("这里是析构函数")

per = Person("Tom",20,10,40)
#当程序结束，则执行__del__

#释放对象
del per
#对象释放以后不可再访问
# print(per.age)

#在函数里定义的对象，会在函数结束时自动释放，
# 这样可以用来减少内存空间的浪费
def func():
    per2 = Person("aa",1,1,1)
func()

while 1:
    pass





