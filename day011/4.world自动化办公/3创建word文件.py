import win32com
import win32com.client
import os

def makeWordFile(fileName,name):
    word = win32com.client.Dispatch("Word.Application")
    #让文档可见
    word.Visible = True

    #创建文档
    doc = word.Document.Add()

    #写内容
    #从头开始写
    r = doc.Range(0,0)
    r.InsertAfter("Hello"+"name"+"\n")
    r.InsertAfter("      你吃了吗？\n")

    #存储文件
    doc.SaveAs(path)
    #关闭文件
    doc.Close()
    #退出word
    word.Quit()

names = ["张三","李四","王五"]
for name in names:
    path = os.path.join(os.getcwd(),name)
    makeWordFile(path,name)
