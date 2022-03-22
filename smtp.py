# @Author  : hexios
# @Email   : hiskying@icloud.com
# @Time    : 2022/3/21 16:01
# @File    : smtp.py

import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 发件人邮箱账号
mail_user = 'xxxx@qq.com'

# 发件人邮箱密码，为授权码一般为非登录密码
mail_pass = 'xxxxx'

# 设置接收邮件
receivers = ['xxxx@icloud.com,xxxx@outlook.com,xxxx@88.com']

# 邮件内容
mail_msg = """
qqq
"""

# 邮件内容，文本格式，把plain改成html是html格式
message = MIMEText(mail_msg, 'html', 'utf-8')
# 显示的发件人
message['From'] = mail_user
# 显示的收件人
message['To'] = ','.join(receivers)
message['Subject'] = Header('系统出现问题了！', 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(mail_user, message['To'].split(','), message.as_string())
    smtpObj.quit()
    print("邮件发送成功！")
except smtplib.SMTPException:
    print("Error: 邮件发送失败！")