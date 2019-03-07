# coding=utf-8
"""
by huangsl
封装selenium常用方法的page类
"""

import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from utils.logger import Logger
from selenium.webdriver.support.ui import Select
from utils.browser import Browser
from utils.config import Config, SCREENSHOT_PATH, TEMP_PATH

success = "SUCCESS    "
fail = "FAIL    "
now_time = time.strftime("%Y%m%d%H%M%S")


class MyPage(object):

    def __init__(self):
        self.log = Logger(logger=self.__class__.__name__)
        self.logger = self.log.get_log()

        br_type = Config().get("browser", "name")
        self.driver = Browser(br_type).get_driver()
        self.logger.info("%s启动%s浏览器" % (success, br_type))

        if not os.path.exists(TEMP_PATH):
            os.mkdir(TEMP_PATH)

    def back(self):
        self.driver.back()
        self.logger.info("点击浏览器后退按钮")

    def forward(self):
        self.driver.forward()
        self.logger.info("点击浏览器前进按钮")

    def open_url(self, url):
        self.driver.get(url)
        self.logger.info("打开站点 %s" % url)

    def wait(self, secs):
        time.sleep(secs)
        self.logger.info("等待 %.2f 秒" % secs)

    def take_screenshot(self):
        if not os.path.exists(SCREENSHOT_PATH):
            os.mkdir(SCREENSHOT_PATH)
        file_name = SCREENSHOT_PATH + '/' + now_time + '.png'
        try:
            self.driver.get_screenshot_as_file(file_name)
            self.logger.info("%s已截图保存为：%s" % (success, file_name))
            return file_name
        except NameError as e:
            self.logger.error("%s截图失败，错误：%s" % (fail, e))
            self.take_screenshot()

    def find_element(self, selector):
        """
        封装的元素定位方法, 入参selector格式为"by=>value"
        :param selector:
        :return element:
        """
        if '=>' not in selector:
            raise NameError("格式错误，请按此格式输入：by=>value")

        selector_by = selector.split('=>')[0].strip()
        selector_value = selector.split('=>')[1].strip()

        # by_id
        if selector_by == "id":
            element = self.driver.find_element_by_id(selector_value)
            self.logger.info("%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        # by_name
        elif selector_by == "name":
            element = self.driver.find_element_by_name(selector_value)
            self.logger.info("%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        # by_class_name
        elif selector_by == "class_name":
            element = self.driver.find_element_by_class_name(selector_value)
            self.logger.info("%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        # by_link_text
        elif selector_by == "link_text":
            element = self.driver.find_element_by_link_text(selector_value)
            self.logger.info("%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        # by_partial_link_text
        elif selector_by == "partial_link_text":
            element = self.driver.find_element_by_type(selector_value)
            self.logger.info("%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        # by_tag_name
        elif selector_by == "tag_name":
            element = self.driver.find_element_by_tag_name(selector_value)
            self.logger.info("%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        # by_xpath
        elif selector_by == "xpath":
            element = self.driver.find_element_by_xpath(selector_value)
            self.logger.info("%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        # by_css_selector
        elif selector_by == "css_selector":
            element = self.driver.find_element_by_css_selector(selector_value)
            self.logger.info("%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        else:
            raise NameError("请输入有效的元素类型")

        return element

    def clear_type(self, selector, text, log_text=True):
        """
        清空输入框后输入
        :param selector:
        :param text:
        :param log_text:是否在log中记录输入值
        :return:
        """
        try:
            self.wait_element(selector)
            elem = self.find_element(selector)
            elem.clear()
            elem.send_keys(text)
            if log_text:
                self.logger.info("%s清空输入框并输入：%s" % (success, text))
            else:
                self.logger.info("%s清空输入框并输入" % success)
        except Exception as e:
            self.logger.error("%s无法往输入框输入，错误：%s" % (fail, e))
            self.take_screenshot()

    def type(self, selector, text, log_text=True):
        """
        不清空输入框直接输入
        :param selector:
        :param text:
        :param log_text:是否在log中记录输入值
        :return:
        """
        try:
            self.wait_element(selector)
            elem = self.find_element(selector)
            elem.send_keys(text)
            if log_text:
                self.logger.info("%s清空输入框并输入：%s" % (success, text))
            else:
                self.logger.info("%s清空输入框并输入" % success)
        except Exception as e:
            self.logger.error("%s无法往输入框输入，错误：%s" % (fail, e))
            self.take_screenshot()

    def clear(self, selector):
        """
        清空输入框
        :param selector:
        :return:
        """
        try:
            self.wait_element(selector)
            elem = self.find_element(selector)
            elem.clear()
            self.logger.info("%s清空输入框" % success)
        except Exception as e:
            self.logger.error("%s无法清空输入框，错误：%s" % (fail, e))
            self.take_screenshot()

    def click(self, selector):
        """
        点击元素
        :param selector:
        :return:
        """
        try:
            self.wait_element(selector)
            elem = self.find_element(selector)
            elem.click()
            self.logger.info("%s点击元素：%s" % (success, selector))
        except Exception as e:
            self.logger.error("%s无法点击元素，错误：%s" % (fail, e))
            self.take_screenshot()

    def right_click(self, selector):
        """
        右键点击元素
        :param selector:
        :return:
        """
        try:
            self.wait_element(selector)
            elem = self.find_element(selector)
            ActionChains(self.driver).context_click(elem).perform()
            self.logger.info("%s右键点击元素：%s" % (success, selector))
        except Exception as e:
            self.logger.error("%s无法右键点击元素%s，错误：%s" % (fail, selector, e))

    def exec_js(self, script):
        """
        执行js语句
        :param script:
        :return:
        """
        try:
            self.driver.execute_script(script)
            self.logger.info("%s执行js：%s" % (success, script))
        except Exception as e:
            self.logger.error("%s执行js<%s>发生错误：%s" % (fail, script, e))

    def max_window(self):
        self.driver.maximize_window()
        self.logger.info("窗口最大化")

    def get_text(self, selector):
        """
        获取元素文本
        :param selector:
        :return:
        """
        try:
            self.wait_element(selector)
            elem_text = self.find_element(selector).text
            self.logger.info("%s获取文本为：%s" % (success, elem_text))
            return elem_text
        except Exception as e:
            self.logger.error("%s获取文本失败，错误：%s" % (fail, e))

    def wait_element(self, selector):
        """
        显式等待元素出现
        :param selector:
        """
        if '=>' not in selector:
            raise NameError("格式错误，请按此格式输入：by=>value")

        selector_by = selector.split('=>')[0].strip()
        selector_value = selector.split('=>')[1].strip()
        message = "元素%s不存在" % selector_value

        if selector_by == 'id':
            WebDriverWait(self.driver, 10, 0.5)\
                .until(ec.presence_of_element_located((By.ID, selector_value)), message)
        elif selector_by == 'name':
            WebDriverWait(self.driver, 10, 0.5)\
                .until(ec.presence_of_element_located((By.NAME, selector_value)), message)
        elif selector_by == 'class_name':
            WebDriverWait(self.driver, 10, 0.5)\
                .until(ec.presence_of_element_located((By.CLASS_NAME, selector_value)), message)
        elif selector_by == 'link_text':
            WebDriverWait(self.driver, 10, 0.5)\
                .until(ec.presence_of_element_located((By.LINK_TEXT, selector_value)), message)
        elif selector_by == 'tag_name':
            WebDriverWait(self.driver, 10, 0.5)\
                .until(ec.presence_of_element_located((By.TAG_NAME, selector_value)), message)
        elif selector_by == 'xpath':
            WebDriverWait(self.driver, 10, 0.5)\
                .until(ec.presence_of_element_located((By.XPATH, selector_value)), message)
        elif selector_by == 'css_selector':
            WebDriverWait(self.driver, 10, 0.5)\
                .until(ec.presence_of_element_located((By.CSS_SELECTOR, selector_value)), message)
        else:
            raise NameError("请输入正确的查找方式，'id','name','class_name','link_text','tag_name','xpath','css'")

    def select(self, selector, select_type, value):
        """
        下拉选择
        :param selector:select元素定位
        :param select_type:select查找方法，有index, value, visible_text
        :param value:要查找的值，对应type，如type是visible_text则查找option显示的文本
        """
        self.wait_element(selector)
        if select_type == "index":
            try:
                Select(self.find_element(selector)).select_by_index(value)
                self.logger.info("%s通过option的<%s>选中第<%s>项" % (success, select_type, value))
            except Exception as e:
                self.logger.error("%s无法通过<%s>选中第<%s>项，错误：%s" % (fail, select_type, value, e))
        elif select_type == "value":
            try:
                Select(self.find_element(selector)).select_by_value(value)
                self.logger.info("%s通过option的<%s>选中<%s>项" % (success, select_type, value))
            except Exception as e:
                self.logger.error("%s无法通过<%s>选中<%s>项，错误：%s" % (fail, select_type, value, e))
        elif select_type == "visible_text":
            try:
                Select(self.find_element(selector)).select_by_visible_text(value)
                self.logger.info("%s通过option的<%s>选中<%s>项" % (success, select_type, value))
            except Exception as e:
                self.logger.error("%s无法通过<%s>选中<%s>项，错误：%s" % (fail, select_type, value, e))
        else:
            raise NameError("请输入正确的查找方法：index, value, visible_text")

    def get_page_title(self):
        """
        获取网页title
        :return: title
        """
        title = self.driver.title
        self.logger.info("%s获取当前网页title为：%s" % (success, title))
        return title

    def move_to(self, selector):
        """
        鼠标移动到元素并停留
        """
        self.wait_element(selector)
        try:
            elem = self.find_element(selector)
            ActionChains(self.driver).move_to_element(elem).perform()
            self.logger.info("%s鼠标移动至元素%s" % (success, selector))
        except Exception as e:
            self.logger.error("%s移动至元素%s失败，错误：%s" % (fail, selector, e))

    def enter(self, selector):
        """
        模拟键盘回车按钮
        """
        self.wait_element(selector)
        elem = self.find_element(selector)
        elem.send_keys(Keys.ENTER)
        self.logger.info("点击回车")

    def operate_alert(self, option="OK"):
        """
        alert弹窗操作
        :param option: 点击确认或取消，"OK"--确认，"Cancel"--取消， 默认点确认
        """
        al = self.driver.switch_to.alert
        if option == "OK":
            al.accept()
            self.logger.info("弹窗点击确认")
        else:
            al.dismiss()
            self.logger.info("弹窗点击取消")

    def switch_window(self, title):
        """
        切换窗口、标签页
        :param title: 窗口、标签title
        :return:
        """
        handlers = self.driver.window_handles
        for handler in handlers:
            self.driver.switch_to.window(handler)
            if self.driver.title == title:
                self.logger.info("切换至<%s>窗口" % title)
                break

    def switch_frame(self, frame):
        """
        切换iframe
        :param frame: iframe的name，id，default--切换至主文档，parent--切换至上一层iframe
        :return:
        """
        if frame == "default":
            self.driver.switch_to.default_content()
            self.logger.info("切换至主文档")
        elif frame == "parent":
            self.driver.switch_to.parent_frame()
            self.logger.info("切换回上一层iframe")
        else:
            self.driver.switch_to.frame(frame)
            self.logger.info("切换至iframe<%s>" % frame)

    def quit(self):
        """
        退出浏览器
        """
        self.driver.quit()
        self.logger.info("退出浏览器")
        self.log.remove_log()


if __name__ == "__main__":
    p1 = MyPage()
    p1.open_url("http://uucenter.uulian.com.cn/register")
    elem = p1.find_element('id=>code')
    code_image = TEMP_PATH + '/code.png'
    elem.screenshot(code_image)
