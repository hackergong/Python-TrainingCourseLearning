class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getAge(self):
        return  self.age #self.v是属性，所以用[]来获取v的值

