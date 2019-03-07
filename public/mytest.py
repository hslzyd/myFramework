# coding=utf-8
"""
测试类的基类，继承自unittest.Testcase
定义测试套件，打开哪个浏览器
"""

import unittest
from public import mypage
from utils import logger


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = logger.Logger(cls.__name__).getlog()
        cls.logger.info("############################## Test Start ##############################")
        cls.mp = mypage.MyPage()
        cls.mp.max_window()

    @classmethod
    def tearDownClass(cls):
        cls.mp.quit()
        cls.logger.info("############################### Test End ###############################")
