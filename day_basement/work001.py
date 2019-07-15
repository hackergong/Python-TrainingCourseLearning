'''
作业1
水仙花数
从控制台输入一个三位数，如果是水仙花数就该打印“是水仙花数”，否则打印“不是水仙花数“
153=1^3+5^3+3^3

'''
'''
print("水仙花数程序,输入2则退出")

while num!=0:
#判断是否是三位数
    num=(input("请输入一个三位数： "))
    if len(str(num))!=3:
      num=int(input("请重新输入一个三位数： "))

#求每一位数
    num=int(num)
    uint=(num % 100) % 10
    tens=int((num % 100) / 10)
    hundreds = int(num / 100)

    #test
    # temp=uint**3+tens**3+hundreds**3
    # print(temp)

    temp=uint**3+tens**3+hundreds**3
    if temp==num:
        print("%.2d是水仙花数" % num)
    else:
        print("%.2d不是水仙花数" % num)
'''

'''
作业2
从控制台输入一个五位数，如果是回文数就打印“是回文数”，否则打印“不是回文数”
11111.12321
'''
'''
print("回文数程序")

#判断是否是5位数
num=(input("请输入一个五位数： "))
if len(str(num))!=5:
    num=int(input("请重新输入一个五位数： "))

#求每一位数
num=int(num)

a1 = int(num / 10000)
a2 = int((num /1000) % 10)
a3 = int((num / 100) % 10)
a5 = int(num % 10)
a4 = int(((num % 100)-a5) / 10)

print (a1,a2,a3,a4,a5)
#判断
if a1==a5:
    if a2==a4:
        print("%d是回文数" % num)
else:
    print("%d不是回文数" % num)
'''

'''
作业三
从控制台输入两个数，输出较大的值
从控制台输入三个数，输出较大的值
'''

'''
print("请输入两个数")
num1 = int(input("num1："))
num2 = int(input("num2："))

num3 = int(input("num2："))
#判断两个数
# if num1 == num2:
#     print(num1)
# else:
#     if num1 > num2:
#         print(num1)
#     else:
#         print(num2)

#判断三个数
# if num1 > num2:
#     if num1 > num3:
#         print(num1)
#     else:
#         print(num3)
# else:
#     if num2 > num3:
#         print(num2)
#     else:
#         print(num3)

#
max=num1
if num2 > max:
    max=num2
if num3 > max:
    max=num3
print(max)
'''
#
# a=1
# if not a:
#     print("0000")
# else:
#     print ("11111")

#输出重复字符串
# str1="good"
# str2=str1*10
# print("str2=",str2)
# str3="tracy is a good man"
# str4=str3[6:19]
# print(str4)

#转义字符串

# print(r"\\t\\")
# print(r"F:\统计软件\t in Action 中文版PDF及原代码")
#
# print(eval("-123-1"))

# str5="good man"
# print(str5.center(40,"*"))

# str9="kaige is a very very nice man"
# print(str9.rindex("very"))
#
# num=1
# while num<=5:
#     print(num)
#     num +=1
# num=1
# sum=0
# while num <=100:
#     sum += num
#     num +=1
# print(sum)

# str = "sunck is a handsome man"
# index = 0
# while index < len(str):
#     print("str[%d] = %s" % (index, str[index]))
#     index +=1











