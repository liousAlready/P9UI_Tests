# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 3:27 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : read_excel.py
# @Software: PyCharm

import os
import xlrd

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../element_info_datas/element_info_datas.xls')

work_book = xlrd.open_workbook(excel_path)
sheet = work_book.sheet_by_name("login_page")
row_count = sheet.nrows

element_infos = {}
for i in range(1, row_count):
    element_info = {}
    element_info['element_name'] = sheet.cell_value(i, 1)
    element_info['locator_type'] = sheet.cell_value(i, 2)
    element_info['locator_value'] = sheet.cell_value(i, 3)
    element_info['timeout'] = sheet.cell_value(i, 4)
    element_infos[sheet.cell_value(i, 0)] = element_info

print(element_infos)
