#1
# s = set([1,2,3,3,4,4])
#
# s.update([7,8,9])
# for index,data in enumerate(s):
#     print(index,data)


#2
# from collections import Iterable
# from collections import Iterator
#
# print(isinstance([],Iterator))
# print(isinstance((),Iterator))
# print(isinstance({},Iterator))
# print(isinstance("",Iterator))
# print(isinstance((x for x in range(10)),Iterator))   #迭代器
#将list转化为迭代对象
# print(isinstance(iter([],Iterator)))
# print(isinstance(iter((),Iterator)))
# print(isinstance(iter({},Iterator)))
# print(isinstance(iter("",Iterator)))
# endstr = "end"
# str = ""
# for  line in iter(input,endstr):
#     str += line+ "\n"
#
# print(str)

# #3
# import sys
# import time
# from collections import deque
#
# fancy_loading = deque('>--------------------')
#
# while True:
#     print('\r%s' % ''.join(fancy_loading))
#     fancy_loading.rotate(1)
#     sys.stdout.flush()
#     time.sleep(0.08)


#4
# def func2(list):
#     list[0]=100
#     print(list)
#     print(id(list))
# li=[1,2,3,4,5]
# func2(li)
# print(li)
# print(id(li))

# a=10
# b=10
# print(id(a),id(b))

def func(name,*arr):
    print(name)
    for x in arr:
        print(x)
func("sunck","good","nice","handsome")









