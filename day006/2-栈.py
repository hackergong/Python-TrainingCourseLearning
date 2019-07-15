'''
栈：stack 先进后出表

'''
#模拟栈结构
stack = []

#进栈（存数据）
stack.append("A")
stack.append("B")
stack.append("C")
print(stack)

#出栈（取数据）
res1 = stack.pop()
print("res =",res1)
print(stack)

