# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 9:05 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : login_page.py
# @Software: PyCharm

import os
import time

from common.log_utils_old import logger
from common.base_page import *
from common.element_data_utils_02 import ElementDataUtils
from common.browser_utils import *


#  页面是类  控件：属性 控件操作：方法

class LoginPage(BasePage):  # 继承页面类

    def __init__(self, driver):
        # 驱动的处理
        # 1.继承父类  子类构造方法需要显示调用父类的构造
        super().__init__(driver)
        # # 2.父类方法.构造方法(self,driver)
        # BasePage.__init__(self, driver)

        # 创建excel读取对象，通过字典来进行数据读取
        elements = ElementDataUtils('login').get_element_infos("login_page")
        self.username_input_box = elements["username_inputbox"]
        self.password_input_box = elements["password_inputbox"]
        self.submit = elements["login_button"]

    def input_username(self, username):  # 方法 --》 控件的操作
        logger.info("输入账号: %s" % username)
        self.input(self.username_input_box, username)

    def input_password(self, password):
        logger.info("输入密码: %s" % password)
        self.input(self.password_input_box, password)

    def click_login(self):
        self.click(self.submit)
        logger.info("点击登录按钮")

    #  如果用户名和密码错误，点击提提示框中的确定 并返回提示内容
    def get_login_fail_alert_content(self):
        return self.switch_to_alert()


if __name__ == "__main__":
    # 页面= 属性+方法
    # 属性命名 = 名字+类型
    # 操作命名 = 操作+元素对象

    driver = BrowserUtils().get_driver()
    login_page = LoginPage(driver)

    login_page.open_url(local_config.get_url)
    login_page.set_window_max()
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
    login_page.wait(2)
    login_page.screen_shot_path_as_file()
