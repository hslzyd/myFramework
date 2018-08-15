# coding=utf-8

import unittest
from utils import HTMLTestRunner_PY3
import time
from utils.config import CASE_PATH, REPORT_PATH
from utils.mail import Mail
from utils.config import Config
import os


def run():
    suite = unittest.defaultTestLoader.discover(start_dir=CASE_PATH, pattern='test*.py', top_level_dir=None)
    now_time = time.strftime("%Y-%m-%d-%H_%M_%S")
    if not os.path.exists(REPORT_PATH):
        os.mkdir(REPORT_PATH)
    report_name = REPORT_PATH + '/TestReport_' + now_time + '.html'
    fp = open(report_name, 'wb')
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"测试用例执行情况")
    runner.run(suite)
    if int(Config().get('mail', 'on_off')):
        Mail(report_name).send()  # 发送测试报告
    fp.close()


if __name__ == "__main__":
    run()
