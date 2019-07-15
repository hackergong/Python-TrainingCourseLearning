
class Person(object):

    def run(self):
        print("run")
    def eat(self,food):
        print("I have eat "+food)

    # 默认存在，但不显示存在
    #构造函数
    def __init__(self,name,age,height,weight):
        #定义属性
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        # print(name,age,height,weight)
        # print("This is init")
        # pass


'''
构造函数：__init__()在使用类创建对象的时候自动调用
注意：如果不显示的写出构造函数，默认会自动添加一个空的构造函数
'''

per = Person("Tom",16,160,80)
print(per.name,per.age,per.height,per.weight)

per1 = Person("jerry",17,170,100)
print(per1.name,per1.age,per1.height,per1.weight)












