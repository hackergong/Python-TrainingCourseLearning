from person import Person
from bulletbox import BulletBox
from gun import Gun

#弹夹
bulletBox = BulletBox(5)
#bulletBox 是一个对象
print(bulletBox.bulletCount)
#枪
gun = Gun(bulletBox)

#人
per = Person(gun)
per.fire()
per.fire()
per.fire()

#per.fire.gun.shoot.bulletBox.bulletCount








'''
人
类名：Perso
属性：gun
行为：fire

枪
类名：Gun
属性：bulletBox
行为：Shoot

弹夹
类名：BulletBox
属性：bulletCount
行为：
'''















# class Person():
#     def __init__(self,name,age,num = 2):
#         self.name = name
#         self.age = age
#         self.num = num
#     def Gum
#     def Fire(self):
#         self.num -= 1
#         if self.num==0:
#             print("子弹用尽" )
#     def __str__(self):
#         return "%s-%d" % (self.name,self.age)
#
#
#
# per = Person("tom",20,1)
# per.Gum()


