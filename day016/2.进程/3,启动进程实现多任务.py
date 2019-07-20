'''
multiprocessing  库
跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象

'''

from multiprocessing import Process
from time import sleep
import os
#子进程
def run(str):
    while True:
        #os.getpid() 获取当前进程ID号
        #os.getppid() 获取当前进程的父进程ID号
        print("tracy is a %s man---%s---%s" % (str,os.getpid(),os.getppid()))
        sleep(2.5)

if __name__ == "__main__":
    print("主进程启动")
    #创建子进程
    #targer说明进程执行的任务 #args 后面是一个元组，里面只有一个元素的时候需要加逗号
    #可在任务管理器-详细信息中找打PID号
    p = Process(target=run,args=("nice",))
    #启动进程
    p.start()
    while True:
        print("tracy is a good man--%s" %(os.getpid()))
        sleep(2)

