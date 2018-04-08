import utils.config
from selenium import webdriver
from utils.logger import Logger
import time

CHROME_DRIVER = utils.config.DRIVER_PATH + '\chromedriver.exe'
FIREFOX_DRIVER = utils.config.DRIVER_PATH + '\geckodriver.exe'
IE_DRIVER = utils.config.DRIVER_PATH + '\IEDriverServer.exe'
EDGE_DRIVER = utils.config.DRIVER_PATH + '\MicrosoftWebDriver.exe'

TYPES = {'chrome': webdriver.Chrome, 'firefox': webdriver.Firefox, 'ie': webdriver.Ie, 'edge': webdriver.Edge}
EXECUTABLE_PATH = {'chrome': CHROME_DRIVER, 'firefox': FIREFOX_DRIVER, 'ie': IE_DRIVER, 'edge': EDGE_DRIVER}

SUCCESS = "SUCCESS    "
FAIL = "FAIL    "
logger = Logger(logger="Browser").getlog()
now_time = time.strftime("%Y%m%d%H%M%S")


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):
    def __init__(self, browser_type='chrome'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError("配置文件错误，仅支持%s!" % '、'.join(TYPES.keys()))
        self.driver = None

    def get_driver(self):

        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        logger.info("%s启动%s浏览器" % (SUCCESS, self._type))
        return self.driver


if __name__ == '__main__':
    b = Browser('chrome')
    b.get_driver()