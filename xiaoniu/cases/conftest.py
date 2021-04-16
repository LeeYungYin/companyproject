import os
import sys

sys.path.append(os.getcwd())
import pytest
from selenium import webdriver
from config import config
from pages.login_page import LoginPage
from data.login_data import case_success
from pages.home_page import HomePage


@pytest.fixture(scope="class")
def browser():
    """
启动浏览器和关闭浏览器
前置条件一般用yield 返回参数给测试用例，等用例执行完才执行yield后面的内容
    """
    wb = webdriver.Chrome(r'D:\Myfile\chromedriver\chromedriver.exe')
    wb.implicitly_wait(config.IMPLICTLY_WAIT_TIMEOUT)
    wb.maximize_window()
    yield wb
    wb.quit()


@pytest.fixture(scope="class")
def refresh(browser):
    """
    用例之间刷新浏览器
    """
    browser.refresh()


@pytest.fixture(scope="class")
def login(browser):
    """前置登录"""
    # 调用login_page 的login()函数
    # borwser 代表的是borwser的返回值 driver
    login_page = LoginPage(browser)
    # 传入正确的手机号码和密码
    user_info = case_success[0]
    login_page.get().login(user_info["mobile"], user_info["password"])
    yield browser


@pytest.fixture(scope="class")
def product(login):
    """前置产品管理页面"""
    home_page = HomePage(login)
    home_page.click_product_list().click_product_detail()
    yield login

@pytest.fixture(scope="class")
def workers(login):
    """前置设备管理页面"""
    home_page = HomePage(login)
    home_page.click_workers_list().click_workers_detail()
    yield login
