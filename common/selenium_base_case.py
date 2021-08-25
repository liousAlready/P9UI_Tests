# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 9:07 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : selenium_base_case.py
# @Software: PyCharm


import unittest
from common.browser_utils import BrowserUtils
from common.config_utils import local_config
from common.base_page import BasePage
from common.log_utils import logger


class SeleniumBaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logger.info("======测试类开始======")
        cls.base_page = BasePage(BrowserUtils().get_driver())

    def setUp(self) -> None:
        self.base_page.set_window_max()
        self.base_page.implicitly_wait(10)
        self.base_page.open_url(local_config.get_url)

    def tearDown(self) -> None:
        # 断言失败截图
        errors = self._outcome.errors
        for test, exc_info in errors:
            if exc_info:
                self.base_page.wait()
                self.base_page.screen_shot_path_as_file()
        self.base_page.wait(2)
        self.base_page.quit_browser()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     logger.info("======测试类结束======")
