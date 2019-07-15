import urllib.request
import ssl
import json

def ajaxCrawler(url):
    header = {
        "User-Agent":"Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/54.0.2840.99 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=header)
    #使用ssl创建未验证的上下文
    context = ssl._create_unverified_context()

    response = urllib.request.urlopen(req,context=context)
    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)
    return jsonData

'''
url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20"
info = ajaxCrawler(url)
print(info)
'''

for i in range(1,10):
    url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start="+str(i*20)+""
    info = ajaxCrawler(url)
    print(info)











#报错，因为https协议






























