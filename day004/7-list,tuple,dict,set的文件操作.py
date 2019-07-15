'''
dict,tuple,dict,set的文件操作
'''
import pickle  #数据持久性模块

#写入操作  pickle.dump()
myList = (1,2,3,4,5,"hello master!","该")
path = r"G:\python_learn\pycharm_learn\pythonlearn\day004\write.txt"
f = open(path,"wb")
pickle.dump(myList,f)
f.close()

#读取   pickle.load()

f1 = open(path,"rb")
tempList = pickle.load(f1)
print(tempList)
f1.close()


