# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 3:58 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : element_data_utils.py
# @Software: PyCharm

import os
from common.excel_utils import ExcelUtils
from common.config_utils import local_config

#  元素识别信息读取工具类
current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '..', local_config.test_data_path)


class TestDataUtils:

    def __init__(self, test_suite, test_class_name):
        self.test_class_name = test_class_name
        self.excel_data = ExcelUtils(excel_path, test_suite).get_sheet_data_by_list()
        self.excel_row_count = len(self.excel_data)

    def convert_excel_data_test_data(self):
        test_data_information = {}
        for row in range(1, self.excel_row_count):  # 循环总行数
            test_data_info = {}  # 数据分层
            if self.excel_data[row][2].__eq__(self.test_class_name):  # 判断传入的测试类是否与excel中数据一致
                test_data_info["test_name"] = self.excel_data[row][1]  # 取出测试名称
                # test_data_info["is_not"] = self.excel_data[row][3] # 取出是否执行
                test_data_info["is_not"] = False if self.excel_data[row][3].__eq__("是") else True  # 取出是否执行
                test_data_info["excepted_result"] = self.excel_data[row][4]  # 取出期望结果
                test_parameter = {}  # 测试数据需要用字典来读取
                for case_data in range(5, len(self.excel_data[row])):  # 从第六个参数开始进行判断 因为测试数据可能有多个
                    if self.excel_data[row][case_data].__contains__("=") and len(
                            self.excel_data[row][case_data]) > 2:  # 分割测试数据并判断长度是否大于两个
                        parameter_info = self.excel_data[row][case_data].split("=")
                        test_parameter[parameter_info[0]] = parameter_info[1]
                        test_data_info['test_parameter'] = test_parameter
            test_data_information[self.excel_data[row][0]] = test_data_info
        return test_data_information


if __name__ == "__main__":
    cs = TestDataUtils('login_suite', 'LoginCase').convert_excel_data_test_data()
    print(cs)
    for k, v in cs.items():
        print(k, v)
