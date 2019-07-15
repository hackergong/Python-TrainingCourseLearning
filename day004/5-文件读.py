'''
#读文件
'''

'''
过程：
1.打开文件（）
2.读文件内容
3.关闭文件
'''


'''
1.打开文件
open(open,flag[，encoding][，errors])
path:要打开文件的路径
flag:打开文件的方式
r：以只读的方式打开文件，文件的描述符放在文件的开头
rb：以二进制格式打开一个文件用于只读，文件的描述符
    放在文件的开头
r+：打开一个文件用于读写，文件的描述符放在文件的开头
w：打开一个文件只用于写入，如果该文件已经存在会覆盖，
    如果不存在则创建新文件
wb：打开一个文件只用于写入二进制，如果该文件已经存在会覆盖，
    如果不存在则创建新文件
w+：打开一个文件用于读写，如果该文件已经存在会覆盖，
    如果不存在则创建新文件
a：打开一个文件用于追加，如果该文件已经存在，文件描述符会放在
    文件末尾
a+：打开一个文件用于读写，
encoding:编码方式utf-8，jbk
errors：错误处理
'''

path = r"G:\python_learn\pycharm_learn\pythonlearn\day004\practice.txt"
f = open(path,"r",encoding = "utf-8",errors="ignore")


'''
2.读文件
'''
#1.读取文件的全部内容
# str1 = f.read()
# print(str1)

#2.读取指定字符数，read(参数)指的是前十个字符，如果出现中文，应该使用编码utf-8
# str2 = f.read(10)
# print(str2)

#3.读取整行readline()，包括“\n”字符
# str4 = f.readline()
# print(str4)
# str5 = f.readline()
# print(str5)

#4.readline()读取指定字符数
# str6 = f.readline(10)
# print(str6)

#5:readlines()读取所有行并返回列表
# list7 = f.readlines()
# print(list7)

#6:若给定的数字大于0，返回实际size字节的字数，读取所有行并返回列表
# list8 = f.readlines(20)
# print(list8)

#若文件描述符已经到了结尾，可修改文件描述符的位置
# f.seek(0)
# str9 = f.read()

#一个完整的过程
try:
    f1 = open(path,"r",encoding="utf-8")
    print(f1.read())
finally:
    if f1:
        f1.close()

#下面的方法可不用写关闭文件f2.close(),with自动关闭文件
with open(path,"r",encoding = "utf-8") as e:
    print(f2.read())

'''
3.关闭文件
'''
f.close()