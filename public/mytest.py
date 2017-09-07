# coding=utf-8
"""
测试类的基类，继承自unittest.Testcase
定义测试套件，打开哪个浏览器
"""

import unittest
from public import mypage
from public import logger


class MyTest(unittest.TestCase):
    def setUp(self):
        self.logger = logger.Logger("MyTest").getlog()
        self.logger.info("############################## Test Start ##############################")
        self.driver = mypage.MyPage()
        self.driver.max_window()

    def tearDown(self):
        self.driver.quit()
        self.logger.info("##############################  Test End  ##############################")
