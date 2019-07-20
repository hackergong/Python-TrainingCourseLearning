import os
import time
from multiprocessing import Pool

def copyFile(rPath,wPath):
    fr = open(rPath,"rb")

    fw = open(wPath,"wb")

    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()

path = r"G:\python_learn\pycharm_learn\Python-TrainingCourseLearning\day016\2.进程\file"
toPath =r"G:\python_learn\pycharm_learn\Python-TrainingCourseLearning\day016\2.进程\tofile"


if __name__ == "__main__":
    #读取path下的所有的文件
    fileList = os.listdir(path)
    start = time.time()
    pp = Pool()
    for fileName in fileList:
        pp.apply_async(copyFile,args=(os.path.join(path,fileName),os.path.join(toPath,fileName)))
    pp.close()
    pp.join()
    end = time.time()
    print("总耗时：%0.2f" % (end-start))