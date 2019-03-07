# coding=utf-8
"""
by huangsl
日志类，指定fielHandler和streamHandler将日志保存到文件以及控制台输出
调用时，如：logger.info(string)将string记录为INFO级别的日志
"""
import logging
import time
import os
from utils.config import LOG_PATH


class Logger(object):
    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建fileHandler，保存日志到日志文件
        now = time.strftime("%Y%m%d%H%M%S")
        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)
        log_name = LOG_PATH + '/' + now + '.log'
        self.fh = logging.FileHandler(log_name)
        self.fh.setLevel(logging.INFO)

        # 创建streamHandler，在控制台输出日志
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.INFO)

        # 定义输出格式formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)

        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    def get_log(self):
        return self.logger

    def remove_log(self):
        self.logger.removeHandler(self.fh)
        self.logger.removeHandler(self.ch)
