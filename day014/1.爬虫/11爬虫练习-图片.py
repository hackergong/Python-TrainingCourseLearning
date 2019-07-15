
import urllib.request
import re
import os


def imageCrawler(url,toPath):
    headers = {
        "User-Agent":"Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/54.0.2840.99 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    HTMLStr = response.read().decode("utf-8")


    # with open(r"G:\python_learn\pycharm_learn\pythonlearn\day014\file\yhd.html","wb") as f:
        # f.write(HTMLStr)

    pat = r'<img original="//(.*?)" />'
    re_image = re.compile(pat)
    imageList = re_image.findall(HTMLStr)
    # print(imageList)
    # print(len(imageList))
    # print(imageList[0])

    num = 1
    for imageUrl in imageList:
        path = os.path.join(toPath,str(num)+".jpg")
        num += 1
        #把图片下载到本地存储
        urllib.request.urlretrieve("https://"+imageUrl,filename=path)



url = "https://search.yhd.com/c0-0/k%25E8%25BF%259E%25E8%25A1%25A3%25E8%25A3%2599/"

toPath = r"G:\python_learn\pycharm_learn\pythonlearn\day014\file\image"

imageCrawler(url,toPath)














'''
将网页下载，分析网页的组成，然后再构建
'''













