from dealFile import DealFile

d =DealFile( )
path = r"G:\python_learn\pycharm_learn\pythonlearn\day012\作业\1文件的封装\00001.pdf"

def func(str):
    print(str + "!")
#              回调函数（再另一个函数里使用
d.readPdf(path,func)


