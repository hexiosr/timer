# coding=UTF-8
# @Time    : 2022/1/5 16:14
# @Author  : hexios
# @Email   : hexiosr@icloud.com
# @File    : timer.py
import smtplib
import ssl
import time
from email.header import Header
from email.mime.text import MIMEText
from urllib import request

from twilio.rest import Client

import config
from config import logging_config

ssl._create_default_https_context = ssl._create_unverified_context
logger = logging_config.Config().get_config()


def fun():
    try:
        with request.urlopen(
                "http://81.68.209.220:25555/1111.html"  # 接口
        ) as file:
            if file.status == 200:
                print('正常')
                logger.info(file.status)
                logger.info(file.read())
    except Exception as e:
        print('异常')

        # 邮件提醒
        # 邮件内容，文本格式，把plain改成html是html格式
        message = MIMEText(config.mail_msg + f'{e}!', 'html', 'utf-8')
        # 显示的发件人
        message['From'] = config.mail_user
        # 显示的收件人
        message['To'] = ','.join(config.receivers)
        message['Subject'] = Header('系统出现异常！', 'utf-8')
        smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
        smtp.login(config.mail_user, config.mail_pass)
        smtp.sendmail(config.mail_user, message['To'].split(','), message.as_string())
        smtp.quit()
        logger.info("邮件发送成功！")

        # 短信提醒
        client = Client(config.account_sid, config.auth_token)
        message = client.messages.create(
            to="+xxxx",
            from_="+xxxx",
            body="系统出现异常：" + f'{e} !')
        logger.info("短信发送成功！")
        logger.info(e)
        print(message.sid)
        print("短信，邮件发送成功！")


# 定时函数
def sleep(hour, min, sec):
    return hour * 3600 + min * 60 + sec


# 定时
seconds = sleep(0, 0, 10)
print()
while True:
    time.sleep(seconds)
    fun()
