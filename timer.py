# @Time    : 2022/1/5 16:14
# @Author  : hexios
# @Email   : hexiosr@outlook.com
# @File    : timer.py

from urllib import request
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def fun():
    try:
        with request.urlopen(
                "https://www.baidu.com/"
        ) as file:
            print(file.status)
            print(file.reason)
            print('-------')
    except Exception as e:
        print(e)


def sleep(hour, min, sec):
    return hour * 3600 + min * 60 + sec


seconds = sleep(0, 0, 3)
while 1 == 1:
    time.sleep(seconds)
    fun()
