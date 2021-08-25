# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 11:33 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : base_page.py
# @Software: PyCharm

import os.path
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.log_utils_old import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from common.config_utils import local_config
from common import HTMLTestReportCN

'''所有页面的父类,提取所有页面的公共操作，做成BasePage'''

system = sys.platform


# 启动浏览器之后，将driver传给Base_page
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def open_url(self, url):
        self.driver.get(url)
        logger.info("打开url：%s" % url)

    def set_window_max(self):
        self.driver.maximize_window()
        logger.info("浏览器最大化...")

    def page_refresh(self):
        self.driver.refresh()
        logger.info("浏览器刷新...")

    def get_title(self):
        value = self.driver.title
        logger.info("获取标题：%s" % value)
        return value

    def get_url(self):
        value = self.driver.current_url
        return value

    def get_text(self, element_info):
        element = self.find_element(element_info)
        text = element.text
        logger.info("获取文本信息：%s" % text)
        return text

    def get_page_source(self):
        source = self.driver.page_source
        return source

    def close_tab(self):
        self.driver.closer()
        logger.info("关闭当前的tab页面")

    def quit_browser(self):
        self.driver.quit()
        logger.info("退出浏览器")

    def back_up(self):
        self.driver.back()
        logger.info("返回上一页...")

    def forward(self):
        self.driver.forward()
        logger.info("前进一页...")

    # 　封装时间
    def wait(self, seconds=local_config.time_out):
        """
        固定等待--加入默认值，如果没有设置超时时间，则默认等待五秒钟

        :param seconds: 如果没有传入值则默认等待5秒钟
        """
        time.sleep(seconds)
        logger.info("休息一会儿 %s 秒钟~" % seconds)

    def implicitly_wait(self, seconds=local_config.time_out):
        """
        隐式等待--加入默认值，如果没有设置超时时间，则默认等待五秒钟

        :param seconds: 如果没有传入值则默认等待5秒钟
        """
        self.driver.implicitly_wait(seconds)
        logger.info("隐式等待个 %s 秒" % seconds)

    #  元素识别 通过分离处理的元素识别字典信息，返回一个元素
    # self.username_input_box = self.driver.find_element(By.XPATH, '//*[@name="account"]')
    def find_element(self, element_infos):
        '''
        :param element_infos:
        :return:
            username_input_box = {"element_name": "用户名输入框",
                                       "locator_type": "xpath",
                                       "locator_value": '//*[@name="account"]',
                                       "timeout": 5}
        '''
        locator_type = element_infos["locator_type"]
        locator_value = element_infos["locator_value"]
        locator_timeout = element_infos["timeout"]
        try:
            if locator_type == "name":
                locator_type = By.NAME
            elif locator_type == "css":
                locator_type = By.CSS_SELECTOR
            elif locator_type == "xpath":
                locator_type = By.XPATH
            elif locator_type == "id":
                locator_type = By.ID
            elif locator_type == "class":
                locator_type = By.CLASS_NAME
            elif locator_type == "linktext":
                locator_type = By.LINK_TEXT
            elif locator_type == "partiallink":
                locator_type = By.PARTIAL_LINK_TEXT
            elif locator_type == "tag":
                locator_type = By.TAG_NAME
            element = WebDriverWait(self.driver, timeout=locator_timeout).until(
                lambda x: x.find_element(locator_type, locator_value))
            logger.info("[%s] 元素识别成功" % element_infos["locator_value"])
        except Exception as e:
            logger.error("[%s] 元素识别失败，原因是: [%s]" % (element_infos["locator_value"], e.__str__()))
            self.screen_shot_path_as_file()
        return element

    #  元素操作

    #  封装输入参数
    def input(self, element_infos, inputs):
        try:
            element = self.find_element(element_infos)
            element.send_keys(inputs)
            logger.info("输入框输入内容：%s , 识别输入框：%s" % (inputs, element_infos["locator_value"]))
        except Exception as e:
            logger.error("[%s] 元素识别失败，原因是: [%s]" % (element_infos["locator_value"], e.__str__()))
            self.screen_shot_path_as_file()

    #  封装点击方法
    def click(self, element_infos):
        try:
            element = self.find_element(element_infos)
            element.click()
            logger.info("识别元素进行点击操作：%s" % element_infos["locator_value"])
        except Exception as e:
            logger.error("[%s] 元素识别失败，原因是: [%s]" % (element_infos["locator_value"], e.__str__()))
            self.screen_shot_path_as_file()

    # 封装鼠标键盘
    def move_to_element_by(self, element_infos):
        """鼠标悬停"""
        el = self.find_element(element_infos)
        ActionChains(self.driver).move_to_element(el).perform()
        self.wait(2)

    def move_mouse_left_click(self, element_info):
        """左击鼠标"""
        target = self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(target).perform()
        logger.info("左击元素：%s" % element_info['locator_value'])

    def move_mouse_double_click(self, element_info):
        """双击元素"""
        target = self.find_element(element_info)
        ActionChains(self.driver).double_click(target).perform()
        logger.info("双击元素：%s" % element_info['locator_value'])

    def long_press_element(self, element_info, second):
        """长按元素--按住多久然后释放"""
        target = self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(target).pause(second)
        logger.info("长按元素：%s，给他按在地上：%s 秒" % (element_info['locator_value'], second))

    # 键盘操作
    def keyboard_tab(self, element_info):
        """点击tab键"""
        element = self.find_element(element_info)
        element.send_keys(Keys.TAB)
        logger.info("点击tab：%s" % element_info['locator_value'])

    def keyboard_delete(self, element_info):
        """删除键"""
        element = self.find_element(element_info)
        element.send_keys(Keys.BACK_SPACE)
        logger.info("删除内容：%s" % element_info['locator_value'])

    def keyboard_all(self, element_info):
        """全选"""
        if system.lower() == "win32":
            element = self.find_element(element_info)
            element.send_keys(Keys.CONTROL, 'a')
            logger.info("全选内容：%s" % element_info['locator_value'])
        else:
            element = self.find_element(element_info)
            element.send_keys(Keys.COMMAND, 'a')
            logger.info("全选内容：%s" % element_info['locator_value'])

    def keyboard_copy(self, element_info):
        """复制内容"""
        if system.lower() == "win32":
            element = self.find_element(element_info)
            element.send_keys(Keys.CONTROL, 'c')
            logger.info("复制内容：%s" % element_info['locator_value'])
        else:
            element = self.find_element(element_info)
            element.send_keys(Keys.COMMAND, 'c')
            logger.info("复制内容：%s" % element_info['locator_value'])

    def keyboard_paste(self, element_info):
        """粘贴内容"""
        if system.lower() == "win32":
            element = self.find_element(element_info)
            element.send_keys(Keys.CONTROL, 'v')
            logger.info("粘贴内容：%s" % element_info['locator_value'])
        else:
            element = self.find_element(element_info)
            element.send_keys(Keys.COMMAND, 'v')
            logger.info("粘贴内容：%s" % element_info['locator_value'])

    def keyboard_cut(self, element_info):
        """剪切内容"""
        if system.lower() == "win32":
            element = self.find_element(element_info)
            element.send_keys(Keys.CONTROL, 'x')
            logger.info("剪切内容：%s" % element_info['locator_value'])
        else:
            element = self.find_element(element_info)
            element.send_keys(Keys.COMMAND, 'x')
            logger.info("剪切内容：%s" % element_info['locator_value'])

    # alert 弹出框
    # def switch_to_alert(self, action='accept', time_out=local_config.time_out):
    #     self.wait(time_out)
    #     alert = self.driver.switch_to.alert  # 弹出框对象
    #     alert_text = alert.text
    #     if action == 'accept':
    #         alert.accept()
    #     else:
    #         alert.dismiss()
    #     return alert_text

    # 扩展 封装提示框输入内容的方法

    # 扩展 Ec模块写断言
    def switch_to_alert(self, action='accept', time_out=local_config.time_out):
        WebDriverWait(self.driver, time_out).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert  # 弹出框对象
        alert_text = alert.text
        if action == 'accept':
            alert.accept()
        else:
            alert.dismiss()
        return alert_text

    # 切句柄
    # 获取当前窗口句柄
    def get_window_handles(self):
        now_handle = self.driver.current_window_handle
        return now_handle

    def switch_to_window_by_handle(self, window_handle):
        self.driver.switch_to.window(window_handle)

    # 更高级的封装方式
    # def switch_to_window_by_title(self, title):
    #     all_handles = self.driver.window_handles
    #     for window_handle in all_handles:
    #         if self.get_title() == title:
    #             self.driver.switch_to.window(window_handle)
    #             break
    #
    # def switch_to_window_by_url(self, url):
    #     all_handles = self.driver.window_handles
    #     for window_handle in all_handles:
    #         if self.get_url() == url:
    #             self.driver.switch_to.window(window_handle)
    #             break

    def switch_to_window_by_title(self, title):
        all_handles = self.driver.window_handles
        for window_handle in all_handles:
            self.driver.switch_to.window(window_handle)
            try:
                if WebDriverWait(self.driver, local_config.time_out).until(EC.title_contains(title)):
                    break
            except Exception as e:
                logger.error("当前切换脚本有误，错误详情：%s" % e)
                continue

    def switch_to_window_by_url(self, url):
        all_handles = self.driver.window_handles
        for window_handle in all_handles:
            self.driver.switch_to.window(window_handle)
            try:
                if WebDriverWait(self.driver, local_config.time_out).until(EC.url_contains(url)):
                    break
            except Exception as e:
                logger.error("当前切换脚本有误，错误详情：%s" % e)
                continue

    def screen_shot_path_as_file_old(self, *screen_shot_path):
        if len(screen_shot_path) == 0:  # 存放在默认路径下
            screen_shot_path = local_config.screen_shot
        else:
            screen_shot_path = screen_shot_path[0]
        now = time.strftime("%Y_%m_%d_%H_%M_%S")
        current = os.path.dirname(__file__)
        file_name = os.path.join(current, '..', local_config.screen_shot, 'Uitest_%s.png' % now)
        self.driver.save_screenshot(file_name)

    def screen_shot_path_as_file(self):
        report_path = os.path.join(os.path.dirname(__file__), '..', local_config.report_path)
        report_dir = HTMLTestReportCN.ReportDirectory(report_path)
        report_dir.get_screenshot(self.driver)

    # 跳转框架
    # 思路一：
    def iframe_switch_to(self, element_infos):
        """通过元素信息来定位"""
        iframe = self.find_element(element_infos)
        self.driver.switch_to.frame(iframe)
        logger.info("现在跳转框架：%s" % element_infos["locator_value"])

    # 思路二：
    def iframe_switch_to_id_or_name(self, id_or_name):
        """通过id或者name"""
        self.driver.switch_to.frame(id_or_name)
        logger.info("现在跳转框架：%s" % id_or_name["locator_value"])

    def iframe_switch_to_by_element(self, element_infos):
        iframe = self.find_element(element_infos)
        self.driver.switch_to.frame(iframe)

    # 思路三：
    def switch_to_frame_all(self, **element_dicts):
        # id = frame_all name = frame_name element = element_infos
        """需要指定配置的元素名才能进行识别操作"""
        if 'id' in element_dicts.keys():
            self.driver.switch_to.frame(element_dicts['id'])
        elif 'name' in element_dicts.keys():
            self.driver.switch_to.frame(element_dicts['name'])
        elif 'element' in element_dicts.keys():
            element = self.find_element(element_dicts['element'])
            self.driver.switch_to.frame(element)

    def switch_to_default(self):
        try:
            self.wait(1)
            self.driver.switch_to.default_content()
            logger.info("调回原来框架")
        except Exception as e:
            logger.error("切换框架失败，原因是：%s" % e)
            self.screen_shot_path_as_file()

    def switch_to_frame_by_element(self, element_info):
        self.wait()
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

    # js
    #  步骤一
    def delete_element_attribute(self, element_infos, attribute_name):
        """移除元素属性封装"""
        element = self.find_element(element_infos)
        js = 'arguments[0].removeAttribute("%s")' % attribute_name
        self.__execute_script(js, element)
        logger.info("移除元素属性: %s" % element_infos["locator_value"])

    def update_element_attribute(self, element_infos, attribute_name, attribute_value):
        """更新元素属性封装"""
        element = self.find_element(element_infos)
        js = 'arguments[0].setAttribute("%s","%s")' % (attribute_name, attribute_value)
        self.__execute_script(js, element)
        logger.info("修改元素属性: %s，替换的值：%s" % (element_infos["locator_value"], attribute_value))

    def scroll(self, height):
        """滚动条"""
        js = "window.scrollBy(0," + str(height) + ")"
        self.__execute_script(js)
        logger.info("当前页面正在滚动，滚动值: %s" % height)

    # 步骤二
    # 封装执行js脚本

    def __execute_script(self, js_str, element=None):
        if element:
            self.driver.execute_script(js_str, element)
        else:
            self.driver.execute_script(js_str)

    # 移动鼠标操作
    def move_mouse_right_click(self, element_infos):
        """右击鼠标"""
        target = self.find_element(element_infos)
        ActionChains(self.driver).context_click(target).perform()
        logger.info("右击元素：%s" % element_infos['locator_value'])

    def mova_mouse_double_click(self, element_infos):
        """双击元素"""
        target = self.find_element(element_infos)
        ActionChains(self.driver).double_click(target).perform()
        logger.info("双击元素：%s" % element_infos['locator_value'])

    def move_mouse_to_element(self, element_infos):
        """鼠标悬停"""
        target = self.find_element(element_infos)
        ActionChains(self.driver).move_to_element(target).perform()
        logger.info("鼠标当前悬停在：%s" % element_infos['locator_value'])
