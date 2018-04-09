# coding=utf-8
"""
测试类，继承myTest
"""

from public import mytest
from pages import bing
from time import sleep


class TestBing(mytest.MyTest):

    def test_search(self):
        bs = bing.Bing(self.driver)
        bs.open_bing()
        bs.search("selenium")
        sleep(3)
        title = bs.get_title()
        self.assertIn('selenium', title)
