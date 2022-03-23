# coding=UTF-8
# @Time    : 2022/1/5 17:14
# @Author  : hexios
# @Email   : hexiosr@icloud.com
# @File    : logging_config.py

import logging.handlers


class Config:
    # creating a logger对象
    logger = logging.getLogger('mylogger')

    # define the default level of the logger
    logger.setLevel(logging.INFO)

    # creating a formatter
    LOG_FILE = 'default.log'
    formatter = logging.Formatter('%(asctime)s | %(levelname)s -> %(message)s')
    file_handler = logging.handlers.RotatingFileHandler("log/default.log", maxBytes=1024 * 1024 * 5, backupCount=5,
                                                        encoding='UTF-8')

    # creating a handler to log on the filesystem
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    # adding handlers to our logger

    logger.addHandler(file_handler)

    # logger.info('this is a log message...')

    def get_config(self):
        return self.logger
