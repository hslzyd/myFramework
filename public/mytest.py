# coding = utf-8

import unittest
from public import module
from public import logger


class MyTest(unittest.TestCase):
    def setUp(self):
        self.logger = logger.Logger("MyTest").getlog()
        self.logger.info("############################## Test Start ##############################")
        self.driver = module.Module('Firefox')
        self.driver.max_window()

    def tearDown(self):
        self.driver.quit()
        self.logger.info("##############################  Test End  ##############################")
