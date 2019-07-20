import tkinter

root = tkinter.Tk()

text = tkinter.Text(root, width=30, height=2) #30的意思是30个平均字符的宽度，height设置为两行
text.pack()

text.insert(tkinter.END, 'I Love\n')  #INSERT表示输入光标所在的位置，初始化后的输入光标默认在左上角
text.insert(tkinter.INSERT, 'Study!')


def show():
    print("哎呦，我被点了一下！")

button =tkinter.Button(root,text="点我",command=show)
button.pack()



root.mainloop()
#生成好的Text组件可以进行编辑（并不是只读形式的）
