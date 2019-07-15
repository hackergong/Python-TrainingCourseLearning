import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("tracy")
win.geometry("600x400+200+20")

#<B1-Motion>左键移动
#<B2-Motion>中键移动
#<B3-Motion>右键移动
label = tkinter.Label(win,text="tracy is a good man")
label.pack()
def func(event):
    print(event.x,event.y)

label.bind("<B1-Motion>",func)#左键移动

#右键移动


win.mainloop()
