from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
import win32com
import win32com.client
import csv

import sys
import importlib

importlib.reload(sys)



class DealFile(object):
    #读取cs
    def readCsv(path):
        infoList = []
        with open(path,"r") as f:
            allFileInfo = csv.reader(f)
            print(allFileInfo)
            for row in allFileInfo():
                infoList.append(row)
        return infoLis
    #写csv
    #[["1","2","3"],["4","5","6"],["7","8","9"]]
    def writeCsv(self,path,data):
        with open(path,"w") as f:
            writer = csv.writer(f) #创建一个writer
            for rowData in data:
                print("rowFata = ",rowData)
                writer.writerow(rowData)  #按行写入
    #读取pdf
    def readPdf(self,path,callback=None,toPath=""):
        f = open(path,"rb")
        parser = PDFParser(f)
        pdfFile = PDFDocument()
        parser.set_document(pdfFile)
        pdfFile.initialize()
        pdfFile.set_parser(parser)
        if not pdfFile.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            manager = PDFResourceManager()
            laparams = LAParams()
            device = PDFPageAggregator(manager,laparams=laparams)
            interpreter = PDFPageInterpreter(manager,device)
            for page in pdfFile.get_pages():
                interpreter.process_page(page)
                layout = device.get_result()
                for x in layout:
                    if (isinstance(x,LTTextBoxHorizontal)):
                        if toPath == "":
                            #处理每行数据
                            str = x.get_text()
                            if callback != None:
                                callback(str)#当做函数运行
                            print(str)
                        else:
                            with open(toPath,"a") as f:
                                str1 = x.get_text()
                                print(str1)
                                f.write(str1+"\n")

    def readWordFile(path):
        mw = win32com.client.Dispatch("Word.Application")
        doc = mw.Documents.Open(path)
        for paragraph in doc.Paragraphs:
            line = paragraph.Range.Text
            print(line)
        doc.Close()
        mw.Quit()