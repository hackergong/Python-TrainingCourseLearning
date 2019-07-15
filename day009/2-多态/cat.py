from animal import Animal

class Cat(Animal):
    def __init__(self,name):
        # self.name = name
        super(Cat,self).__init__(name)
        # Animal.__init__(self,name)
    # def eat(self):
    #     print(self.name + "吃")

