import threading,queue,time,random

#生产者

def producer(Id,q):
    while True:
        num = random.randint(0,1000)
        q.put(num)
        print("生产者%d生产了%d数据放入了队列\n" % (Id,num))
        time.sleep(5)
    #任务完成
    q.task_done()


#消费者
def customer(Id,q):
    while True:
        item = q.get()
        if item is None:
            break
        print("消费者%d消费了%d数据\n" % (Id,item))
        time.sleep(4)
    #任务完成
    q.task_done()

if __name__ == "__main__":
    #消息队列
    q = queue.Queue()
    #启动生产者
    for i in range(4):
        threading.Thread(target=producer,args=(i,q)).start()
    #启动消费者
    for i in range(3):
        threading.Thread(target=customer,args=(i,q)).start()









