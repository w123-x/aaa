import sys,os
sys.path.append(os.getcwd()+r'\ranzhi')
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from util import Email
print(os.getcwd()+r'\ranzhi')

Email().send('smtp.163.com',25,'15129983478@163.com','UWARDUWZROHUSRSK','15129983478@163.com','ranzhi自动化测试报告',r'ranzhi\report\report_2020-12-15_19_50_33.html',r'ranzhi\base\body.html')
# #设置邮件服务器地址
# smtpserver='smtp.163.com'
# #设置邮件服务器端口号
# port=25
# #发件人地址
# sender='15129983478@163.com'
# #发件人密码
# password='UWARDUWZROHUSRSK'
# #收件人地址
# receivers='15129983478@163.com'

# #创建邮件对象
# mail=MIMEMultipart()
# #初始化发件人
# mail['from']=sender
# #收件人
# mail['to']=receivers
# #添加主题
# mail['subject']='Ranzhi自动化测试报告'

# #读取报告内容
# path=r'ranzhi/report/report_2020-12-15_19_50_33.html'
# with open(path,'rb')as file:
#     report=file.read()

# #对附件进行编码(report是以二进制形式读进来的)
# attachment=MIMEText(report,'base64','utf-8')#base64编码格式
# #设置附件的类型(attachment:附件)
# attachment['Content-Type']='application/octet-stream'
# #设置附件的处理方式(浏览器的处理方式)disposition:显示
# attachment['Content-Disposition']='attachment;filename=%s'%path.split('/')[-1]
# #添加附件
# mail.attach(attachment)

# #生成邮件正文
# content='''
# <p>Dear Mike,</p>
# <p>&nbsp;&nbsp;这是ranzhi自动化测试报告，请查收!</p>
# <p>此致</p>
# <p>Tom</p>
# '''
# #对邮件正文进行编码
# body=MIMEText(content,'html','utf-8')
# #添加正文
# mail.attach(body)

# #创建SMTP对象(用来连接服务器)
# smtp=smtplib.SMTP()
# #连接服务器
# smtp.connect(smtpserver,port)
# #登录服务器
# smtp.login(sender,password)
# #发送邮件
# smtp.sendmail(sender,receivers.split(';'),mail.as_string())
# #关闭服务器
# smtp.close()
# print('邮件发送完毕！')


