import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("tracy")
win.geometry("600x400+200+20")

def func(event):
    print(event.x,event.y)

'''
#<Double-Button-1>鼠标左键双击
#<Double-Button-3>鼠标右键双击
#<Triple-Button-1>鼠标左键三击
#<Button-1>鼠标左键，<Button-2>鼠标中键，<Button-3>鼠标右键
'''
button1=tkinter.Label(win,text="leftmouse button")
#bind 给控件绑定事件
button1.bind("<Double-Button-1>",func)  #鼠标绑定
button1.pack()









win.mainloop()