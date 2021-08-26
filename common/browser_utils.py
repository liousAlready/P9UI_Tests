# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 4:38 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : browser_utils.py
# @Software: PyCharm


from selenium import webdriver
from common.config_utils import *
from selenium.webdriver.chrome.options import Options
from common.log_utils_old import logger

# 浏览器类，用来提供driver驱动

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, ".." + local_config.get_driver_path)


class BrowserUtils:

    def __init__(self, driver_path=driver_path):
        self.driver_path = driver_path
        self.driver_name = local_config.default_driver

    def get_driver(self):
        """打开驱动"""
        if self.driver_name.lower() == "chrome":
            logger.info("当前正在打开：%s" % self.driver_name)
            return self.__get_chrome_driver()
        elif self.driver_name.lower() == 'firefox':
            logger.info("当前正在打开：%s" % self.driver_name)
            return self.__get_firefox_driver()
        elif self.driver_name.lower() == "edge":
            logger.info("当前正在打开：%s" % self.driver_name)
            return self.__get_edge_driver()

    def __get_chrome_driver(self):
        """去除谷歌浏览器控制白条"""
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示
        chrome_driver_path = os.path.join(self.driver_path, 'chromedriver.exe')
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        logger.info('初始化Google浏览器并启动')
        return driver

    def __get_firefox_driver(self):
        firefox_driver_path = os.path.join(self.driver_path, 'geckodriver.exe')
        driver = webdriver.Firefox(executable_path=firefox_driver_path)
        return driver

    def __get_edge_driver(self):
        edge_driver_path = os.path.join(self.driver_path, 'msedgedriver.exe')
        driver = webdriver.Edge(executable_path=edge_driver_path)
        return driver


if __name__ == "__main__":
    BrowserUtils().get_driver()
