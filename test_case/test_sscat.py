# coding=utf-8

from public import mytest
from pages import sscat
from time import sleep


class TestSscat(mytest.MyTest):

    def test_checkin(self):
        ss = sscat.SSCAT(self.driver)
        ss.open_sscat()
        ss.login()
        ss.checkin()
        sleep(1)
        msg = ss.get_checkin_msg()
        sleep(2)
        self.assertIn(u"流量", msg)
