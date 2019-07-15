from student import Student
from worker import Worker
from person import Person
stu = Student("tom",19,1235,110)
print(stu.name,stu.age,stu.stuId)
# stu.stuFunc()

# print(stu.__money) #私有属性无法访问
print(stu.getMoney()) #通过继承过来的公有方法访问私有属性
stu.run()

wor = Worker("jack",10,112)
print(wor.name,wor.age)

per = Person("aa",1,2)
print(per.getMoney())

'''
父类有的私有属性，子类不可直接访问，而是通过父类的方法访问私有属性
'''