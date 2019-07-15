import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("tracy")
win.geometry("400x400+200+20")

cv = tkinter.StringVar()
com = ttk.Combobox(win,textvariable=cv)
com.pack()
#设置下拉数据
com["value"] = ("黑龙江","吉林","辽宁")
#设置默认值
com.current(0)

#绑定事件
def func(event):
    print(com.get())
    print(cv.get())
    print("tracy is a good man")
com.bind("<<ComboboxSelected>>",func)









win.mainloop()