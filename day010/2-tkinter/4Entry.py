import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("Tracy")
#设置大小和位置
win.geometry("400x400+200+50") #长宽400 距离左侧200，上部50

'''
进入消息循环
输入控件
用于显示简单的文本内容
'''
#绑定变量
e = tkinter.Variable()
#show 密文显示  show=“*”
entry = tkinter.Entry(win,show="*",textvariable=e)
entry.pack()

#e就带包输入框这个对象
#设置值
# e.set("请输入密码")
#取值
# print(e.get())
print(entry.get())

win.mainloop()
