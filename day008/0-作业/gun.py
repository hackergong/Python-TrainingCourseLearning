class Gun(object):
    def __init__(self,bullet):
        self.bullet = bullet
    def shoot(self):
        if self.bullet.bulletCount == 0:
            print("没有子弹")
        else:
            self.bullet.bulletCount -= 1
            print(("剩余子弹：%d") % (self.bullet.bulletCount))