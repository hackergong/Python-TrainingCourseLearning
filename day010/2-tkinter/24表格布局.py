import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("tracy")
win.geometry("600x400+200+20")




label1= tkinter.Label(win,text="good",bg="blue")
label2= tkinter.Label(win,text="nice",bg="red")
label3= tkinter.Label(win,text="cool",bg="pink")
label4= tkinter.Label(win,text="handsome",bg="yellow")


#表格布局
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=1,column=0)
label4.grid(row=1,column=1)



win.mainloop()