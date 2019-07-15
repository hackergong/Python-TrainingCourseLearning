
def sayGood():
    print("tracy is a good1 man")

def sayHello():
    print("tracy is a nice1 man")

def sayHandsome():
    print("tracy is a handsome1 man")
#每一个模块都有一个__name__属性，当其值等于“__main__”时，
#表明该模块自身在执行

#当前文件如果为程序入口文件，则__name__属性的值为__main__d
if __name__ == "__main__":
    print(print("this is a tracy3.py"))
else:
    print(__name__)#输出该文件名