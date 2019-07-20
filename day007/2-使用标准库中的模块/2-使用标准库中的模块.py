'''
引入模块
'''
#使用cmd执行
import sys
# import time
# import datetime
# print(sys.argv)
#获取命令行参数的列表
# for i in sys.argv:
    # print(i+"\n")

name = sys.argv[0]
age = sys.argv[1]
print(name,age)

#自动查找所需模块的路径的列表
# print(sys.path)

'''
sys.exit(n)
功能：执行到主程序末尾，解释器自动退出，但是如果需要中途退出程序，可以调用sys.exit函数，带有一个可选的整数参数返回给调用它的程序，表示你可以在主程序中捕获对sys.exit的调用。（0是正常退出，其他为异常

'''

