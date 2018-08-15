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
    def setUpClass(self):
        self.logger = logger.Logger(self.__name__).getlog()
        self.logger.info("############################## Test Start ##############################")
        self.driver = mypage.MyPage()
        self.driver.max_window()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        self.logger.info("##############################  Test End  ##############################")
