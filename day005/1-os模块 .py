'''
os：包含了普遍的操作系统的功能
'''
import os

#1
#输出：nt-为windows操作系统，posix-为Linux，Unix，Mac,OS_X
# print(os.name)


#2
#打印操作系统的详细信息
# print(os.uname())

#3
#获取操作系统中的环境变量
# print(os.environ)
#获取指定环境变量
# print(os.environ.get("APPDATA"))

#4
#获取当前目录
# print(os.curdir)
#获取当前工作目录，即python脚本所在的目录
# print(os.getcwd())


#以列表的形式返回指定目录下的所有文件
# print(os.listdir(r"G:\python_learn\pycharm_learn\pythonlearn\day005"))
#在当前目录下创建新目录
# os.mkdir("sunck1")
# os.mkdir(r"G:\python_learn\pycharm_learn\pythonlearn\day005\sunck2")

#删除当前目录下的指定目录
# os.rmdir("sunck1")

#获取文件属性
# print(os.stat("sunck1"))

#重命名
# os.rename("sunck1","kaige1")

#删除普通文件
# os.remove("file1.txt")

# 运行shell命令
# os.system("notepad")#打开记事本
# os.system("write")#打开写字板
# os.system("mspaint")#打开画板
# os.system("msconfig")#系统设置

#os.system("shutdown -s -t 1")#关机  1可以设置时间，单位为秒
# os.system("shutdown -s -t 10000")
# os.system("shutdown -a") #取消关机操作

#os.system("taskkill /f /im notepad.exe") #关闭记事本

#有些方法存在os模块里，还有些存在于os.path中
#查看当前的绝对路径
#print(os.path.abspath("./kaige"))

#相对路径不是从根目录发起


#拼接路径
#os.path.join(p1,p2)
# p1 = r"G:\python_learn\pycharm_learn\pythonlearn\day004"

# p2 = "sunck"
# p3 = "\sunck1"
# p4 = r"sunck2\a\b"
# p5 = "/root/tracy/home"
#注意：参数2里开始不要有斜杠
# print(os.path.join(p1,p2))
#G:\python_learn\pycharm_learn\pythonlearn\day004\sunck
# print(os.path.join(p1,p3))
#G:\sunck1
# print(os.path.join(p1,p4))
#G:\python_learn\pycharm_learn\pythonlearn\day004\sunck2\a\b
# print(os.path.join(p1,p5))
#G:/root/tracy/home

#拆分路径
# os.path.split(path1)
# path1 = r"G:\python_learn\pycharm_learn\pythonlearn\day005"

# print(os.path.split(path1))
#拆分为元组，('G:\\python_learn\\pycharm_learn\\pythonlearn', 'day004')

#获取扩展名
# os.path.splitext(path1)
# print(os.path.splitext(path1))
#获取扩展名，('G:\\python_learn\\pycharm_learn\\pythonlearn\\day004\\kaige', '.txt')

# path2 = r"G:\python_learn\pycharm_learn\pythonlearn\day005\file.txt"
#判断是否是目录#是目录返回True，否则返回False
# os.path.isdir(path2)
# print(os.path.isdir(path2))
#是目录返回True，否则返回False

#判断文件是否存在
# os.path.isfile(path2)
# print(os.path.isfile(path2))


# path4 = r"G:\python_learn\pycharm_learn\pythonlearn\day002"
#判断目录是否存在
# os.path.exists(path4)
# print(os.path.exists(path4))

path3 = r"G:\python_learn\pycharm_learn\pythonlearn\day004\write5.txt"
#获得文件大小(字节)
# os.path.getsize(path3)
# print(os.path.getsize(path3))

#获得文件的所在目录
print(os.path.dirname(path3))
#获得路径下该文件的名字
print(os.path.basename(path3))



#PID-进程号



