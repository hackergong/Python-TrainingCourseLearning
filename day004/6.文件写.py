'''
文件的写
'''
import time
path = r"G:\python_learn\pycharm_learn\pythonlearn\day004\write2.txt"
f = open(path,"w")

#写文件
#1.将信息写入缓冲区
f.write("I alse like play basketbal\n")


#2.刷新缓冲区 flush()
#直接把内部缓冲区的数据立刻写入文件，而不是被动的等待自动刷新缓冲区写入。
f.flush()

#文件未关闭，但仍然将缓冲区的数据写入文件。
while True:
    pass


# while 1:
#     f.write("I like play football")
#     time.sleep(0.0001)

#使用\n,也可以刷新缓冲区
#f.write("I alse like play basketbal\n")


f.close()