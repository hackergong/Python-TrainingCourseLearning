class Person(object):
    #创建对象的时候自动咨执行
    def __init__(self,name,age,height,weight,money):
        #定义属性
        self.name = name
        self.height = height
        self.weight = weight
        self.__age__ = age
        #双下划线变为不可修改内部属性
        self.__money = money  #Person__money
    def run(self):
        print(self.__money)
    #通过内部的方法，取修改私有属性
    #通过自定义的方法时间对私有属性的赋值和取值
    def setMoney(self,money):
        #数据过滤
        if money < 0:
            money = 0
        self.__money = money
    def getMoney(self):
        return self.__money

per = Person("tom",20,70,29,10000)
# per.age = 10
# print(per.age)

#如果要让内部的属性不被外部直接访问,在属性前加两个下划线（__）
#在Python中如果在属性前加两个下划线，那么这个属性就变成私有属性

# per.__money = 0
# print(per.__money)  #此处仍然能打印，因为动态语言可以随时添加属性
                    #这是因为添加了一个per.__money的属性

# print(per.__money) #不可通过外部直接属性
# per.run()

per.setMoney(10000)
print(per.getMoney())

#per.__Money
#会报错，不能直接访问私有属性的原因，是因为Python解释器把__Money变成了
#_Person__money，仍然可以使用_Person__money去访问，但是强烈不建议，
#不同的解释器可能存在的变量名不一致
per._Person__money = 1
print(per.getMoney())

#在Python中，__XX__ 属于特色变量，可以直接访问
#self.__age__ = age
print(per.__age__)

#在Python中，_XXXX  变量，这样的实例变量，外部也是可以访问的。
#按照约定的规则，当我们看到这样的变量，意思是：虽然我可以被访问，
#请把我视为私有变量。不要直接访问我。





















































