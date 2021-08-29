# -*- coding: utf-8 -*-
# @Time    : 2021/8/22 9:36 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : excel_utils.py
# @Software: PyCharm
# @desc : 读取excel表工具类，底层封装，读取excel表文件后，返回[],[],[]


import os
import xlrd
from common.config_utils import local_config


class ExcelUtils:
    """

    先判定是否为excel文件，然后再出来xls，xlsx类型，并且判断文件存在

    """

    def __init__(self, file_path, sheet_name=None):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.sheet_data = self.__get_sheet_data()

    def __get_sheet_data(self):
        work_book = xlrd.open_workbook(self.file_path)
        if self.sheet_name:  # 当sheet_name存在 ，就按sheet_name 获取页签数据
            sheet = work_book.sheet_by_name(self.sheet_name)
        else:
            sheet = work_book.sheet_by_index(0)  # 当sheet不存在时，就读取文件的第一个页签 sheet1
        return sheet

    @property
    def get_row_count(self):
        row_count = self.sheet_data.nrows
        return row_count

    @property
    def get_col_count(self):
        col_count = self.sheet_data.ncols
        return col_count

    def get_sheet_data_by_list(self):
        """
        将excel表的数据通过列表返回 [[],[],[]]
        :return:
        """
        all_excel_data = []
        for row in range(self.get_row_count):  # 假设有self.get_row_count = 5 取0， 1，2，3，4
            row_excel_data = []
            for col in range(self.get_col_count):
                cell_value = self.sheet_data.cell_value(row, col)
                row_excel_data.append(cell_value)
            all_excel_data.append(row_excel_data)
        return all_excel_data


if __name__ == "__main__":
    # current_path = os.path.dirname(__file__)
    # excel_path = os.path.join(current_path, '..', local_config.test_data_path)
    # ex = ExcelUtils(excel_path, 'login').get_sheet_data_by_list()
    # for i in ex:
    #     print(i)
    pass
