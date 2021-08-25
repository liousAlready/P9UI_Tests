# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 4:25 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : config_utils.py
# @Software: PyCharm
import configparser
import os

current = os.path.dirname(__file__)
config_path = os.path.join(current, '../config/config.ini')


class ConfigUtils:

    def __init__(self, config_path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path, encoding="utf-8")

    @property
    def get_url(self):
        url = self.cfg.get("DEFAULT", "LOGIN_URL")
        return url

    @property
    def get_driver_path(self):
        url = self.cfg.get("DRIVER_PATH", "DRIVER_PATH")
        return url

    @property
    def get_logs_path(self):
        logs_path = self.cfg.get("LOGS", "LOGS_PATH")
        return logs_path

    @property
    def log_level(self):
        log_level = self.cfg.get("LOGS", "LOGS_LEVEL")
        return int(log_level)

    @property
    def default_driver(self):
        default_driver = self.cfg.get("DRIVER", "DEFAULT_DRIVER")
        return default_driver

    @property
    def time_out(self):
        time_out = self.cfg.get("DEFAULT", "TIME_OUT")
        return int(time_out)

    @property
    def screen_shot(self):
        screen_shot = self.cfg.get("DEFAULT", "screen_shot")
        return screen_shot

    @property
    def username(self):
        username = self.cfg.get("DEFAULT", "username")
        return username

    @property
    def password(self):
        password = self.cfg.get("DEFAULT", "password")
        return password

    @property
    def test_data_path(self):
        test_data_path = self.cfg.get("DEFAULT", "test_data_path")
        return test_data_path

    @property
    def case_path(self):
        case_path = self.cfg.get("DEFAULT", "case_path")
        return case_path

    @property
    def report_path(self):
        report_path = self.cfg.get("DEFAULT", "report_path")
        return report_path


local_config = ConfigUtils()

if __name__ == "__main__":
    print(local_config.get_url)
    print(local_config.report_path)
    print(local_config.case_path)
