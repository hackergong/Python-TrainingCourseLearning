def A():
    print("A--start")
    B()
    print("A--end")


def B():
    print("B--start")
    C()
    print("B--end")
def C():
    print("C--start")

    print("C--end")

A()

'''
A--start
B--start
C--start
C--end
B--end
A--end
'''

def A():
    print(1)
    print(2)
    print(3)
def B():
    print("x")
    print("y")
    print("z")

#但协程的特点在于是一个线程执行
#与线程相比，协程的执行效率极高，因为只有一个线程，也不存在同时写变量的冲突，在协程中共享资源不加锁，只需要判断状态
#Python对协程的支持是通过generator实现的
