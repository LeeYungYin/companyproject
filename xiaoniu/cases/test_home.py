import logging
import time
import pytest
from data.list_data import list_info
from pages.home_page import HomePage


@pytest.mark.niu
class TestHome():

    @pytest.mark.parametrize("test_info", list_info)
    def test_home_list_click(self, test_info, login):
        home_page = HomePage(login)
        home_page.get_operation()
        major_info = home_page.click_list(test_info['list']).click_detail(test_info['name']) \
            .get_element(test_info["expected"])
        time.sleep(3)
        try:
            assert test_info["expected"] == major_info
            logging.info("测试用例通过")
            home_page.save_screenshot(test_info['list'])
            time.sleep(2)
        except AssertionError as e:
            logging.error("测试用例不通过{}".format(e))
            raise e
