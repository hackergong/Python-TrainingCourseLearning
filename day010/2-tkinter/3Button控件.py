import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("Tracy")
#设置大小和位置
win.geometry("400x400+200+50") #长宽400 距离左侧200，上部50

def func():
    print("tracy is a good man")
# 执行程序
button1 = tkinter.Button(win,text="按钮",command=func,width=3,height=1)
button1.pack()

#退出界面
button2 = tkinter.Button(win,text="退出",command=win.quit)
button2.pack()


win.mainloop()
