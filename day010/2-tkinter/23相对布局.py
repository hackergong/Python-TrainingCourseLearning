import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("tracy")
win.geometry("600x400+200+20")



label1= tkinter.Label(win,text="good",bg="blue")
label2= tkinter.Label(win,text="nice",bg="red")
label3= tkinter.Label(win,text="cool",bg="pink")

#相对布局，窗体改变对空间有影响
label1.pack(fill=tkinter.BOTH,side=tkinter.LEFT)
label2.pack(fill=tkinter.X,side=tkinter.TOP)
label3.pack()




win.mainloop()