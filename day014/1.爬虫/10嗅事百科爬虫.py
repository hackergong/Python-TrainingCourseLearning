import urllib.request
import ssl
import re

def jokeCrawler(url):
    header = {
        "User-Agent":"Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/54.0.2840.99 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=header)
    #使用ssl创建未验证的上下文
    context = ssl._create_unverified_context()

    response = urllib.request.urlopen(req)
    # HTML = str(response.read()) 用于计算有多少个
    HTML = response.read().decode("utf-8")

    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    re_joke = re.compile(pat,re.S)  #re.S匹配换行
    divList = re_joke.findall(HTML)
    # print(len(dicList))
    # print(dicList)
    dict_jock = {}
    for div in divList:
        #用户名
        re_u = re.compile(r"<h2>(.*?)</h2>",re.S)
        username = re_u.findall(div)
        username = username[0]
        #段子
        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>',re.S)

        Before_duanzi = re_d.findall(div)
        Before_duanzi = Before_duanzi[0]
        delete_space = re.compile(r'\s+')
        duanzi = re.sub(delete_space,'',Before_duanzi)
        print(duanzi)
        dict_jock[username] = duanzi

    return dict_jock
'''
    with open(r"G:\python_learn\pycharm_learn\pythonlearn\day014\file\file3.html","w",encoding="utf-8") as f:
        f.write(HTML)
'''

url = "https://www.qiushibaike.com/text"
info = jokeCrawler(url)

path = r"G:\python_learn\pycharm_learn\pythonlearn\day014\file\joke.txt"
path1 = r"G:\python_learn\pycharm_learn\pythonlearn\day014\file\joke1.txt"
f = open(path,"w",encoding="utf-8")
for k,v in info.items():
    f.write(k)
    f.write(str(v))
f.close()

'''
with open(path,"r",encoding="utf-8") as f:
    data = f.read()
    delete_space = re.compile(r'\s+')
    outdata = re.sub(delete_space,'',data)
    with open(path1,'w',encoding="utf-8") as f:
        f.write(outdata)
'''















