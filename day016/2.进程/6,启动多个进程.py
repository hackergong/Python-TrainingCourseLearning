from multiprocessing import Pool #进程池
import os,time,random

def run(name):
    print("子进程%d启动--%s" % (name,os.getpid()))
    start = time.time()
    time.sleep(random.choice([1,2,3]))
    end = time.time()
    print("子进程%d结束--%s---耗时%0.2f" % (name,os.getpid(),end-start))

if __name__ == "__main__":
    print("父进程启动")

    #创建多个进程
    #Pool 进程池,默认大小是CPU核心数，数字表示可以同时指向的进程数量（我的电脑逻辑处理器有4个）
    Pp = Pool()
    for i in range(4):
        #创建进程，放入进程池统一管理
        Pp.apply_async(run,args=(i,))
    #在调用join之前，必须先调用close，调用close之后就不能再继续添加新的进程
    Pp.close()
    #进程池对象调用join，会等待进程池中所有的子进程结束完毕后再执行父进程
    Pp.join()



    print("父进程结束")





































