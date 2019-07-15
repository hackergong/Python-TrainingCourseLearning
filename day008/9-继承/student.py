from person import Person

class Student(Person):
    #实现自己的init，应该有name,age
    def __init__(self,name,age,money,stuId):
        #调用父类中的__init__
        super(Student,self).__init__(name,age,money)
        #super，调用父类中的init，让父类中的self代表子类的对象，而(student,self)这个self代表子类对象
    #子类可以有自己独有的属性
        self.stuId = stuId
    #无法输出钱
    def stuFunc(self):
        print(self.__money)