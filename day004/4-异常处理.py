'''
需求：当程序遇到问题时不让程序结束，而越过错误继续向下执行

'''

'''
try.....except....else
格式：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
..........
except 错误码 as e:
    语句n
else:
    语句e

注意：else语句可有可无

作用：检测try语句块中的错误，从而让except语句捕获错误并处理

逻辑：当程序执行到try-except-else语句时
1,如果当try“语句t”执行出现错误，会匹配第一个错误码，如果匹配上就执行
    对应的“语句”
2.如果try“语句t”执行没有错误，没有匹配的异常，错误将会被提交到上一层的
    try语句或者到程序的最上层
3.如果try“语句t”执行没有错误，执行else下的“语句e”(你得有else)

'''


##第一种模式
# try:
#     print(3/0)
# except NameError as e:
#     print("no such the varoable")
# except ZeroDivisionError as e:
#     print("除数为0了")
# else:
#     print("code no problemm")
#
# print("********")


##第二种模式
#python 错误代码
#使用except，而不适用任何的错误类型
# try:
#     #print(4/0)
#     print(num)
# except:
#     print("程序出现异常")


##第三种模式
#使用except带着多种异常
'''
try:
    print(5/0)
except (NameError,ZeroDivisionError):
    print("出现了NameError或ZeroDivisionError")

'''

#异常特殊的地方
'''
BaseException  所有异常的基类
1.错误其实是class类，所有的错误都继承自BaseException，所以
在捕获的时候，它捕获了该类的错误，还把子类一网打尽
2.跨越多层调用

'''
try:
    print(5/0)
except BaseException as e:
    print("异常")
except ZeroDivisionError as e:
    print("异常2")

#内存的错误无法跳过
#2.跨越多层调用，main调用了func2，func2调用了func1，
# func1出现错误被捕获
def func1(num):
    print(1/num)
def func2(num):
    func1(num)
def main():
    func2(0)
try:
    main()
except ZeroDivisionError as e:
    print("****")













