import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("Tracy")
#设置大小和位置
win.geometry("400x400+200+50") #长宽400 距离左侧200，上部50

#进入消息循环
def showInfor():
    print(entry.get())

#全局变量
entry = tkinter.Entry(win)
entry.pack()

button = tkinter.Button(win,text="按钮",command=showInfor)
button.pack()


win.mainloop()