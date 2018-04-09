# coding=utf-8
"""
测试页面对象，只需要写定位和操作的函数，供测试类调用
"""

from public import basepage


class Bing(basepage.BasePage):

    def open_bing(self):
        """打开bing"""
        self.driver.open_url("http://www.bing.com")

    def search(self, keyword):
        self.driver.clear_type("id=>sb_form_q", keyword)
        self.driver.click("id=>sb_form_go")

    def get_title(self):
        """获取页面title"""
        return self.driver.get_page_title()
