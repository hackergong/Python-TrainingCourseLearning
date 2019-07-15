from types import MethodType

#创建一个空类
class Person(object):
    #限制添加属性,只能添加的属性
    __slots__ = ("name","age")

per = Person()
#动态添加属性，这体现了动态语言的特点(灵活)
per.name = "tom"
print(per.name)
#动态添加方法
'''
def say(self):
    print("my name is " + self.name)
per.speak = say
per.speak()
'''
def say(self):
    print("my name is " + self.name)
#引入 from types import MethodType
# per.speak = MethodType(say,per)
# per.speak()
#看一下偏函数

#思考：如果我们想要限制实例的属性怎么办？
#比如：只允许给对象添加name,age,height,weight属性。


#解决：定义类的时候，定义一个特殊的属性(__slots__),可以限制动态添加的属性

per.height = 170
print(per.height)



























