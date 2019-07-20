from multiprocessing import Process
import os
import time

class TracyProcess(Process):
    def __init__(self,name):
        #Process.__init__(self)
        Process.__init__(self)
        self.name = name

    def run(self):
        print("子进程(%s-%s)启动" % (self.name,os.getpid()))

        time.sleep(3)

        print("子进程(%s-%s)启动" % (self.name,os.getpid()))
