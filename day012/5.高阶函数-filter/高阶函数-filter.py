'''
原型：filter(fn,lsd)
参数1为函数
参数2为序列
功能：用于过滤序列
把传入的函数依次作用于序列每个元素,根据返回的是True还是False决定是否保留该元素
False 剔除数据   True  保留数据
'''


list1 = [1,2,3,4,5,6,7,8,9]
#筛选条件
def func(num):
    #偶数保留
    if num%2 == 0:
        return True
    #奇数剔除
    return False
l = filter(func,list1)
print(list(l))



data = [["姓名","年龄","爱好"],["tom",25,"无"],["hanhan",26,"金钱"]]
def func2(v):
    v = str(v)
    if v == "无":
        return False
    return True
for line in data:
    m = filter(func2,line)
    print(list(m))





































