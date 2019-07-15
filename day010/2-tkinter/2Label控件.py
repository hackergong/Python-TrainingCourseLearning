import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("Tracy")
#设置大小和位置
win.geometry("400x400+200+50") #长宽400 距离左侧200，上部50

#进入消息循环
'''
Label:标签控件，可以显示文本
'''
#win:父窗体
#text:显示文本内容
#bg:背景色
#fg:字体色
#wraplength:指定text文本中多宽后进行换行
#justify :设置换行后的对齐方式center lift right
#anchor：位置  n北,e东,s南,w西,ne东北,nw西北,se东南,sw西南,or center
label = tkinter.Label(win,
                      text="tracy is a perfect boy",
                      bg = "white",
                      fg = "red",
                      font = ("黑体",20),
                      width = 10,
                      height = 10,
                      wraplength = 100,
                      justify = "center",
                      anchor = "center")
#显示在win上
label.pack()

win.mainloop()