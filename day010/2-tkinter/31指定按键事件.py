import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("tracy")
win.geometry("600x400+200+20")

def func(event):
    print("event.char = ",event.char)
    print("event.keycode = ",event.keycode)

win.bind("a",func)

win.mainloop()