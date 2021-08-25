# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 2:08 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : demo_switch_to_windos.py
# @Software: PyCharm


import time
from common.browser_utils import BrowserUtils
from common.base_page import BasePage
from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# driver.find_element_by_link_text("新闻").click()
# driver.find_element_by_link_text("hao123").click()
# driver.find_element_by_link_text("地图").click()

driver = BrowserUtils().get_driver()
base = BasePage(driver)
base.open_url("https://www.baidu.com")
base.set_window_max()
base.implicitly_wait(10)
base.driver.find_element_by_link_text("新闻").click()
base.driver.find_element_by_link_text("hao123").click()
base.driver.find_element_by_link_text("地图").click()

base.switch_to_window_by_title("百度一下，你就知道")
base.driver.find_element_by_name('wd').send_keys("python")
base.screen_shot_path_as_file()

base.switch_to_window_by_title("百度新闻——海量中文资讯平台")
base.driver.find_element_by_xpath('//*[@id="ww"]').send_keys("hahah")

base.switch_to_window_by_url('hao123.com')
base.driver.find_element_by_name('word').send_keys('hao123')

# base.switch_to_window_by_title("hao123_上网从这里开始")
# base.driver.find_element_by_xpath('//*[@id="search"]/form/div[2]/input').send_keys("这是测试")

driver.page_source()