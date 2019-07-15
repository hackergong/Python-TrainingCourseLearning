import tkinter

win = tkinter.Tk()
win.title("tracy")
win.geometry("400x400+200+20")

'''
供用户通过拖拽指示器改变变量的值，可以水平，也可以竖直
tkinter.HORIZONTAL——水平   tkinter.VERTICAL——竖直(默认)
length  水平时表示宽度，竖直时表示高度
tickinterval  选择值将会为该值的倍数
'''
scale1 = tkinter.Scale(win,from_=0,to=100,orient=tkinter.VERTICAL
                       ,tickinterval=5,length=200)
scale1.pack()

#设置初始值
scale1.set(10)
#获取当前值
def showNum():
    print(scale1.get())

tkinter.Button(win,text="按钮",command=showNum).pack()





win.mainloop()
