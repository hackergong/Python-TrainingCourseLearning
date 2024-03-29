import urllib.request
import ssl
import re
import os
from collections import deque

def writeFileBytes(htmlBytes,toPath):
    #Bytes,二进制，所以wb
    with open(toPath,"wb") as f:
        f.write(htmlBytes)

def writeFileStr(htmlBytes,toPath):
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

def qqCrawler(url,toPath):
    htmlBytes = getHtmlBytes(url)
    htmlStr = str(htmlBytes)
    pat = r'(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)'

    re_url = re.compile(pat)
    urlList = re_url.findall(htmlStr)
    urlList = list(set(urlList))

    pat = r"[0-9]\d{4,10}"
    re_qq = re.compile(pat)
    qqList = re_qq.findall(htmlStr)
    #去重
    qqList = list(set(qqList))
    f = open(toPath,"a")
    for qqStr in qqList:
        f.write(qqStr+"\n")
    f.close()


    return urlList

# qqCrawler(url,toPath)

def centerControl(url,toPath):
    queue = deque()

    queue.append(url)
    while len(queue) != 0:
        targetUrl = queue.popleft()
        urlList = qqCrawler(targetUrl,toPath)
        for item in urlList:
            tempUrl =item[0]
            queue.append(tempUrl)

url = r"https://www.douban.com/group/topic/110094603/"
toPath = r"G:\python_learn\pycharm_learn\Python-TrainingCourseLearning\day014\file\qqfile.txt"

centerControl(url,toPath)

'''
    writeFileBytes(htmlBytes,r"G:\python_learn\pycharm_learn\Python-TrainingCourseLearning\day014\file\file1.html")
    writeFileStr(htmlBytes,r"G:\python_learn\pycharm_learn\Python-TrainingCourseLearning\day014\file\File2.txt")
'''







