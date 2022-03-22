# @Author  : hexios
# @Email   : hiskying@icloud.com
# @Time    : 2022/3/22 17:31
# @File    : sms.py

from twilio.rest import Client

import logging_config

logger = logging_config.Config().get_config()

# Your Account SID from twilio.com/console
account_sid = "xxxxxx"
# Your Auth Token from twilio.com/console
auth_token = "xxxxxxxx"

client = Client(account_sid, auth_token)


def sms1():
    message = client.messages.create(
        to="+xxxxxx",
        from_="+xxxxxx",
        body="系统出现问题！")
    logger.info("短信发送成功！")
    print('短信发送成功!')
