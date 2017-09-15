# coding=utf-8

import unittest
import HTMLTestRunner
import time
import os


def run():
    test_dir = os.getcwd() + '\\test_case'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py', top_level_dir=None)

    now_time = time.strftime("%Y-%m-%d-%H_%M_%S")
    report_name = os.getcwd() + '\\reports\\TestReport_' + now_time + '.html'
    fp = file(report_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"测试用例执行情况")
    runner.run(suite)
    fp.close()


if __name__ == "__main__":
    run()
