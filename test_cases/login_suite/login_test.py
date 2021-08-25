# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 4:05 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : login_test.py
# @Software: PyCharm


import unittest
from common.config_utils import local_config
from action.login_action import LoginAction
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class LoginCase(SeleniumBaseCase):
    test_class_data = TestDataUtils('login_suite', 'LoginCase').convert_excel_data_test_data()

    @unittest.skipIf(test_class_data['test_login_success']['is_not'], '条件为真则跳过，如果为假则执行')
    def test_login_success(self):
        test_function_data = self.test_class_data['test_login_success']
        self._testMethodDoc = test_function_data['test_name'] + str(test_function_data['is_not'])
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success(test_function_data['test_parameter'].get('username'),
                                               test_function_data['test_parameter'].get('password'))
        self.assertEqual(main_page.get_username(), test_function_data['excepted_result'], "测试失败")

    @unittest.skipIf(test_class_data['test_login_fail']['is_not'], '条件为真则跳过，如果为假则执行')
    def test_login_fail(self):
        test_function_data = self.test_class_data['test_login_fail']
        self._testMethodDoc = test_function_data['test_name'] + str(test_function_data['is_not'])
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail(test_function_data['test_parameter'].get('username'),
                                                test_function_data['test_parameter'].get('password'))
        self.assertEqual(actual_result, "登录失败，请检查您的用户名或密码是否填写正确。", "测试失败")

    def test_default(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_default()
        self.assertEqual(main_page.get_username(), "测试人员1", "测试失败")


if __name__ == "__main__":
    unittest.main()
