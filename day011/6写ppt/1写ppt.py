import win32com
import win32com.client


def makePPT(path):
    ppt = win32com.client.Dispatch("PowerPoint.Appplication")
    ppt.Visible = True

    #增加一个文件
    pptFile = ppt.Presentations.Add()
    #创建页
    page1 = pptFile.Slides.Add(1,1)
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = "tracy"
    t2 = page1.Shapes[1].TextFrame.TextRange
    t2.Text = "tracy is a good man"

    #创建第二页
    page2 = pptFile.Slides.Add(1,1)
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = "tracy1"
    t2 = page1.Shapes[1].TextFrame.TextRange
    t2.Text = "tracy1 is a good man"

    #保存
    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()

path = r"G:\python_learn\pycharm_learn\pythonlearn\day011\6写ppt\a.pptx"

makePPT(path)