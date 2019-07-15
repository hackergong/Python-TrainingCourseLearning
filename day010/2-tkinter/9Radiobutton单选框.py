import tkinter

win = tkinter.Tk()
win.title("tracy")
win.geometry("400x400+200+20")

def update():
    print(r.get())#打印vlaue值

#一组单选框要绑定同意变量
r = tkinter.IntVar() #绑定的是Int
# r =tkinter.StringVar() #绑定的是String
radio1 = tkinter.Radiobutton(win,text="one",value=1,
                             variable=r,command=update)
radio1.pack()

radio2 = tkinter.Radiobutton(win,text="two",value=2,
                             variable=r,command=update)
radio2.pack()

radio3 = tkinter.Radiobutton(win,text="three",value=3,
                             variable=r,command=update)
radio3.pack()


win.mainloop()