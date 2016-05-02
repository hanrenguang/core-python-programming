#!usr/bin/env python
# -*- coding: utf-8 -*-

# 输入Email地址和口令:
from_addr = raw_input('From: ')
password = raw_input('Password: ')
# 输入SMTP服务器地址:
smtp_server = raw_input('SMTP server: ')
# 输入收件人地址:
to_addr = raw_input('To: ')

import smtplib
from email.mime.text import MIMEText
from email.header import Header
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("hanrenguang@outlook.com", 'utf-8')
message['To'] =  Header("coderhangg@163.com", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
try:
    server = smtplib.SMTP(smtp_server, 587) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], message.as_string())
    server.quit()
except:
    print "error"
