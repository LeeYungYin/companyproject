import time
import logging
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from data.login_data import case_uninvalid, case_success, case_error


@pytest.mark.success
class TestLogin():

    @pytest.mark.parametrize("test_info", case_success)
    def test_login_success(self, test_info, browser):
        """登录成功"""
        login_page = LoginPage(browser)
        login_page.get().login(test_info["mobile"], test_info["password"])
        user_info = HomePage(browser).get_user_account()
        try:
            assert test_info["expected"] in user_info  # 用包含关系不用等于关系
            logging.info("测试用例通过")
            time.sleep(2)
        except AssertionError as e:
            logging.error("测试用例不通过:{}".format(e))
            raise e

    @pytest.mark.parametrize("test_info", case_error)
    def test_login_empty_moblie(self, test_info, browser): # 第一个参数为用例 第二个参数为前置条件的浏览器对象
        """账号密码为空"""
        login_page = LoginPage(browser)
        login_page.get().login(test_info["mobile"], test_info["password"])
        # 获取实际结果
        if test_info["tag"] == "account":
            error_msg_elem = login_page.get_account_is_empty_msg()
        if test_info["tag"] == "password":
            error_msg_elem = login_page.get_password_is_empty_msg()
        # 断言
        try:
            assert test_info["expected"] == error_msg_elem
            logging.info("测试用例通过")
            time.sleep(2)
        except AssertionError as e:
            logging.error("测试用例不通过:{}".format(e))
            raise e

    @pytest.mark.parametrize("test_info", case_uninvalid)
    def test_account_not_exist(self, test_info, browser):
        """账号不存在"""
        login_page = LoginPage(browser)
        login_page.get().login(test_info["mobile"], test_info["password"])
        # 获取实际结果
        error_msg_elem = login_page.get_account_not_exist_msg()
        # 断言
        try:
            assert test_info["expected"] == error_msg_elem
            logging.info("测试用例通过")
            time.sleep(2)
        except AssertionError as e:
            logging.error("测试用例不通过:{}".format(e))
            raise e
