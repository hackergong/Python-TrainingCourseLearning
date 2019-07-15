
class Person(object):
    def __init__(self,name,age):
        #属性直接对外暴露
        # self.age = age
        #限制访问
         self.__age = age
         self.__name = name
    '''
    def getAge(self):
        return self.__age
    def setAge(self,age):
        if age < 0:
            age = 0
        self.__age = age
    '''
    #方法名为受限制的变量去掉双下划线的
    #
    @property
    def age(self):
        return self.__age
    @age.setter   #去掉下划线.setter
    def age(self,age):
         if age < 0:
            age = 0
         self.__age = age
    @property
    def name(self):
        return self.__name
    @name.setter   #去掉下划线.setter
    def name(self,name):
         self.__name = name



per = Person("tom",18)

#属性直接对外保罗
#不安全，没有数据的过滤
# per.age = -10
# print(per.age)


#使用限制访问，需要自己写set和get方法才能访问
# per.setAge(15)
# print(per.getAge())


per.age = 100  #相当于setAge
print(per.age)   #相当于getAge
#
# per = Person(18)
# print(per.age)
# per.age = 4
# print(per.age)

print(per.name)


#property 可以让你对受限制访问的属性使用点语法

#__age是不能被直接调用的，比如用 per.__age，直接操作是报错的，但是我们
#可以调用set，get等来修改调用其值












