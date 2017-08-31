# coding=utf-8
"""
by huangsl
封装selenium常用方法的page类
"""

import time
import os
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import NoSuchElementException
from public.logger import Logger
from selenium.webdriver.support.ui import Select

success = "SUCCESS    "
fail = "FAIL    "
logger = Logger(logger="BasePage").getlog()
now_time = time.strftime("%Y%m%d%H%M%S")


class Module(object):

    def __init__(self, browser='ff'):
        dr = None
        if browser == "Chrome" or browser == "cr":
            dr = webdriver.Chrome()
        elif browser == "Firefox" or browser == "ff":
            dr = webdriver.Firefox()
        elif browser == "PhantomJS" or browser == "ph":
            dr = webdriver.PhantomJS()

        try:
            self.driver = dr
            logger.info(u"%s打开%s浏览器" % (success, browser))
        except Exception:
            raise NameError(u"未找到%s浏览器，请输入'cr'，'ff'或'ph'。")

    def back(self):
        self.driver.back()
        logger.info(u"点击浏览器后退按钮")

    def forward(self):
        self.driver.forward()
        logger.info(u"点击浏览器前进按钮")

    def open_url(self, url):
        self.driver.get(url)
        logger.info(u"打开站点 %s" % url)

    @staticmethod
    def sleep(secs):
        time.sleep(secs)
        logger.info(u"强制等待 %f 秒" % secs)

    def take_screenshot(self):
        file_path = os.path.dirname(os.getcwd()) + '\\screenshots\\'
        file_name = file_path + now_time + '.jpg'
        try:
            self.driver.get_screenshot_as_file(file_name)
            logger.info(u"%s已截图保存为：%s" % (success, file_name))
        except NameError as e:
            logger.error(u"%s截图失败，错误：%s" % (fail, e))
            self.take_screenshot()

    def find_element(self, selector):
        """
        封装的元素定位方法, 入参selector格式为"by=>value"
        :param selector:
        :return element:
        """
        if '=>' not in selector:
            raise NameError(u"格式错误，请按此格式输入：by=>value")

        selector_by = selector.split('=>')[0].strip()
        selector_value = selector.split('=>')[1].strip()

        # by_id
        if selector_by == "id":
            element = self.driver.find_element_by_id(selector_value)
            logger.info(u"%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        # by_name
        elif selector_by == "name":
            element = self.driver.find_element_by_name(selector_value)
            logger.info(u"%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        # by_class_name
        elif selector_by == "class_name":
            element = self.driver.find_element_by_class_name(selector_value)
            logger.info(u"%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        # by_link_text
        elif selector_by == "link_text":
            element = self.driver.find_element_by_link_text(selector_value)
            logger.info(u"%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        # by_tag_name
        elif selector_by == "tag_name":
            element = self.driver.find_element_by_tag_name(selector_value)
            logger.info(u"%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        # by_xpath
        elif selector_by == "xpath":
            element = self.driver.find_element_by_xpath(selector_value)
            logger.info(u"%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        # by_css_selector
        elif selector_by == "css_selector":
            element = self.driver.find_element_by_css_selector(selector_value)
            logger.info(u"%s通过<%s>查找<%s>元素" % (success, selector_by, selector_value))
        else:
            raise NameError(u"请输入有效的元素类型")

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
                logger.info(u"%s清空输入框并输入：%s" % (success, text))
            else:
                logger.info(u"%s清空输入框并输入" % success)
        except Exception as e:
            logger.error(u"%s无法往输入框输入，错误：%s" %(fail, e))
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
                logger.info(u"%s清空输入框并输入：%s" % (success, text))
            else:
                logger.info(u"%s清空输入框并输入" % success)
        except Exception as e:
            logger.error(u"%s无法往输入框输入，错误：%s" %(fail, e))
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
            logger.info(u"%s清空输入框" % success)
        except Exception as e:
            logger.error(u"%s无法清空输入框，错误：%s" %(fail, e))
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
            logger.info(u"%s点击元素：%s" % (success, selector))
        except Exception as e:
            logger.error(u"%s无法点击元素，错误：%s" % (fail, e))
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
            logger.info(u"%s右键点击元素：%s" % (success, selector))
        except Exception as e:
            logger.error(u"%s无法右键点击，错误：%s" % (fail, e))

    def exec_js(self, script):
        """
        执行js语句
        :param script:
        :return:
        """
        try:
            self.driver.execute_script(script)
            logger.info(u"%s执行js：%s" % (success, script))
        except Exception as e:
            logger.error(u"%s执行js<%s>发生错误：%s" % (fail, script, e))

    def max_window(self):
        self.driver.maximize_window()
        logger.info(u"窗口最大化")

    def get_text(self, selector):
        """
        获取元素文本
        :param selector:
        :return:
        """
        try:
            self.wait_element(selector)
            elem_text = self.find_element(selector).text
            logger.info(u"%s获取文本为：%s" % (success, elem_text))
            return elem_text
        except Exception as e:
            logger.error(u"%s获取文本失败，错误：%s" % (fail, e))

    def wait_element(self, selector):
        """
        显式等待元素出现
        :param selector:
        :return:
        """
        if '=>' not in selector:
            raise NameError(u"格式错误，请按此格式输入：by=>value")

        selector_by = selector.split('=>')[0].strip()
        selector_value = selector.split('=>')[1].strip()
        message = u"元素%s不存在" % selector_value

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
        elif selector_by == 'css':
            WebDriverWait(self.driver, 10, 0.5)\
                .until(ec.presence_of_element_located((By.CSS_SELECTOR, selector_value)), message)
        else:
            raise NameError(u"请输入正确的查找方式，'id','name','class_name','link_text','tag_name','xpath','css'")

    def select(self, selector, select_type, value):
        """
        下拉选择
        :param selector:select元素定位
        :param select_type:select查找方法，有index, value, visible_text
        :param value:要查找的值，对应type，如type是visible_text则查找option显示的文本
        :return:
        """
        self.wait_element(selector)
        if select_type == "index":
            try:
                Select(self.find_element(selector)).select_by_index(value)
                logger.info(u"%s通过option的<%s>选中第<%s>项" % (success, select_type, value))
            except Exception as e:
                logger.error(u"%s无法通过<%s>选中第<%s>项，错误：%s" % (fail, select_type, value, e))
        elif select_type == "value":
            try:
                Select(self.find_element(selector)).select_by_value(value)
                logger.info(u"%s通过option的<%s>选中<%s>项" % (success, select_type, value))
            except Exception as e:
                logger.error(u"%s无法通过<%s>选中<%s>项，错误：%s" % (fail, select_type, value, e))
        elif select_type == "visible_text":
            try:
                Select(self.find_element(selector)).select_by_visible_text(value)
                logger.info(u"%s通过option的<%s>选中<%s>项" % (success, select_type, value))
            except Exception as e:
                logger.error(u"%s无法通过<%s>选中<%s>项，错误：%s" % (fail, select_type, value, e))
        else:
            raise NameError(u"请输入正确的查找方法：index, value, visible_text")

    def quit(self):
        self.driver.quit()
        logger.info(u"退出浏览器")