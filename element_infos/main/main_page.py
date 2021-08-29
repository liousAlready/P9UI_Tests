# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 9:07 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : main_page.py
# @Software: PyCharm


import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_infos.login.login_page import LoginPage
from common.element_data_utils import ElementDataUtils
from common.log_utils_old import logger
from common.base_page import BasePage
from common.browser_utils import BrowserUtils


class MainPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

        # 创建excel读取对象，通过字典来进行数据读取
        elements = ElementDataUtils('main', 'main_page').get_element_infos()
        self.my_zone_link = elements["my_zone_link"]
        self.user_menu = elements["user_menu"]
        self.quit_button = elements["quit_button"]

    def goto_my_zone(self):
        """选择我的地盘"""
        self.click(self.my_zone_link)
        logger.info("点击我的地盘")

    def get_username(self):
        """获取用户名"""
        value = self.get_text(self.user_menu)
        logger.info("获取用户名称：%s" % value)
        return value

    def click_user(self):
        self.click(self.user_menu)
        logger.info("点击user")

    def click_quit(self):
        self.click(self.quit_button)
        self.wait(2)
        logger.info("点击退出")


if __name__ == "__main__":
    driver = BrowserUtils().get_driver()
    main_page = MainPage(driver)
