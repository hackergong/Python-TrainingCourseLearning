import tkinter

win = tkinter.Tk()
win.title("Spinbox控件")
win.geometry("400x400+200+20")


'''
数值范围控件
increment=5 以5为步长，默认为1
values 最好不要与from to一起使用
'''
def update():
    print(v.get())



# command只要值改变就会执行相应的方法
v = tkinter.StringVar()#绑定个变量
sp = tkinter.Spinbox(win,from_=0,to=100,increment=1,
                    textvariable=v,command=update)
sp.pack()

#赋值
v.set(20)
#取值
# print(v.get())



win.mainloop()