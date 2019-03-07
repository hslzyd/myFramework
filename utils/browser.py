from utils import config
from selenium import webdriver
import time

CHROME_DRIVER = config.DRIVER_PATH + '\chromedriver.exe'
FIREFOX_DRIVER = config.DRIVER_PATH + '\geckodriver.exe'
IE_DRIVER = config.DRIVER_PATH + '\IEDriverServer.exe'
EDGE_DRIVER = config.DRIVER_PATH + '\MicrosoftWebDriver.exe'

TYPES = {'chrome': webdriver.Chrome, 'firefox': webdriver.Firefox, 'ie': webdriver.Ie, 'edge': webdriver.Edge}
EXECUTABLE_PATH = {'chrome': CHROME_DRIVER, 'firefox': FIREFOX_DRIVER, 'ie': IE_DRIVER, 'edge': EDGE_DRIVER}

SUCCESS = "SUCCESS    "
FAIL = "FAIL    "
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
        return self.driver


if __name__ == '__main__':
    b = Browser('edge')
    driver = b.get_driver()
    driver.get("https://www.google.com")
    driver.quit()
