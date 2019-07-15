import win32com
import win32com.client

def readWordFile(path):
    #调用系统word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    #打开文件
    doc = mw.Documents.Open(path)
    #doc.Paragraphs 拿出doc中的段落
    for paragraph in doc.Paragraphs:
        #按行取出
        line = paragraph.Range.Text
        print(line)
    #关闭文件
    doc.Close()
    #退出word
    mw.Quit()

path = r"G:\python_learn\pycharm_learn\pythonlearn\day011\4.world自动化办公\tracy.docx"


readWordFile(path)