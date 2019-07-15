'''
引入模块
'''
#使用cmd执行
import sys
import time
import datetime

print(sys.argv)
#获取命令行参数的列表
for i in sys.argv:
    print(i+"\n")

# name = sys.argv[1]
# age = sys.argv[2]
# print(name,age)

#自动查找所需模块的路径的列表
print(sys.path)



