import urllib.request
import random


url = "http://www.baidu.com"

'''
#模拟请求头
headers = {
    "Accept":"application/json,text/javascript,*/*;q=0.01",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
}
#设置一个请求体
req = urllib.request.Request(url,headers=headers)
#发起请求
response = urllib.request.urlopen(req)

data = response.read().decode("utf-8")
print(data)
'''



agentsList = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]

agentStr = random.choice(agentsList)
req = urllib.request.Request(url)
#向请求体里添加了User-Agent
req.add_header("User-Agent",agentStr)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))






#user-Agent













