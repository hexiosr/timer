# @Time    : 2022/1/5 16:14
# @Author  : hexios
# @Email   : hexiosr@outlook.com
# @File    : timer.py

from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

try:
    with request.urlopen(
            "https://www.baidu.com/"
    ) as file:
        print(file.status)
        print(file.reason)
except Exception as e:
    print(e)
