# @Time    : 2022/1/5 16:14
# @Author  : hexios
# @Email   : hexiosr@outlook.com
# @File    : timer.py

from urllib import request
import time
import ssl
import logging_config

ssl._create_default_https_context = ssl._create_unverified_context

logger = logging_config.Config().get_config()


def fun():
    try:
        with request.urlopen(
                "http://81.68.209.220/"
        ) as file:
            if file.status == 200:
                logger.info(file.status)
                logger.info(file.read())
                logger.info('不发短信 ')
    except Exception as e:
        logger.info(' 发短信')
        logger.info(e)


def sleep(hour, min, sec):
    return hour * 3600 + min * 60 + sec


# 定时
seconds = sleep(0, 0, 1)
print()
while True:
    time.sleep(seconds)
    fun()
