# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 4:41 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : main_page_test.py
# @Software: PyCharm


from common.browser_utils import BrowserUtils
from common.config_utils import local_config
from action.login_action import LoginAction


driver = BrowserUtils().get_driver()
driver.get(local_config.get_url)
driver.maximize_window()

main_page = LoginAction(driver).login_default()
value = main_page.get_username()

print(value)