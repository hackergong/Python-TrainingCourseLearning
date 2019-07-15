import urllib.request

urllib.request.urlretrieve("http://www.baidu.com",filename=r"G:\python_learn\pycharm_learn\pythonlearn\day014\file\file2.html")


#urlretrieve在执行的过程中，会产生一些缓存
#清除缓存
urllib.request.urlcleanup()






