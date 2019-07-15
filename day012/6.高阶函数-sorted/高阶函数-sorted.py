'''
#排序：冒泡，选择， <  快速，插入，计数器排序

'''
#1
#普通排序
list1 = [4,7,2,5,3]
list2 =sorted(list1)   #默认升序排序
print(list1)
print(list2)


#2
#按绝对值大小排序
list3 = [4,-7,2,-5,3]
#key接受函数来实现自定义排序规则
list4 =sorted(list3,key=abs)  #默认升序排序
# list4 =sorted(map(abs,list3))
print(list3)
print(list4)

#3
#降序
list5 = [4,7,2,5,3]
list6 =sorted(list5,reverse=True)
print(list5)
print(list6)


#4
list7 = ["f","c","e","a","h"]
list8 =sorted(list7)
print(list7)
print(list8)

#5
#按字符串长度拍
list9 = ["fffffff","cccc11","ef2","aca23","2h2"]
list10 =sorted(list9,key=len)
print(list9)
print(list10)

#6
#函数可以自己写
def myLen(str):
    return len(str)
list11 = ["fffffff","cccc11","ef2","aca23","2h2"]
list12 =sorted(list11,key=myLen)
print(list11)
print(list12)



































