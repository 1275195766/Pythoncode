
import poplib
import smtplib
from email.header import decode_header
from email.mime.text import MIMEText
import email


#如何登陆邮箱
sent=smtplib.SMTP_SSL('smtp.qq.com',465)#这一行设置了SMTP服务器为smtp.qq.com
sent.login('1275915766@qq.com','jpdfdemxwjlkjgdc')#这里一定注意，若有独立密码则填独立密码


#发送邮件
#上面已经登陆了，现在需要设置发送内容，然后发送即可
#to=['1287594867@qq.com','35662429@qq.com','569898888@qq.com','wuyaoxue@outlook.com','1521479251@qq.com']
to=['wuyaoxue@outlook.com','1521479251@qq.com']
content=MIMEText('这是测试，收到邮件回我一个消息呗^_^')#MIMEText的参数代表邮件的具体内容
content['Subject']='测试'#这里设置邮件标题
content['From']='1275915766@qq.com'#这里设置邮件从哪里发送
content['To']=','.join(to)#这里设置邮件发送的地址，可以群发
sent.sendmail('1275915766@qq.com',to,content.as_string())#这一步实现发送邮件,有三个参数，需要注意各参数代表什么
print "发送成功"
sent.close()
