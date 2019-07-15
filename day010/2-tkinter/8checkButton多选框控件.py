import tkinter

win = tkinter.Tk()
win.title("tracy")
win.geometry("400x400+200+20")

def update():
    message = ""
    if hobby1.get() == True:
        message += "money\n"
    if hobby2.get() == True:
        message += "power\n"
    if hobby3.get() == True:
        message += "people\n"
    #清除text中的所有内容
    text.delete(0.0,tkinter.END)
    #将选中的message添加到text中
    text.insert(tkinter.INSERT,message)





#生成一个布尔类型的变量
#要绑定的变量
hobby1 = tkinter.BooleanVar()
#多选框  variable为变量，绑定为hobby1
check1  = tkinter.Checkbutton(win,text="money",
                    variable=hobby1,command=update)
check1.pack()

hobby2 = tkinter.BooleanVar()
check2  = tkinter.Checkbutton(win,text="power",
                    variable=hobby2,command=update)
check2.pack()

hobby3 = tkinter.BooleanVar()
check3  = tkinter.Checkbutton(win,text="people",
                    variable=hobby3,command=update)
check3.pack()

#设置文本内框
text = tkinter.Text(win,width=50,height=5)
text.pack()


win.mainloop()