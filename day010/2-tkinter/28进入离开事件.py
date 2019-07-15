import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("tracy")
win.geometry("600x400+200+20")

#<Enter>鼠标光标进入时触发
#<Leave>鼠标光标离开时触发
label = tkinter.Label(win,text="tracy is a good man")
label.pack()
def func(event):
    print(event.x,event.y)

label.bind("<Leave>",func)









win.mainloop()
