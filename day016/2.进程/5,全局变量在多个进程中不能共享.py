from multiprocessing import Process
from time import sleep

num = 100

def run():
    print("子进程开始")

    global num  #相当于创建num= 100
    num += 1
    print(num)
    print(id(num))

    print("子进程结束")



if __name__ == "__main__":
    print("父进程开始")

    p = Process(target=run)
    p.start()
    p.join()

    print("父进程结束 %s   %s" % (num,id(num)))


#子进程和父进程的num是不一样的，每个进程都有自己的数据段，代码段，是完全不同的两个地址
#在子进程中修改全局变量对父进程的全局变量没有影响


















