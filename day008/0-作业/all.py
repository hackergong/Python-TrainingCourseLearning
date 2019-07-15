import time
#子弹夹
class bulletBox(object):
    def __init__(self,count):
        self.bulletcount = count
        print("一共有子弹%d发" % (self.bulletcount))

#枪
class Gun(object):
    def __init__(self,bulletbox):
        self.bulletbox = bulletbox
    def shoot(self):
        if self.bulletbox.bulletcount == 0:
            print("没有子弹了")
        else:
            self.bulletbox.bulletcount -= 1
            print("剩余%d发" % (self.bulletbox.bulletcount))

#人
class Person(object):
    #属性
    def __init__(self,gun):
        self.gun = gun
    #方法/行为
    def fire(self):
        self.gun.shoot()
    def fillBullet(self,fillcount):
        self.gun.bulletbox.bulletcount = fillcount

bulletbox = bulletBox(5)
gun =  Gun(bulletbox)
per = Person(gun)
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
time.sleep(3)
per.fillBullet(2)
per.fire()
per.fire()














