from person import Person

class Worker(Person):
    #实现自己的init，应该有name,age
    def __init__(self,name,age,money):
        super(Worker,self).__init__(name,age,money)
        #调用父类中的__init__
        #super
