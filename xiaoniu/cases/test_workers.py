import logging
import time

import pytest

from cases.test_product import TestProduct
from data.workers_data import workers_data_info, workers_select_info, workers_click_info, workers_time_info
from pages.workers_page import WorkersPage


@pytest.mark.niu
class TestWorkers(TestProduct):
    @pytest.mark.parametrize("test_info", workers_data_info, )
    def test_workers_input_search(self, test_info, workers):
        """输入框查询"""
        workers_page = WorkersPage(workers)
        workers_page.workers_refreash()
        workers_page.get_input(test_info['input_info'], test_info['data_info'])
        flag, workers_data = workers_page.get_data(test_info['data_info'])
        try:
            if flag:
                assert test_info['data_info'] in workers_data
                logging.info("测试通过")
                time.sleep(2)
                workers_page.save_screenshot(test_info['data_info'])
            else:
                assert test_info['none_data'] in workers_data
                logging.info("测试通过")
                time.sleep(2)
                workers_page.save_screenshot(test_info['data_info'])
        except AssertionError as e:
            logging.error("测试不通过{}".format(e))
            workers_page.save_screenshot(test_info['data_info'])
            raise e

    @pytest.mark.parametrize("test_info", workers_select_info)
    def test_workers_select_search(self, test_info, workers):
        """下拉框查询"""
        workers_page = WorkersPage(workers)
        workers_page.workers_refreash()
        workers_page.workers_select(test_info['first_info'], test_info['data_info'])
        flag, workers_data = workers_page.get_data(test_info['data_info'])
        try:
            if flag:
                assert test_info['data_info'] in workers_data
                logging.info("测试通过")
                time.sleep(2)
                workers_page.save_screenshot(test_info['data_info'])
            else:
                assert test_info['none_data'] in workers_data
                logging.info("测试通过")
                time.sleep(2)
                workers_page.save_screenshot(test_info['data_info'])
        except AssertionError as e:
            logging.error("测试不通过{}".format(e))
            workers_page.save_screenshot(test_info['data_info'])
            raise e

    @pytest.mark.parametrize("test_info", workers_click_info)
    def test_workers_box_search(self, test_info, workers):
        """点击框查询"""
        workers_page = WorkersPage(workers)
        workers_page.workers_refreash()
        flag, workers_data = workers_page.get_box(test_info['first_info'], test_info['second_info'],
                                                  test_info['total_info'])
        try:
            if flag:
                assert test_info['first_info'] in workers_data
                logging.info("测试通过")
                time.sleep(2)
                workers_page.save_screenshot(test_info['first_info'])
            else:
                assert test_info['none_data'] in workers_data
                logging.info("测试通过")
                time.sleep(2)
                workers_page.save_screenshot(test_info['first_info'])
        except AssertionError as e:
            logging.error("测试不通过{}".format(e))
            workers_page.save_screenshot(test_info['first_info'])
            raise e

    @pytest.mark.parametrize("test_info", workers_time_info)
    def test_workers_time_search(self, test_info, workers):
        """时间插件查询"""
        workers_page = WorkersPage(workers)
        workers_page.workers_refreash()
        flag, workers_data = workers_page.wokrers_time(test_info['first_info'], test_info['second_info'])
        try:
            if flag:
                assert test_info['first_info'] in workers_data
                logging.info("测试通过")
                time.sleep(2)
                workers_page.save_screenshot(test_info['first_info'])
            else:
                assert test_info['none_data'] in workers_data
                logging.info("测试通过")
                time.sleep(2)
                workers_page.save_screenshot(test_info['first_info'])
        except AssertionError as e:
            logging.error("测试不通过{}".format(e))
            workers_page.save_screenshot(test_info['first_info'])
            raise e