'''
打印出所有三位数中的水仙花数
告诉我五位数中右多少个回文数
从控制台输入一个数，判断是否是质数
从控制台输入一个数，分解质因数         ****
从控制台输入一个字符串，返回这个字符串中有多少个单词*****
从控制台输入一个字符串，打印出这个字符串中所有数字字符的和 ******
'''


#打印出所有三位数中的水仙花数
'''
print("所有三位数中的水仙花数程序")
num=100
while num <= 999:

#求每一位数
    uint=(num % 100) % 10
    tens=int((num % 100) / 10)
    hundreds = int(num / 100)

    #test
    # temp=uint**3+tens**3+hundreds**3
    # print(temp)

    temp=uint**3+tens**3+hundreds**3
    if temp==num:
        print(num)
    num += 1

#153 370 371 407
'''

#告诉我五位数中右多少个回文数
'''
print("回文数程序")

num = 10000
count_num = 0
while num <= 99999:

    a1 = int(num / 10000)
    a2 = int((num / 1000) % 10)
    a3 = int((num / 100) % 10)
    a5 = int(num % 10)
    a4 = int(((num % 100) - a5) / 10)

# 判断
    if a1 == a5:
        if a2 == a4:
            print(num)
            count_num += 1
    num += 1
print ("回文数共有:%d个" % (count_num))
#900个

'''


#从控制台输入一个数，判断是否是质数
#除了1和它本身外，没有任何其它因数
'''
import math
num = int(input("input a number:"))

i=2
while i <= (math.ceil(num/2)):
    if num % i==0:
        print("%d不是质数" % (num))
        break
    i +=1
if i==(math.ceil(num/2)+1):
    print("%d是质数" % (num))

'''

#从控制台输入一个数，分解质因数
#把合数用几个质数相乘的形式表现出来
#
# num= int(input())
# i =2
# while num != 1:
#     if num % i == 0:
#         print(i)
#         num //= i   #取整
#     else:
#         i += 1




'''
import math

num = int(input("input a number:"))
f = []
i = 2
a = "false"
temp = num
for i in range(2,num):
    while True:
        if num % i == 0:
            f.append(i)
            a = "True"
            num = num/2
        else:
            break


if a == "False":
    print("%d的质因数是1和%d" % (num,num))
else:
    print(f)

'''


#从控制台输入一个字符串，返回这个字符串中有多少个单词

'''
str = input("请输入一个字符串：")

i = 0
x = 0
str=str.strip()

while i < (len(str)):
    while str[i] != " ":
        i += 1
        if i == len(str):
            break
            #结束所有循环
    x += 1
   # print(x)
    if i == len(str):
        break
    while str[i] == " ":
        i += 1
print("一共有%d个单词" % x)
'''



#从控制台输入一个字符串，打印出这个字符串中所有数字字符的和
#字符0的ASCll码为48 字符9的ASCll码为57
'''
str = input("请输入一个字符串：")

i = 0
str=str.strip()
sum = 0
while i < (len(str)):
    if str[i] <= "9" and str[i] >= "0" :
        sum += int(str[i])
    i += 1

print("sum = %d" % sum)

'''
'''
列表练习
'''
# list11 = [[1,2,3],[4,5,6],[7,8,9]]
# print(list11[0][0])

# list13 = [1,2,3,4,5]
# list13.extend([6,7,8])
# print(list13)

#从列表中找出某个值第一个匹配的索引值
# list18 = [1,2,3,4,5,3,4]
# index0 = list18.index(4)
# index1 = list18.index(3,3,6)
# print(index1)



#
# num = 0
# listNum = []
# while num < 5:
#     val = int(input("请"))
#     listNum.append(val)
#     num += 1
# print(listNum)

# listNum.sort()
# #计算最大值有多少个，之后依次删除
# count = listNum.count(listNum[len(listNum)-1])
# #listNum[最大值]
# print(count)
# c=0
# while c<count:
#     listNum.pop()
#     c += 1
# print(listNum[len(listNum)-1])
#


# import  turtle
#
# turtle.screensize(100,500)
# turtle.done()


# str40 = '''
# tracy is a good man
# tracy is a nice man
# tracy is a handsome man
# '''
# print(str40.splitlines())


# list41 = ['tracy','is','a','good','man']
# str42 = " ".join(list41)
# print(str42)