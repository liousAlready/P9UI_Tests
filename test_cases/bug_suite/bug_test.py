# -*- coding: utf-8 -*-
# @Time : 2021/8/20 13:45
# @Author : Limusen
# @File : bug_test

import unittest
from action.bug_action import BugAction
from common.selenium_base_case import SeleniumBaseCase
from action.login_action import LoginAction
from common.test_data_utils import TestDataUtils


class BugTest(SeleniumBaseCase):
    test_class_data = TestDataUtils("bug_suite", "bug_case").convert_excel_data_test_data()

    def setUp(self) -> None:
        super().setUp()
        login = LoginAction(self.base_page.driver)
        main_page = login.login_default()
        self.bug = BugAction(main_page.driver)
        return self.bug

    @unittest.skipIf(test_class_data['test_commit_bug']['is_not'], '条件为真则跳过，如果为假则执行')
    def test_commit_bug(self):
        test_function_data = self.test_class_data['test_commit_bug']
        self._testMethodDoc = test_function_data['test_name'] + str(test_function_data['is_not'])  # testMethodDoc测试备注
        result = self.bug.commit_bug(test_function_data['test_parameter'].get('title'),
                                     test_function_data['test_parameter'].get('content'))
        self.assertIn(test_function_data['test_parameter'].get('title'), result, "test_commit_bug--失败")


if __name__ == "__main__":
    unittest.main()
