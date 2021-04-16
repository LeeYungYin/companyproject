import logging
import os
import re
import time

from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from config import config
from datetime import datetime
from pywinauto import Desktop


class BasePage:
    """
    基础封装函数
    """

    def __init__(self, wb: Chrome):
        self.wb = wb

    def find(self, locator):
        """获取元素"""
        try:
            e = self.wb.find_element(*locator)
            return e
        except Exception as error:
            logging.error(f"元素定位失败：{error}")
            return False

    def find_split(self, locatortype, locatorname):
        """获取元素"""
        try:
            if locatortype == 'xpath':
                e = self.wb.find_element_by_xpath(locatorname)
            if locatortype == 'id':
                e = self.wb.find_element_by_id(locatorname)
            if locatortype == 'name':
                e = self.wb.find_element_by_name(locatorname)
            return e
        except Exception as error:
            logging.error(f"元素定位失败：{error}")
            return False

    def find_exist(self, locator):
        """元素是否存在"""
        flag = True
        e = self.find(locator)
        if e is not False:
            return flag, e
        else:
            flag = False
            return flag, e

    def finds(self, locator):
        """获取多个元素"""
        try:
            e = self.wb.find_elements(*locator)
            return e
        except Exception as error:
            logging.error(f"元素定位失败：{error}")
            return False

    def finds_exist(self, locator):
        """元素多个是否存在"""
        flag = True
        e = self.wb.finds(locator)
        if e is not False:
            return flag
        else:
            flag = False
            return flag

    def save_screenshot(self, name=None):
        """截屏"""
        img_path = config.IMG_PATH
        # 生成截图的文件名
        ts_str = datetime.now().strftime("%y-%m-%d-%H_%M_%S")
        if name is None:
            file_name = os.path.join(img_path, ts_str + ".png")
        else:
            file_name = os.path.join(img_path, name + ts_str + ".png")
        self.wb.save_screenshot(file_name)
        return self

    def wait_element_clickable(self, locator, timeout=20, poll_frequency=0.2):
        """等待元素被点击"""
        wait = WebDriverWait(self.wb, timeout, poll_frequency)
        try:
            e = wait.until(expected_conditions.element_to_be_clickable(locator))
            return e
        except Exception as error:
            logging.error(f"元素定位失败{error}")
            return False

    def wait_element_visible(self, locator, timeout=20, poll_frequency=0.2):
        """等待元素可见"""
        wait = WebDriverWait(self.wb, timeout, poll_frequency)
        try:
            e = wait.until(expected_conditions.visibility_of_element_located(locator))
            return e
        except Exception as error:
            logging.error(f"元素定位失败{error}")
            return False

    def wait_element_present(self, locator, timeout=20, poll_frequency=0.2):
        """等待元素加载"""
        wait = WebDriverWait(self.wb, timeout, poll_frequency)
        try:
            e = wait.until(expected_conditions.presence_of_element_located(locator))
            return e
        except Exception as error:
            logging.error(f"元素定位失败{error}")
            return False

    def wait_elements_visible(self, locator, timeout=20, poll_frequency=0.2):
        """等待多个元素可见"""
        wait = WebDriverWait(self.wb, timeout, poll_frequency)
        try:
            e = wait.until(expected_conditions.visibility_of_all_elements_located(locator))
            return e
        except Exception as error:
            logging.error(f"元素定位失败{error}")
            return False

    def wait_elements_present(self, locator, timeout=20, poll_frequency=0.2):
        """等待多个元素加载"""
        wait = WebDriverWait(self.wb, timeout, poll_frequency)
        try:
            e = wait.until(expected_conditions.presence_of_all_elements_located(locator))
            return e
        except Exception as error:
            logging.error(f"元素定位失败{error}")
            return False

    def click_element(self, locator):
        """点击某个元素"""
        e = self.wait_element_clickable(locator)
        e.click()
        return self

    def double_click_element(self, locator):
        """双击某个元素"""
        e = self.wait_element_clickable(locator)
        ac = ActionChains(self.wb)
        ac.double_click(e).perform()
        return self

    def move_to(self, locator):
        """鼠标悬停"""
        e = self.wait_element_clickable(locator)
        ac = ActionChains(self.wb)
        ac.move_to_element(e).perform()
        return self

    def drag_and_drop(self, source_locator, target_locator):
        """拖拽"""
        e1 = self.wait_element_clickable(source_locator)
        e2 = self.wait_element_clickable(target_locator)
        ac = ActionChains(self.wb)
        ac.drag_and_drop(e1, e2).perform()
        return self

    """右击"""

    """窗口切换"""

    def switch_to_iframe(self, e, wait=False):
        """iframe切换"""
        if not wait:
            self.switch_to_iframe(e)
            return self
        wait = WebDriverWait(self.wb, 30)
        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(e))
        return self

    def screen_shot(self):
        """截图"""
        pic_name = os.path.join(self.img_path, str(int(time.time())) + 'jpg')
        self.wb.save_screenshot(pic_name)
        return self

    def window_scroll(self, width=None, height=None):
        """窗口滚动"""
        if width is None:
            width = "0"
        if height is None:
            height = "0"

        js = "window.scrollTo({w},{h});".format(w=width, h=height)
        self.wb.execute_script(js)
        return self

    def refresh(self, locator):
        """刷新页面"""
        e = self.find(locator)
        e.click()
        return self

    def select(self, locator):
        """下拉框选择"""
        e = self.find(locator)
        s = Select(e)
        return s

    def unusual_select(self, first_locator, second_locator):
        """没有select标签的下拉框操作"""
        e = self.find(first_locator)
        e.click()
        e = self.wait_element_clickable(second_locator)
        e.click()
        return self

    def unusual_upload(self, locator, path):
        """系统上传操作"""
        e = self.find(locator)
        e.click()
        app = Desktop()
        dialog = app['打开']
        dialog['Edit'].type.keys(path)
        dialog['Button'].click()
        return self

    def string_get_number(self,strings):
        numbers = re.findall(r"\d+", strings)
        numbers = numbers.pop()
        return int(numbers)
