import logging
import time

import pytest

from data.product_data import product_data_info, product_select_info
from pages.product_page import ProductPage


@pytest.mark.product
class TestProduct():

    @pytest.mark.parametrize("test_info", product_data_info)
    def test_product_input_search(self, test_info, product):
        product_page = ProductPage(product)
        product_page.get_input(test_info['input_info'], test_info['data_info'])
        flag, product_data = product_page.get_data(test_info['data_info'])
        try:
            if flag:
                assert test_info['data_info'] in product_data
                logging.info("测试通过")
                product_page.save_screenshot(test_info['data_info'])
            else:
                assert test_info['none_data'] in product_data
                logging.info("测试通过")
                product_page.save_screenshot(test_info['data_info'])
        except AssertionError as e:
            logging.error("测试不通过:{}".format(e))
            raise e

    @pytest.mark.parametrize("test_info", product_select_info)
    def test_product_select_search(self, test_info, product):
        product_page = ProductPage(product)
        product_page.product_refresh()
        product_page.product_select(test_info['first_info'], test_info['data_info'])
        flag, product_data = product_page.get_data(test_info['data_info'])
        try:
            if flag:
                assert test_info['data_info'] in product_data
                logging.info("测试通过")
                product_page.save_screenshot(test_info['data_info'])
                time.sleep(2)
            else:
                assert test_info['none_data'] in product_data
                logging.info("测试通过")
                product_page.save_screenshot(test_info['data_info'])
                time.sleep(2)
        except AssertionError as e:
            logging.error("测试不通过:{}".format(e))
            raise e
