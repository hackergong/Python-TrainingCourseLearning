'''

两个线程同时工作，一个存钱，一个取钱

#阻止了多线程的并发执行，包含锁的某段代码实际上只能以单线程模式执行，所以效率大大降级了。
#由于可以存在多个锁，不同线程持有不同的锁，并试图获取其他的锁，可能造成死锁，导致多个线程挂起，只能靠操作系统强制关闭

'''
import threading
import time

lock = threading.Lock()

num = 10
def run(n):
    global num
    for i in range(1000000):
    # 锁定
    #确保了这段代码只能由一个线程从头到尾的完整执行
        '''
        lock.acquire()
        try:
            num = num + n
            num = num - n
        finally:
            #解锁
            lock.release()
        '''
    # 与上面代码功能相同，with lock 可以自动上锁与解锁说
        with lock:
            num = num + n
            num = num - n


if __name__ == "__main__":
    time.perf_counter()
    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(7,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("num = ",num)
    print("%0.2f" % (time.perf_counter()))



























