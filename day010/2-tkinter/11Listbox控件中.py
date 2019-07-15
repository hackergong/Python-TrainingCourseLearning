import tkinter

win = tkinter.Tk()
win.title("Listbox控件中")
win.geometry("400x400+200+20")

#绑定变量
lbv = tkinter.StringVar()
#与BORWSE相似，但不支持鼠标移动选中位置
lb = tkinter.Listbox(win,selectmode=tkinter.SINGLE,listvariable=lbv)
lb.pack()
for item in ["good","nice","handsome","vg","vn"]:
    #按顺序添加
    lb.insert(tkinter.END,item)

#打印当前列表中的选项
print(lbv.get())
#设置选项，上面的选项全部变为下面设置的选项
# lbv.set(("1","2","3"))

#绑定事件,"点击鼠标左键两下"
def myPrint(event):
    print(lb.get(lb.curselection()))
#重点重点重点重点
lb.bind('<Double-Button-1>',myPrint)


win.mainloop()









