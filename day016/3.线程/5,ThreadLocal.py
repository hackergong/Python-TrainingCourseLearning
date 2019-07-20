import threading

num = 10
#创建一个全局的ThreadLocal对象
#每个线程有独有的存储空间，每个线程对ThreadLocal对象都可以读写，但是互不影响
local = threading.local()
def run(x,n):
        x = x + n
        x = x - n
        return x

def func(n):
    local.x = num
    for i in range(1000000):
        r = run(local.x,n)
    print(r)
    print("%s-%d" % (threading.current_thread().name,local.x))



if __name__ == "__main__":
    t1 = threading.Thread(target=func,args=(6,))
    t2 = threading.Thread(target=func,args=(7,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("num = ",num)

#作用：为每个线程绑定一个数据库，或者HTTP请求，或者用户身份









