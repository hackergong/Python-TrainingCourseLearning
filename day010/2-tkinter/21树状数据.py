import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("tracy")
win.geometry("600x400+200+20")

tree = ttk.Treeview(win)
tree.pack()

#添加一级树枝
treeF1 = tree.insert("",0,"中国",text="中国CHN",
                     values=("F1"))
treeF2 = tree.insert("",1,"美国",text="美国USA",
                     values=("F2"))
treeF3 = tree.insert("",2,"英国",text="英国UK",
                     values=("F3"))
#添加二级树枝
treeF1_1 = tree.insert(treeF1,0,"黑龙江",text="中国黑龙江",
                     values=("F1_1"))
treeF1_2 = tree.insert(treeF1,1,"吉林",text="中国吉林",
                     values=("F1_2"))
treeF1_3 = tree.insert(treeF1,2,"辽宁",text="中国辽宁",
                     values=("F1_3"))

treeF2_1 = tree.insert(treeF2,0,"得克萨斯州",text="美国得克萨斯州",
                     values=("F1_1"))
treeF2_2 = tree.insert(treeF2,1,"底特律",text="美国底特律",
                     values=("F1_2"))
treeF2_3 = tree.insert(treeF2,2,"旧金山",text="美国旧金山",
                     values=("F1_3"))

#三级树枝
treeF1_1_1 = tree.insert(treeF1_1,0,"哈尔滨",text="黑龙江哈尔滨")
treeF1_1_2 = tree.insert(treeF1_1,0,"五常",text="黑龙江五常")


win.mainloop()


#作业做一个五级的项目
#写界面