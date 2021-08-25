# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 8:57 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : testcase_demo.py
# @Software: PyCharm

import unittest


class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")

    def setUp(self) -> None:
        print("setUP")

    def tearDown(self) -> None:
        print("tearDown")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test01(self):
        print("test01")

    def test02(self):
        print("test02")


if __name__ == "__main__":
    unittest.main()
