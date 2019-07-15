
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("Tracy")
#设置大小和位置
win.geometry("400x400+200+50") #长宽400 距离左侧200，上部50

#进入消息循环
'''
文本控件，用于显示多行文本
'''
#height:表示行数
text = tkinter.Text(win,width=30,height=4)
text.pack()  #将控件置入窗体win
str = '''I have a dream,the world is peace，I have a dream,the world is peace，
I have a dream,the world is peace，I have a dream,the world is peace，
I have a dream,the world is peace，I have a dream,the world is peace，
'''
text.insert(tkinter.INSERT,str) #将str嵌入文本控件


win.mainloop()