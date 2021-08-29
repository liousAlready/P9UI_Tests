# -*- coding: utf-8 -*-
# @Time    : 2021/8/29 9:30 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : email_demo.py
# @Software: PyCharm
# @desc : 发送邮件demo


import os
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

# 邮件服务器地址
smtp_server = "smtp.qq.com"
# 邮箱名
smtp_sender = "1650503480@qq.com"
# 授权码
smtp_sender_password = "tnmwuuycifiedcah"
# 收件人
smtp_receiver = " 1650503480@qq.com"
# 抄送人
smtp_cc = "1695403591@qq.com"
# 邮件逐条
smtp_subject = " 自动化测试报告（测试版）"

smtp_body = "来自自动化测试的结果"

# 邮件文本消息
msg = MIMEText(smtp_body, 'html', 'utf-8')  # 邮件消息对象
msg['from'] = smtp_sender  # 发送者
msg['to'] = smtp_receiver  # 接受者
msg['Cc'] = smtp_cc  # 抄送者
msg['subject'] = smtp_subject

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user=smtp_sender, password=smtp_sender_password)
smtp.sendmail(smtp_sender, smtp_receiver.split(",") + smtp_cc.split(","), msg.as_string())
