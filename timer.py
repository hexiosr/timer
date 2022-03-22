# coding=UTF-8
# @Time    : 2022/1/5 16:14
# @Author  : hexios
# @Email   : hexiosr@icloud.com
# @File    : timer.py

import ssl
import time
from urllib import request

import logging_config
import sms
import smtp

ssl._create_default_https_context = ssl._create_unverified_context
logger = logging_config.Config().get_config()


def fun():
    try:
        with request.urlopen(
                "http://81.68.209.220:25555/1111.html"
        ) as file:
            if file.status == 200:
                print('正常')
                logger.info(file.status)
                logger.info(file.read())
    except Exception as e:
        print('异常')
        smtp.emails()  # 邮件
        sms.sms1()  # 短信
        logger.info(e)


# 定时函数
def sleep(hour, min, sec):
    return hour * 3600 + min * 60 + sec


# 定时
seconds = sleep(0, 0, 10)
print()
while True:
    time.sleep(seconds)
    fun()
