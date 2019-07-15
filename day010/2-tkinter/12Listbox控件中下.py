import tkinter

win = tkinter.Tk()
win.title("tracy")
# win.geometry("400x400+200+20")

'''
EXTENDED 可以使listbox支持shift和control
'''
#列表box
lb = tkinter.Listbox(win,selectmode=tkinter.EXTENDED)

for item in ["good","nice","handsome","vg","vn","ad","ab","dv"
             ,"as","tg","mnm","lakers","mmm","nnnn","oooo","pppp",
"nice","handsome","vg","vn"]:
    #按顺序添加
    lb.insert(tkinter.END,item)
'''
按住shift，可以实现连选
按住ctrl可以实现单选
'''
#滚动条
sc =tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT,fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
#额外给属性赋值
sc['command'] = lb.yview

win.mainloop()