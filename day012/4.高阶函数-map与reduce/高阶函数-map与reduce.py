'''
大数据
2015年
分布式zookepeer
hadoop
spark

storm
Jstorm
zookepeer
kafka
spring

'''

'''
#python内置了map()和reduce()
#map()
#原型 map(fn,lsd)
#参数1是函数
#参数2是序列
#功能：将传入的函数依次作用在序列中的每一个元素，并把结果作为新的Iterator返回
#将数据处理为可使用的方式
'''
'''
#将单个字符转成对应的字面量整数
def chr2int(chr):
    return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[chr]
list1 = ["2","1","6","5"]
res = map(chr2int,list1)
print(res) #打印的是一个对象，是惰性列表
# print(list(res))  #应该用list()将其显示
#[chr2int("2"),chr2int("1"),chr2int("6"),chr2int("5"),
'''

'''
#将整数元素的列表，转为字符串型
#[1,2,3,4] -> ["1","2","3","4"]
l = map(str,[1,2,3,4])
print(list(l))
'''


'''
#reduce(fn,lsd)
#参数1为函数
#参数2为列表
#功能：一个函数作用在序列上，这个函数必须接受两个参数，reduce把结果继续和序列的下一个元素累计运算
#reduce(f,[a,b,c,d])
#f(f(f(a,b),c),d)
'''

from functools import reduce

'''
#求一个序列的和
list2 = [1,2,3,4,5]
#1 + 2
#1 + 2 + 3
#1 + 2 + 3 + 4
#1 + 2 + 3 + 4 + 5
def mySum(x,y):
    return x + y
r = reduce(mySum,list2)
print(r)
'''

#将字符串转成对应字面量数字
def str2int(str):
    def fc(x,y):
        return x * 10 + y
    def fs(chr):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[chr]
    return reduce(fc,map(fs,list(str)))
a = str2int("13579")
print(a)
print(type(a))

def myMap(func,li):
    resList = []
    for parase in li:
        res = func(parase)
        resList.append(res)




















































































