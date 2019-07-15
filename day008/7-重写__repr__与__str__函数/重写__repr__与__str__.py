'''

重写：将函数定义重写写一遍
__str__()：在调用print打印对象时自动调用，是给用户用的，是一个描述对象的方法
__repr__()：是给机器用的，在python解释器里直接敲对象名在回车后调用的方法
                即在命令指示符中使用

注意：在没有str时，且有repr，str=repr


'''
class Person(object):
    #创建对象的时候自动咨执行
    def __init__(self,name,age,height,weight):
        #定义属性
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
    #使用它即可将信息全部显示
    def __str__(self):
       return "%s-%d-%d-%d" %(self.name,self.age,self.height,self.weight)
    # def __repr__(self):
    #     print("This is repr")
per = Person("tom",20,170,44)
print(per.name,per.age,per.height,per.weight)#这样写不是很方便

print(per)
print(per.__str__())

#优点：当一个对象的属性值很多，并且都需要打印，重写了__str__方法后，简化了代码

'''
#作业
人开枪射击子弹

'''














