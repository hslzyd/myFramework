# coding=utf-8


class BasePage(object):
    """
    所有页面的基类
    """
    def __init__(self, driver):
        self.driver = driver
