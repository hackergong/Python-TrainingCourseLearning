import tkinter

win = tkinter.Tk()
win.title("多选")
# win.geometry("400x400+200+20")

#MULTIPLE  支持多选
lb = tkinter.Listbox(win,selectmode=tkinter.MULTIPLE)
lb.pack()

for item in ["good","nice","handsome","vg","vn"]:
    #按顺序添加
    lb.insert(tkinter.END,item)


win.mainloop()