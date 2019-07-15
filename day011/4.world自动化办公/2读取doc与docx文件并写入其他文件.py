import win32com
import win32com.client
import time
time.perf_counter()





def readWordFileToOtherFile(path,toPath):
    #调用系统word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    #打开文件
    doc = mw.Documents.Open(path)

    #将word的数据保存到另一个文件,2 表示是txt文件
    doc.SaveAs(toPath,2)

    #关闭文件
    doc.Close()
    #退出word
    mw.Quit()

path = r"G:\python_learn\pycharm_learn\pythonlearn\day011\4.world自动化办公\tracy.docx"
toPath = r"G:\python_learn\pycharm_learn\pythonlearn\day011\4.world自动化办公\a.txt"

readWordFileToOtherFile(path,toPath)

y3=time.perf_counter()
print("%ds" % y3)