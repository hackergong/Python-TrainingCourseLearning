'''
为了方便存储
等等
'''
#编码******
path = r"G:\python_learn\pycharm_learn\pythonlearn\day004\write5.txt"

with open(path,"wb") as f1:
    str = "tracy is a good man凯"
    f1.write(str.encode("utf-8"))

with open(path,"rb") as f2:
    data = f2.read()
    print(data)
    print(type(data))
    newData = data.decode("utf-8")
    print(newData)
    print(type(newData))
#errors可以忽略打开文件的错误
#以二进制写入时，应该编码和解码同一种码
#以utf-8编码，读取时以gbk读取，加上errors，读出的汉字成为乱码







