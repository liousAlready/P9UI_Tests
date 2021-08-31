# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 10:33 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : log_utils_old.py
# @Software: PyCharm
import logging
import os

current_path = os.path.dirname(__file__)
log_path = os.path.join(current_path, '../logs/test.log')


class LogUtils:

    def __init__(self, path=log_path):
        self.logfile_path = path
        self.logger = logging.getLogger(__name__)  # 创建日志对象
        self.logger.setLevel(level=logging.INFO)
        file_log = logging.FileHandler(self.logfile_path, encoding="utf-8")  # 文件日志对象
        formatter = logging.Formatter('logs:%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)

    def get_logger(self):
        return self.logger


logger = LogUtils().get_logger()
