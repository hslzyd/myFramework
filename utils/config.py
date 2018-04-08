# coding = utf-8
"""
读取配置文件、设置路径
"""

import os
from utils.file_reader import INIReader

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.ini')
LOG_PATH = os.path.join(BASE_PATH, 'logs')
REPORT_PATH = os.path.join(BASE_PATH, 'reports')
SCREENSHOT_PATH = os.path.join(BASE_PATH, 'screenshots')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
DATA_PATH = os.path.join(BASE_PATH, 'data')


class Config:
    def __init__(self, config=CONFIG_FILE):
        self.cp = INIReader(config).data

    def get(self, section, option):
        """
        获取ini文件section节点中option对应的value值
        :param section:节名
        :param option:键名
        :return:返回value
        """
        return self.cp.get(section, option)


if __name__ == '__main__':
    c = Config()
    print(c.get('browser', 'name'))
