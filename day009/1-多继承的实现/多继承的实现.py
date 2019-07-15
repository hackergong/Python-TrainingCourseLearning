from child import Child


def main():
    c = Child(300,100)
    print(c.money,c.facevalue)
    c.play()
    c.eat()
    #注意：父类中方法名相同，默认调用的是子类在括号中排前面的父类中的方法
    c.func()#继承父亲的func




if __name__ == "__main__":
    main()