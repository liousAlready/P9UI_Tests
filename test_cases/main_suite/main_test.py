# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 4:40 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : main_test.py
# @Software: PyCharm


import unittest
from action.login_action import LoginAction
from action.quit_action import QuitAction
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class MainCase(SeleniumBaseCase):
    test_class_data = TestDataUtils("main_suite", "main_case").convert_excel_data_test_data()

    def setUp(self) -> None:
        super().setUp()
        main_page = LoginAction(self.base_page.driver).login_default()
        self.main = QuitAction(main_page.driver)
        return self.main

    @unittest.skipIf(test_class_data['test_quit']['is_not'], '条件为真则跳过，如果为假则执行')
    def test_quit(self):
        test_function_data = self.test_class_data['test_quit']
        self._testMethodDoc = test_function_data['test_name'] + str(test_function_data['is_not'])  # testMethodDoc测试备注
        result = self.main.quit()
        self.assertIn(test_function_data['excepted_result'], result, "测试失败")


if __name__ == "__main__":
    unittest.main()
