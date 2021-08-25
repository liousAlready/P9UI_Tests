# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 3:17 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : login_action.py
# @Software: PyCharm


# 登录页面功能操作

from element_infos.login_page import LoginPage
from element_infos.main_page import MainPage
from common.config_utils import local_config


class LoginAction:

    def __init__(self, driver):
        self.login = LoginPage(driver)

    def login_action(self, username, password):
        self.login.input_username(username)
        self.login.input_password(password)
        self.login.click_login()

    def login_success(self, username, password):
        self.login_action(username, password)
        return MainPage(self.login.driver)

    def login_fail(self, username, password):
        self.login.wait(2)
        self.login_action(username, password)
        return self.login.get_login_fail_alert_content()

    def login_default(self):
        self.login.wait(2)
        self.login_action(local_config.username, local_config.password)
        return MainPage(self.login.driver)
