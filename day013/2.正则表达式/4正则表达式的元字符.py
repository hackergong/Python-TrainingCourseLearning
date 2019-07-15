import re

print("----------匹配单个字符与数字----------")
'''
.               匹配除换行符以外的任意字符
[0123456789]    []是字符集合，表达匹配方括号中所包含的任意一个字符
[tracy]         匹配't','r','a','c','y'中任意一个字符
[a-z]           匹配任意小写字母
[A-Z]           匹配任意大写字母
[0-9]           匹配任意数字，类似[0123456789]
[0-9a-zA-Z]     匹配任意的数字和字母
[0-9a-zA-Z_]    匹配任意的数字,字母和下划线
[^tracy]        匹配除了tracy这几个字母以外的所有字符，中括号里的^称为脱字符，表示不匹配集合中的字符
[^0-9]          匹配所有的非数字字符
\d              匹配数字，效果同[0-9]
\D              匹配非数字符，效果同[^0-9]
\w              匹配数字，字母和下划线，效果同[0-9a-zA-Z_]
\W              匹配非数字，字母和下划线，效果同[^0-9a-zA-Z_]
\s              匹配任意的空白符(空格，换行，回车，换页，制表),效果同[\f\r\n\t]
\S              匹配任意的非空白符，效果同[^ \f\n\r\t]

'''
print(re.findall("\d","sUnck ! is 6 a go3od man2"))




print("----------锚字符(边界字符)----------")
'''
^       行首匹配，和在[]里的^不是一个意思
$       行尾匹配

\A      匹配字符串开始，它和^的区别是，\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配其它行的行首

\Z      匹配字符串结束，它和$的区别是，\Z只匹配整个字符串的结尾，即使在re.M模式下也不会匹配其它行的行尾

\b      匹配一个单词的边界，也就是指单词和空格间的位置
（'er\b' 可以匹配never ，但是不能匹配nerve）
\B      匹配非单词边界
('er\B'  可以匹配不是单词边界的，如nerve)

'''

# print(re.search("^tracy","tracy is a good man"))

print(re.findall("^tracy","tracy is a good man\ntracy is a nice man",re.M))
print(re.findall("\Atracy","tracy is a good man\ntracy is a nice man",re.M))

print(re.findall("man$","tracy is a good man\ntracy is a nice man",re.M))
print(re.findall("man\Z","tracy is a good man\ntracy is a nice man",re.M))

print(re.search(r"er\b","never   "))
print(re.search(r"er\b","nerve"))
print(re.search("er\B","never"))
print(re.search("er\B","nerve"))




print("----------匹配多个字符----------")
'''
说明：下方的x,y,z均为假设的普通字符(n,m为非负整数)，不是正则表达式的元字符
(xyz)       匹配小括号内的xyz(作为一个整体去匹配)
x?          匹配0个或者1个x
x*          匹配0个或者任意多个x(.*表示匹配0个或者任意多个字符(换行符除外))
x+          匹配至少一个x
x{n}        匹配确定的n个x(n是一个非负整数)
x{n,}       匹配至少n个x
x{n,m}      匹配至少n个最多m个x。注意：n<=m
x|y         |表  示或，匹配的是x或y

'''


print(re.findall(r"(tracy)","tracyis a good man,tracy is a nice man"))
print(re.findall(r"a?","aaa"))#非贪婪匹配（尽可能少的匹配）
print(re.findall(r"a*","aaaabbba")) #贪婪匹配（尽可能多的匹配）
print(re.findall(r".*","aaaabbba"))  #全部匹配
print(re.findall(r"a+","aaaabbba")) #贪婪匹配（尽可能多的匹配）
print(re.findall(r"a{3}","aaaabbba"))  #['aaa']
print(re.findall(r"a{3}","aa"))   #小于三个，无法匹配
print(re.findall(r"a{3}","aaaabbbaaaa"))    #[取三个
print(re.findall(r"a{3,}","aaaabbbaaaa"))   #至少三个
print(re.findall(r"a{2,3}","aaaabbbaaaa"))  #至少2个，最多3个
print(re.findall(r"((t|T)racy)","tracy--Tracy"))


print("----------------特殊----------------")
'''
*?  +?  x?     最小匹配,通常都是尽可能多的匹配，可以使用这种解决贪婪匹配

(?:x)           类似(xyz)，但不表示一个组



'''
#需求，提取sunck.....man
str = "tracy is a good man! tracy is a nice man!tracy is a handsome man"
print(re.findall(r"^tracy.*?man$",str))
print(re.findall(r"tracy.*?man",str))
#注释：/* part*/  /* part1 */
print(re.findall(r"//*.*?/*/","/* part1*/  /* part1 */"))
#第二个/将*转义，  .*表示任意多个， /将*转义, ?最少个















































































































