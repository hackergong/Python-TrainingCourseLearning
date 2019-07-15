import urllib.request
import ssl
import re
import os

def writeFileBytes(htmlBytes,toPath=""):
    #Bytes,二进制，所以wb
    with open(toPath,"wb") as f:
        f.write(htmlBytes)

def writeFileStr(htmlBytes,toPath=""):
    with open(toPath,"w") as f:
        f.write(str(htmlBytes))

def getHtmlBytes(url):
    headers = {
        "User-Agent":"Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/54.0.2840.99 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)
    return response.read()

def qqCrawler(url,toPaht):
    htmlBytes = getHtmlBytes(url)

    htmlStr = str(htmlBytes)
    pat = r"[1-9]\d{4,10}"
    re_qq = re.compile(pat)
    #finditer
    qqList = re_qq.findall(htmlStr)
    #去重
    qqList = list(set(qqList))
    # print(qqList)
    # print(len(qqList))


'''
    writeFileBytes(htmlBytes,r"G:\python_learn\pycharm_learn\pythonlearn\day014\file\fileBytes.html")
    writeFileStr(htmlBytes,r"G:\python_learn\pycharm_learn\pythonlearn\day014\file\FileStr.html")
'''



url = r"https://www.douban.com/event/15918569/discussion/44770328/"
toPath = r"G:\python_learn\pycharm_learn\pythonlearn\day014\file\qqFile.txt"
qqCrawler(url,toPath)











