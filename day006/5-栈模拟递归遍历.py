'''


使用栈来模拟递归调用
'''
import os

def getAllDirRE(path):
    stack  = []
    stack.append(path)

    #处理栈
    while len(stack)!=0:
        #从栈里取出数据
        dirPath = stack.pop()
        #查看目录下所有文件
        fileList = os.listdir(dirPath)
        #fileList表示当前路径下的文件目录
        #处理每一个文件，如果是普通文件则打印出来，如果是目录则将目录的地址压栈
        for fileName in fileList:
            fileAbsPath = os.path.join(dirPath,fileName)
            if os.path.isdir(fileAbsPath):
                #是目录就压栈
                print("目录："+fileName)
                stack.append(fileAbsPath)
            else:
                #打印普通文件
                print("普通文件:"+fileName)

getAllDirRE(r"I:\book")