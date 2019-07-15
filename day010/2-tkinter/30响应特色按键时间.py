import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("tracy")
win.geometry("600x400+200+20")


#<Shift_L> 响应左侧shift
#<shift_R> 响应右侧shift
#<F5>
#<Return>  回车
#<BackSpace>  退格
label = tkinter.Label(win,text="tracy is a good man",
                      bg="red")
#设置焦点
label.focus_set()
label.pack()
def func(event):
    print("event.char = ",event.char)
    print("event.keycode = ",event.keycode)
#响应左shift按键
label.bind("<Shift_L>",func)


win.mainloop()