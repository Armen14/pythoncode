#!usr/bin/python
#-*- coding:utf-8 -*-

import string
import smtplib
from email.MIMEText import MIMEText

################################################
I = 'armen.ubuntu.krokodil625@gmail.com'
You = 'armen153@yandex.ru'

message = 'Привет, как дела?'
subject = 'Письмо тест'
################################################
################################################
#SMTP-server
server_smtp = "smtp.gmail.com"
port = 25

user_name = "armen.ubuntu.krokodil625@gmail.com"
user_password = "blxalpha0.5"
#################################################
#################################################
#created message
msg = MIMEText(message, "", "utf-8")
msg['Subject'] = subject
msg['From'] = I
msg['To'] = You
#################################################
#################################################
#sender
send = smtplib.SMTP(server_smtp, port)
send.ehlo()
send.starttls()
send.ehlo()
send.login(user_name, user_password)
send.sendmail(I, You, msg.as_string())
send.quit()
#################################################
