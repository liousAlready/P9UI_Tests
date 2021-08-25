# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 9:03 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : elements_demo.py
# @Software: PyCharm


from common.element_data_utils_02 import ElementDataUtils

str1 = 'bug链接 [%s]'
title = "唐同学创建的bug"

print(str1 % title)

elements = ElementDataUtils('login').get_element_infos("bug_page")
bug_link = elements['bug_link']
print(elements)

#  方法一：
# 字典里面，通过key取值
locator_value = bug_link['locator_value'] % title
print(locator_value)

# 方法二：

locator = bug_link.get("locator_value") % title
print(locator)
