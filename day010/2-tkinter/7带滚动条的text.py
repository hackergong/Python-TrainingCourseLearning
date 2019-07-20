
import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("Tracy")
#设置大小和位置
# win.geometry("400x400+200+50") #长宽400 距离左侧200，上部50

#进入消息循环
'''
文本控件，用于显示多行文本，长文本应加入滚动条
'''

#创建滚动条
scroll = tkinter.Scrollbar()
#创建文本控件
text = tkinter.Text(win,width=50,height=8)  #height:表示行数
#放到窗体的哪一侧
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text.pack(side=tkinter.LEFT,fill=tkinter.Y)
#关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)


str = '''hat I'd like to do is to make some opening comments, and then what I'm really looking forward to doing is taking questions,
not only from students who are in the audience, but also we've received questions online, which will be asked by some of the students
who are here in the audience, as well as by Ambassador Huntsman. And I am very sorry that my Chinese is not as good as your English,
but I am looking forward to this chance to have a dialogue.
This is my first time traveling to China, and I'm excited to see this majestic country. Here, in Shanghai, we see the growth that has
caught the attention of the world -- the soaring skyscrapers, the bustling streets and entrepreneurial activity. And just as I'm impr
essed by these signs of China's journey to the 21st century, I'm eager to see those ancient places that speak to us from China's dista
nt past. Tomorrow and the next day015 I hope to have a chance when I'm in Beijing to see the majesty of the Forbidden City and the wonder
of the Great Wall. Truly, this is a nation that encompasses both a rich history and a belief in the promise of the future.'''

text.insert(tkinter.INSERT,str)






win.mainloop()