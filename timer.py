# coding=UTF-8
# @Time    : 2022/1/5 16:14
# @Author  : hexios
# @Email   : hexiosr@icloud.com
# @File    : timer.py

import ssl
import time
from urllib import request

import logging_config
import smtp

ssl._create_default_https_context = ssl._create_unverified_context
logger = logging_config.Config().get_config()


def fun():
    try:
        with request.urlopen(
                "http://81.68.209.220:25555/123"
        ) as file:
            if file.status == 200:
                logger.info(file.status)
                logger.info(file.read())
                logger.info('不发送 ')
    except Exception as e:
        smtp.emails()
        logger.info(' 发送')
        logger.info(e)


# 定时函数
def sleep(hour, min, sec):
    return hour * 3600 + min * 60 + sec


# 定时
seconds = sleep(12, 0, 0)
print()
while True:
    time.sleep(seconds)
    fun()
