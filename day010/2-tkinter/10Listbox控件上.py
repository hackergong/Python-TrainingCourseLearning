import tkinter

win = tkinter.Tk()
win.title("tracy")
win.geometry("400x400+200+20")


'''
列表框空间，可以包含一个或者多个文本框
作用：在listbox控件的小窗口显示一个字符串
'''

#1.创建一个listbox，添加几个元素
lb = tkinter.Listbox(win,selectmode=tkinter.BROWSE)
lb.pack()

#添加元素
for item in ["good","nice","handsome","vg","vn"]:
    #按顺序添加到末尾
    lb.insert(tkinter.END,item)
#在开始添加
lb.insert(tkinter.ACTIVE,"cool")
#将列表当成一个元素添加的
# lb.insert(tkinter.END,["great boy","cool boy"])
#删除  参数1 为开始的索引，参数2为结束的索引，如果不指定参数2
#，只删除第一个所有点的内容
# lb.delete(1,3)  #删除下标为1到3的元素
# lb.delete(1)  #删除下标为1的元素

#选中  参数1为开始的索引，参数2为结束的索引，如果不指定参数2
#，只选中第一个索引处的内容
lb.select_set(1,2)
# lb.select_set(2,5)
#取消选中
# lb.select_clear(2,4)
# lb.select_clear(4)


#获取列表中的元素的个数
# print(lb.size())


#从列表中取值，参数1为开始的索引，参数2为结束的索引，
#如果不指定参数2，只获取第一个索引处的内容
# print(lb.get(2,4))
print(lb.get(2,3))

#返回当前的索引项，不是item元素
print(lb.curselection())
#判断，一个选项是否被选中，返回True或False
print(lb.selection_includes(1))


win.mainloop()