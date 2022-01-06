# @Time    : 2022/1/5 16:14
# @Author  : hexios
# @Email   : hexiosr@outlook.com
# @File    : timer.py

from urllib import request
import time
import datetime
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def fun():
    now_time = datetime.datetime.now()
    print('---------------------------')
    print(now_time)
    try:
        with request.urlopen(
                "http://81.68.209.220/1"
        ) as file:
            print(file.status)
            print(file.reason)
    except Exception as e:
        print(e)


def sleep(hour, min, sec):
    return hour * 3600 + min * 60 + sec


# 定时
seconds = sleep(0, 0, 1)
while True:
    time.sleep(seconds)
    fun()
