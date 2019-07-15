#判断手机号码
'''
def checkPhone(str):
    if len(str)!=11:
        return False
    elif str[0] !="1":
        return False
    elif str[1:3] !="39" and str[1:3] != "31":
        return False
    for i in range(3,11):
        if str[i]<"0" or str[i]>"9":
            return False
    return True


print(checkPhone("13912334567"))
print(checkPhone("13123434567"))
print(checkPhone("13024567564"))
'''
import re
'''



def checkPhone2(str):
    #13912345678
    # pat = r"^1[3578]\d{9}"
    pat = r"^1(([3578]\d)|(47))\d{8}"
    res = re.match(pat,str)
    return res
print(checkPhone2("13912334567"))
print(checkPhone2("15123434567"))
print(checkPhone2("14724567564"))
print(checkPhone2("12344567533"))
'''


def checkPhone2(str):
    #13912345678
    # pat = r"^1[3578]\d{9}"
    pat = r"(1(([3578]\d)|(47))\d{8})"
    res = re.match(pat,str)
    return res


print(checkPhone2("sdfklfjlsdjfls13709897656sdjflsdj14732345678dsfsdf"))




















