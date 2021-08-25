# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 8:20 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : quit_action.py
# @Software: PyCharm

from element_infos.main_page import MainPage
from element_infos.login_page import LoginPage


class QuitAction:

    def __init__(self, driver):
        self.main = MainPage(driver)

    def quit(self):
        self.main.get_username()
        self.main.click_user()
        self.main.click_quit()
        return self.main.get_page_source()

