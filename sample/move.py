# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 8:13 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : move.py
# @Software: PyCharm


from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils_old import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


# 常用鼠标键盘操作

def move_mouse():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")

    el = driver.find_element(By.NAME, "wd")
    # 1.对页面元素进行右击操作   ActionChains(driver).context_click(el).perform()
    ActionChains(driver).context_click(el).perform()
    # 2.双击   ActionChains(driver).double_click(el).perform()
    el = driver.find_element(By.ID, "su")
    driver.find_element(By.NAME, 'wd').send_keys("惆怅长岑长")
    ActionChains(driver).double_click(el).perform()
    # 3.鼠标悬停
    el = driver.find_element(By.ID, 's-usersetting-top')
    ActionChains(driver).move_to_element(el).perform()
    driver.find_element(By.LINK_TEXT, '高级搜索').click()
