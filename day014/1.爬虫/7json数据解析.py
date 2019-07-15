'''
概念：一种保存数据的格式
作用：可以保存本地的json文件，也可以将json串进行传输，通常将json称为轻量级的传输方式
json组成
{}      代表对象（字典）
[]      代表列表
:       代表键值对
,       代表两个部分

'''
import json

'''
#1
#将json格式的字符串转为python数据类型的对象
jsonStr = '{"name":"sunck凯","age":18,"hobby":["money","ppower","english"],"parames":{"a":1,"b":2}}'
jsonData = json.loads(jsonStr)
print(jsonData)
print(type(jsonData))
print(jsonData["hobby"])
'''

'''
#2
#将python数据类型的对象转为json格式的字符串
jsonData2 = {"name":"sunck凯","age":18,"hobby":["money","ppower","english"],"parames":{"a":1,"b":2}}
jsonstr2 = json.dumps(jsonData2)
print(jsonstr2)
print(type(jsonstr2))
'''

'''
#3
#读取本地的json文件
path1 = r"G:\python_learn\pycharm_learn\pythonlearn\day014\file\a.json"
with open(path1,"rb") as f:
    #json.load()不加s读本地
    data = json.load(f)
    print(data)
    #字典类型
    print(type(data))
'''

'''
#4
#写本地json
path2 = r"G:\python_learn\pycharm_learn\pythonlearn\day014\file\b.json"
jsonStr = {"name":"sunck凯","age":18,"hobby":["money","ppower","english"],"parames":{"a":1,"b":2}}
#将字典写入文件，变为json
with open(path2,"w") as f:
    #将jsonStr写入f
    json.dump(jsonStr,f)
'''















