import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("tracy")
win.geometry("600x400+200+20")


#<Key> 响应所有的按键
label = tkinter.Label(win,text="tracy is a good man",
                      bg="red")
#设置焦点
label.focus_set()
label.pack()
def func(event):
    print("event.char = ",event.char)
    print("event.keycode = ",event.keycode)
#响应所有的按键
label.bind("<Key>",func)

# def func(event):
#     print("event.char = ",event.char)
#     print("event.keycode = ",event.keycode)
# win.bind("<Key>",func)
win.mainloop()
