'''
装饰器
'''


#1
'''
def func1():
    print("tracy is a good man")
def outer():
    print("1")
    func1()
outer()
'''

#2
'''
def func1():
    print("tracy is a good man")
def outer(func):
    print("2")
    func()

func5 = outer(func1)
outer(func1)
'''

#3
'''
#将func1赋给outer的形参，然后函数体内调用func(){即调用func1函数}
def func1():
    print("tracy is a good man")
def outer(func):
    def inner():
        print("3")
        func()
    return inner
#f是函数func1的加强版本，用inner对func1进行装饰。
f = outer(func1)
f()
# 将inner赋给f，则f具有了该函数的功能，可输出print("3"),以及func()
'''


#4
'''
# 复杂装饰器
# 当say函数不能够修改时，则需要使用装饰器
def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner
# @的使用将装饰器应用到函数
# @在python2.4支持使用@符号
@outer    #say = outer(say)
def say(age):
    print("Tracy is a %d years old" % (age))
# say_dec = outer(say)
# 直接使用封闭的函数名，而不需要使用装饰器的函数名
say(-10)
'''

#5
##通用装饰器
'''
def outer(func):
    def inner(*args,**kwargs):#可以传任意参数
        #添加修饰的功能
        print("&&&&&&&")
        func(*args,**kwargs)
    return inner

@outer     #say = outer(say)
def say(name,age):
    print("my name is %s,I'm %d years old" % (name,age))

say("tracy",18)
'''
#函数的参数理论上是无限制的，但实际上不要超过6-7个
#say函数不允许修改，所以使用outer作为装饰器来添加一个print
