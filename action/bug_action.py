# -*- coding: utf-8 -*-
# @Time : 2021/8/20 13:46
# @Author : Limusen
# @File : bug_action

from element_infos.bug.bug_page import BugPage


class BugAction:

    def __init__(self, driver):
        self.bug = BugPage(driver)

    def commit_bug(self, title, content):
        self.bug.click_test_link()
        self.bug.click_bug_link()
        self.bug.click_commit_bug_button()
        self.bug.click_tag()
        self.bug.click_project()
        self.bug.input_bug_title(title)
        self.bug.switch_to_iframe_bug()
        self.bug.input_bug_content(content)
        self.bug.switch_to_default_iframe()
        self.bug.click_accpect_button()
        self.bug.wait(2)
        return self.bug.get_page_source()
