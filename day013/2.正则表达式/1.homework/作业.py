'''
作业
QQ     6666-12345678901
mail   tracy@163.com
phone 010-55348765
user  数字字母下划线6-12位
ip
paswd
url

'''
#阿里云服务器
#QQ     6到10位，全是数字
import re

re_QQ = re.compile(r"^[1-9]\d{5,10}$")
print(re_QQ.search("12345670dsf"))

re_telephone = re.compile(r"([0-9]{3})-?([0-9]{8})")
print(re_telephone.findall("fdsfds123-23453214dfsf45612345678s"))

re_user = re.compile(r"^[0-9a-zA-Z][0-9a-zA-Z_]{5,11}")
print(re_user.findall("2b3edxd124_"))
print(re_user.findall("_1bd2gk"))
print(re_user.findall("a3_sdf"))

#255.255.255.255
re_ip = re.compile(r"(^[0-9]{1,3}(.)[0-9]{1,3}(.)[0-9]{1,3}(.)[0-9]{1,3})")
print(re_ip.search("123.24.2.2"))

#url
re_url = re.compile(r"((www)(.).*(.)(com|cn|org))")

print(re_url.search("www.baidu.com2341"))
print(re_url.search("www.b_aidd23u.cn"))


#passwd
# re_passwd = re.compile((r""))