import os
#递归
def getAllDir(path,sp = ""):
    fileList = os.listdir(path)
    sp += "   "
    for fileName in fileList:
        #path\fileName
        #判断是否是路径
        #处理每一个文件

        fileAbsPath = os.path.join(path,fileName)
        if os.path.isdir(fileAbsPath):
            print(sp,"目录:",fileName)
            getAllDir(fileAbsPath,sp)
        else:
            print(sp+"普通文件:",fileName)

getAllDir(r"I:\book")
