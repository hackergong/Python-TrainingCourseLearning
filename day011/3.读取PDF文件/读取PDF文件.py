import sys
import importlib

importlib.reload(sys)

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def readPdf(path, toPath):
    #以二进制形式打开pdf文件
    f = open(path,"rb")

    #创建一个pdf分析器
    parser = PDFParser(f)

    #创建pdf文档
    pdfFile = PDFDocument()

    #链接分析器与文件分析器
    parser.set_document(pdfFile)
    #提供初始化密码
    pdfFile.initialize()  #现在是无密码状态

    pdfFile.set_parser(parser)
    #检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        #解析数据
        #数据管理器
        manager = PDFResourceManager()
        #创建一个PDF设备对象
        laparams = LAParams()
        #创建聚合器
        device = PDFPageAggregator(manager,laparams=laparams)
        #解释器对象
        interpreter = PDFPageInterpreter(manager,device)

        #开始循环处理，每次处理一页
        for page in pdfFile.get_pages():
            #使用页面解释器来获取
            # PDFPageInterpreter.process_page(page)
            interpreter.process_page(page)
            #使用聚合器获取内容
            layout = device.get_result()
            for x in layout:
                #判断x是否是LTTextBoxHorizontal类型
                if (isinstance(x,LTTextBoxHorizontal)):
                    with open(toPath,"a") as f:#以追加的形式写入pdf
                        #
                        str1 = x.get_text()
                        print(str1)
                        f.write(str1+"\n")







path = r"G:\python_learn\pycharm_learn\pythonlearn\day011\3.读取PDF文件\00005.pdf"
toPath =  r"G:\python_learn\pycharm_learn\pythonlearn\day011\3.读取PDF文件\a.txt"
readPdf(path,toPath)










































