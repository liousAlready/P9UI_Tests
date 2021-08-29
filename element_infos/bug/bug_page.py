# -*- coding: utf-8 -*-
# @Time : 2021/8/20 13:53
# @Author : Limusen
# @File : bug_page


from common.element_data_utils import ElementDataUtils
from common.config_utils import local_config
from common.log_utils import logger
from common.base_page import BasePage


class BugPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        elements = ElementDataUtils('bug', 'bug_page').get_element_infos()

        self.test_link = elements['test_link']
        self.bug_link = elements['bug_link']
        self.commit_bug_button = elements['commit_bug_button']
        self.project_click = elements['project_click']
        self.dbshop_click = elements['dbshop_click']
        self.tag_click = elements['tag_click']
        self.release_click = elements['release_click']
        self.bug_title_input = elements['bug_title_input']
        self.switch_to_iframe = elements['switch_to_iframe']
        self.bug_content_input = elements['bug_content_input']
        self.accpect_button = elements['accpect_button']

    def click_test_link(self):
        self.wait(2)
        self.click(self.test_link)
        logger.info("点击测试链接")

    def click_bug_link(self):
        self.wait(1)
        self.click(self.bug_link)
        logger.info("点击bug链接")

    def click_commit_bug_button(self):
        self.click(self.commit_bug_button)
        logger.info("点击提bug按钮")

    def click_project(self):
        self.click(self.project_click)
        self.wait(1)
        self.click(self.dbshop_click)

    def click_dbshop(self):
        self.click(self.dbshop_click)

    def click_tag(self):
        self.click(self.tag_click)
        self.wait(1)
        self.click(self.release_click)

    def click_release(self):
        self.click(self.release_click)

    def input_bug_title(self, title):
        self.wait(1)
        self.input(self.bug_title_input, title)

    def switch_to_iframe_bug(self):
        self.switch_to_frame_by_element(self.switch_to_iframe)
        logger.info("切入框架")

    def input_bug_content(self, content):
        self.input(self.bug_content_input, content)
        logger.info("输入bug内容")

    def switch_to_default_iframe(self):
        self.switch_to_default()
        logger.info("跳啊")

    def click_accpect_button(self):
        self.click(self.accpect_button)
