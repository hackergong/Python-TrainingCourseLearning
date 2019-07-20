def run():
    #空变量，存储的作用data始终为空
    data = ""
    r = yield data
    #r = a
    print(1,r,data)
    r = yield data
    #r = b
    print(2,r,data)
    r = yield data
    #r = c
    print(3,r,data)


#协程的最简单风格，控制函数的阶段执行，节约线程或者进程的切换
#返回值是一个生成器
m = run()
print(m.send(None))
print(m.send("a"))
print(m.send("b"))
print(m.send("c"))