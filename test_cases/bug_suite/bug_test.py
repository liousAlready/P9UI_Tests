# -*- coding: utf-8 -*-
# @Time : 2021/8/20 13:45
# @Author : Limusen
# @File : bug_test

import unittest
from action.bug_action import BugAction
from common.selenium_base_case import SeleniumBaseCase
from action.login_action import LoginAction


class BugTest(SeleniumBaseCase):

    def test_commit_bug(self):
        login = LoginAction(self.base_page.driver)
        main_page = login.login_default()
        bug = BugAction(main_page.driver)
        title = "哈哈哈哈哈哈哈"
        result = bug.commit_bug(title,"这就是bug呀")
        self.assertIn(title,result,"test_commit_bug--失败")


if __name__ == "__main__":
    unittest.main()
