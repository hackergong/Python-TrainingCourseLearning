'''
'''
'''
try.....except....finally
格式：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
..........
except 错误码 as e:
    语句n
finally:
    语句f

作用:语句t无论是否有错误都执行最后的语句f
'''
# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print("为0了")
# finally:
#     print("必须执行我")
#在打开文件使用后，必须关闭文件，而该方法可以使用到，因为不管有没有错误都会
#强制关闭

#断言!!!!!!!!
def func(num,div):
    assert div!= 0,'div不能为0'
    return num/div
print(func(10,0))
