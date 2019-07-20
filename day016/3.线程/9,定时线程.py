import threading
import time
def run():
    print("tracy is a good man ")

#延时执行
time.perf_counter()
t = threading.Timer(7,run)
t.start()
t.join()
print(time.perf_counter())
print("结束")