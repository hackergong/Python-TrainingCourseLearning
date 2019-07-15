import telnetlib

def telnetDoSomething(IP,user,passwd,command):
    try:
        #连接服务器
        telnet = telnetlib.Telnet(IP)
        #设置调试级别
        telnet.net_dubuglevel(2)

        #每个系统的样式都不一样

        #读取输入用户名的信息
        rt = telnet.read_until("Login username:".encode("utf-8"))
        #写入用户名
        telnet.write((user+"\r\n").encode("utf-8"))

        #读取输入密码的信息
        ut = telnet.read_until("Login password:".encode("utf-8"))
        #写入密码
        telnet.write((passwd+"\r\n").encode("utf-8"))

        #读取验证IP
        It = telnet.read_until("Domain name:".encode("utf-8"))
        #写入用户名
        telnet.write((IP+"\r\n").encode("utf-8"))

        #登录成功，写指令
        rt = telnet.read_until(">".encode("utf-8"))
        telnet.write((command+"\r\n").encode("utf-8"))

        #上面命令执行成功，会继续读>
        #失败，一般不会是>
        rt = telnet.read_until(">".encode("utf-8"))
        #断开连接
        telnet.close()
        return True
    except:
        return False


if __name__ == "__main__":
    IP = "10.0.142.197"
    user = "xumingbin"
    passwd = "*****"
    command = "tasklist"
    print(telnetDoSomething(IP,user,passwd,command))