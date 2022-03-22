# @Author  : hexios
# @Email   : hiskying@icloud.com
# @Time    : 2022/3/21 16:01
# @File    : smtp.py

import smtplib
from email.header import Header
from email.mime.text import MIMEText

import logging_config

logger = logging_config.Config().get_config()

# 发件人邮箱账号
mail_user = 'xxx@qq.com'
# 发件人邮箱密码，为授权码一般为非登录密码
mail_pass = 'xxx'
# 设置接收邮件
receivers = ['xxx@icloud.com']
# 邮件内容
mail_msg = "系统出现异常！"

# 邮件内容，文本格式，把plain改成html是html格式
message = MIMEText(mail_msg, 'html', 'utf-8')
# 显示的发件人
message['From'] = mail_user
# 显示的收件人
message['To'] = ','.join(receivers)
message['Subject'] = Header('系统出现异常！', 'utf-8')


def emails():
    try:
        smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
        smtp.login(mail_user, mail_pass)
        smtp.sendmail(mail_user, message['To'].split(','), message.as_string())
        smtp.quit()
        logger.info("邮件发送成功！")
        print("邮件发送成功！")
    except smtplib.SMTPException:
        logger.info("邮件发送失败！")
        print("Error: 邮件发送失败！")
