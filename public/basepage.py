# coding=utf-8


class BasePage(object):
    """
    所有页面的基类，测试页面继承这个类而不是继承自mypage
    这样的话，在用例类中，实例化的测试页面对象便无法直接访问mypage中的方法
    """
    def __init__(self, driver):
        self.driver = driver
