# coding=utf-8
from public import basepage


class SSCAT(basepage.BasePage):

    def open_sscat(self):
        u"""打开sscat"""
        self.driver.open_url("https://sscat.in/user/index.php")

    def login(self):
        u"""登录"""
        self.driver.type("id=>email", "hslzyd@163.com")
        self.driver.type("id=>passwd", "123654789zyd")
        self.driver.click("id=>login")

    def checkin(self):
        u"""签到"""
        self.driver.click("id=>checkin")

    def get_checkin_msg(self):
        self.driver.get_text("id=>checkin-msg")
