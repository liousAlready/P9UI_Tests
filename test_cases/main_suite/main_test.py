# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 4:40 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : main_test.py
# @Software: PyCharm


import unittest
from common.config_utils import local_config
from element_infos.login_page import LoginPage
from common.browser_utils import BrowserUtils
from action.login_action import LoginAction
from action.quit_action import QuitAction
from common.base_page import BasePage
from common.selenium_base_case import SeleniumBaseCase


class MainCase(SeleniumBaseCase):

    def test_quit(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_default()
        main = QuitAction(main_page.driver)
        result = main.quit()
        self.assertIn("新梦想项目管理平台项目管理系统dasd", result, "测试失败")


if __name__ == "__main__":
    unittest.main()
