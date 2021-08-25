# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 3:58 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : element_data_utils.py
# @Software: PyCharm

import os
import xlrd

#  元素识别信息读取工具类
current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../element_info_datas/element_info_datas.xls')


class ElementDataUtils:
    def __init__(self, module_name, excel_path=excel_path):
        self.work_book = xlrd.open_workbook(excel_path)
        self.sheet = self.work_book.sheet_by_name(module_name)
        self.row_count = self.sheet.nrows

    def get_element_infos(self, sheet_name):
        element_infos = {}
        for i in range(1, self.row_count):
            if self.sheet.cell_value(i, 2) == sheet_name:
                element_info = {}
                element_info['element_name'] = self.sheet.cell_value(i, 1)
                element_info['locator_type'] = self.sheet.cell_value(i, 3)
                element_info['locator_value'] = self.sheet.cell_value(i, 4)
                element_info['timeout'] = self.sheet.cell_value(i, 5)
                element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos


if __name__ == "__main__":
    info = ElementDataUtils("bug").get_element_infos("bug_page")
    print(info)
