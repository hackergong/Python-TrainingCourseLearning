
class Person(object):
    #这里的属性实际上属于类属性(用类名来调用)
    name = "person"
    def __init__(self,name):
        pass
        #对象属性
        self.name = name

# print(Person.name)
per = Person("tom")
per.name = "aaaa"
#对象属性的优先级高于类属性
# print(per.name)
# print(Person.name)
#动态的给对象添加对象属性
# per.age = 19  #只针对当前对象生效，对于类创建的其他对象没有作用
# print(Person.name)
# per2 = Person("lilei")
#print(per2.age)  #没有age属性


#删除对象中的name属性,在调用会使用到同名的类属性
del per.name
print(per.name)

#注意：以后千万不要将对象属性与类属性重名，因为对象属性会屏蔽掉类属性，但是当删除对象属性后，
#再使用又能使用类属性


































