#发邮件的库
import smtplib
#文本
from email.mime.text import MIMEText

#SMTP服务器
SMTPServer = "smtp.163.com"

#发邮件的地址
Sender = "gongxc_8@163.com"
#发送者邮箱的密码
passwd = "gxc140225"

#设置发送的内容
message = "国之大事"
#转换为邮件文本
msg = MIMEText(message)
#标题
msg["Subject"] = "请接收"
#发送至
msg["From"] = Sender

#收件人
# 创建SMTP服务器
#           需要邮箱的服务smtp.SMTP
#                                   #设置端口号,0-65535被系统占用
mailServer = smtplib.SMTP(SMTPServer,25)

#登录邮箱
mailServer.login(Sender,passwd)
#发送邮件
                            #[发送邮箱，接收邮箱]
mailServer.sendmail(Sender,["gongxc_8@163.com","420835785@qq.com",],msg.as_string())
#退出邮箱
mailServer.quit()
