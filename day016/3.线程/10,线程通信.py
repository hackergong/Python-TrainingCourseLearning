import threading,time


def func():
    #事件对象
    event = threading.Event()
    def run():
        for i in range(5):
            #阻塞，等待事件的触发
            event.wait()
            #重置阻塞，可以再次阻塞
            event.clear()
            print("tracy is a good man! %d" % i )
    t = threading.Thread(target=run).start()
    return event

e = func()

#触发事件
for i in range(5):
    time.sleep(2)
    e.set()

















