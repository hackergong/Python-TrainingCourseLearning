import os
import time

def copyFile(rPath,wPath):
    fr = open(rPath,"rb")

    fw = open(wPath,"wb")

    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()

path = r"G:\python_learn\pycharm_learn\Python-TrainingCourseLearning\day016\2.进程\file"
toPath =r"G:\python_learn\pycharm_learn\Python-TrainingCourseLearning\day016\2.进程\tofile"


#读取path下的所有的文件
fileList = os.listdir(path)

#启动for循环处理每一个文件
start = time.time()
for fileName in fileList:
    copyFile(os.path.join(path,fileName),os.path.join(toPath,fileName))


end = time.time()
print("总耗时：%0.2f" % (end-start))
# print(time.perf_counter())
#0.152358289







