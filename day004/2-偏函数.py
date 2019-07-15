
#1
'''
#将二进制1010输出为十进制
print(int("1010",base = 2))
'''

#2
'''
#偏函数，对参数上默认值的控制
def int2(str,base = 2):
    return int(str,base)
print(int2("1010"))
'''

#3
#把一个参数固定住，形成一个新的函数
import functools
int3= functools.partial(int,base = 2)
print(int3("1111"))
#partial返回一个参数，将int返回，base=2固定，用int3保存




