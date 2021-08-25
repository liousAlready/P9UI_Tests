# -*- coding: utf-8 -*-
# @Time    : 2021/8/22 4:44 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : run_all_cases.py
# @Software: PyCharm
# @desc : 执行层脚本，执行所有测试用例


import os
import unittest
from common import HTMLTestReportCN
from common.config_utils import local_config

current_path = os.path.dirname(__file__)
case_path = os.path.join(current_path, '..', local_config.case_path)
report_path = os.path.join(current_path, '..', local_config.report_path)


class RunAllCases:

    def __init__(self):
        self.test_case = case_path
        self.report_path = report_path
        self.title = "禅道UI自动化测试报告"
        self.description = "Li"

    def run(self):
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_case,
                                                       pattern='login_test.py',
                                                       top_level_dir=self.test_case)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)

        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        dir_path = HTMLTestReportCN.GlobalMsg.get_value("dir_path")
        r_path = HTMLTestReportCN.GlobalMsg.get_value("report_path")
        fp = open(r_path, 'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title=self.title, description=self.description, tester="li")

        runner.run(all_suite)
        fp.close()
        return dir_path


if __name__ == "__main__":
    RunAllCases().run()
