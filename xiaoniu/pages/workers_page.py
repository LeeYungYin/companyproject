import logging
import time

from selenium.webdriver.common.by import By
from config import config
from pages.product_page import ProductPage


class WorkersPage(ProductPage):
    url = config.HOST + '#/worker/workers'
    totalcount_locator = (By.XPATH, "//nz-pagination//li[@class = 'ant-pagination-total-text ng-star-inserted']")

    def get(self):
        self.wb.get(self.url)
        return self

    def workers_refreash(self):
        self.product_refresh()
        return self

    def workers_select(self, first, second):
        self.product_select(first, second)
        return self

    def get_box(self, name, data, total=None):
        """所有可以点击的查询按钮"""
        if isinstance(data, dict):
            if total is None:
                workers_data = self.data_dict(name, data)
                if workers_data:
                    flag = True
                    return flag, name
                else:
                    flag = False
                    no_data = self.wait_element_visible(self.none_data_locator)
                    return flag, no_data
            else:
                workers_data = self.data_dict_count(name, data)
                if workers_data:
                    flag = True
                    return flag, name
                else:
                    flag = False
                    no_data = self.wait_element_visible(self.none_data_locator)
                    return flag, name
        elif isinstance(data, list):
            if total is None:
                workers_data = self.data_list(name, data)
                if workers_data:
                    flag = True
                    return flag, name
                else:
                    flag = False
                    no_data = self.wait_element_visible(self.none_data_locator)
                    return flag, no_data
            else:
                workers_data = self.data_list_count(name, data)
                if workers_data:
                    flag = True
                    return flag, name
                else:
                    flag = False
                    no_data = self.wait_element_visible(self.none_data_locator)
                    return flag, no_data
        else:
            return TypeError

    def data_dict(self, name, data: dict):
        for key, value in data.items():
            box_locator = (By.XPATH, "//se[@label = '" + name + "']//nz-tag[contains(text(),'" + key + "')]")
            self.click_element(box_locator)
            time.sleep(1)
            data_locator = (By.XPATH, "//td//*[text()='" + value + "']")
            data_name = self.finds(data_locator)
            return data_name

    def data_dict_count(self, name, data: dict):
        number = []
        totalnumber = []
        for key, value in data.items():
            box_locator = (By.XPATH, "//se[@label = '" + name + "']//nz-tag[contains(text(),'" + key + "')]")
            self.click_element(box_locator)
            time.sleep(1)
            count = self.find(self.totalcount_locator).text
            if value == '':
                totalnumber.append(self.string_get_number(count))
            else:
                number.append(self.string_get_number(count))
        number = sum(number)
        try:
            assert totalnumber[0] == number
            if totalnumber != ['0']:
                return data
        except AssertionError as e:
            logging.error(e)
            raise e

    def data_list(self, name, data: list):
        for i in data:
            box_locator = (By.XPATH, "//se[@label = '" + name + "']//nz-tag[contains(text(),'" + i + "')]")
            self.click_element(box_locator)
            time.sleep(1)
            data_locator = (By.XPATH, "//td//*[text()='" + i + "']")
            data_name = self.finds(data_locator)
            return data_name

    def data_list_count(self, name, data: list):
        number = []
        totalnumber = []
        for i in data:
            box_locator = (By.XPATH, "//se[@label = '" + name + "']//nz-tag[contains(text(),'" + i + "')]")
            self.click_element(box_locator)
            time.sleep(1)
            count = self.find(self.totalcount_locator).text
            if i == '全部':
                totalnumber.append(self.string_get_number(count))
            else:
                number.append(self.string_get_number(count))
        number = sum(number)
        try:
            assert totalnumber[0] == number
            if totalnumber != ['0']:
                return data
        except AssertionError as e:
            logging.error(e)
            raise e

    def wokrers_time(self, name, data: list):
        createtime_locator = (By.XPATH, "//se[@label = '" + name + "']//input")
        workers_time = self.finds(createtime_locator)
        for i in range(len(workers_time)):
            workers_time[i].send_keys(data[i])
        time_locator = (By.XPATH, "//span[contains(text(),'" + data[0] + "')]")
        time_name = self.finds(time_locator)
        if time_name:
            flag = True
            return flag, name
        else:
            flag = False
            no_data = self.wait_element_visible(self.none_data_locator)
            return flag, no_data
