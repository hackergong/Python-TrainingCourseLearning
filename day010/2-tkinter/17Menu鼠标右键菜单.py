import tkinter

win = tkinter.Tk()
win.title("tracy")
win.geometry("400x400+200+20")


#菜单条
menubar = tkinter.Menu(win)

#菜单
menu1 = tkinter.Menu(menubar,tearoff=False)

#给菜单选项添加内容
for item in ["Python","C","C++","OC","Swift","C#",
             "shell","Java","Js","PHP","汇编","NodeJS","退出"]:
    menu1.add_command(label=item)
menubar.add_cascade(label="语言",menu=menu1)

def showMenu(event):
    menubar.post(event.x_root,event.y_root)
#鼠标滚轮
win.bind("<Button-3>",showMenu)





win.mainloop()