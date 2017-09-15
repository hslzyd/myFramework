# coding=utf-8
"""
by huangsl
日志类，指定fielHandler和streamHandler将日志保存到文件以及控制台输出
调用时，如：logger.info(string)将string记录为INFO级别的日志
"""
import logging
import os.path
import time


class Logger(object):
    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建fileHandler，保存日志到日志文件
        now = time.strftime("%Y%m%d%H%M%S")
        log_path = os.getcwd() + '\\logs\\'
        log_name = log_path + now + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 创建streamHandler，在控制台输出日志
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义输出格式formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
