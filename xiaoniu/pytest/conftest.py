import pytest
from selenium import webdriver

"""
conftest.py固定文件，不需要导入函数 直接可以调用函数
"""


@pytest.fixture(scope="class", autouse=True)
# class：每一个类启动一次浏览器 module：每一个模块启动一次浏览器 package：
# 每一个包启动一次浏览器 session：全局对象启动一次浏览    器
# autouse 自动调用夹具，无需传函数，谨慎使用

def before_test_and_after():
    """启动浏览器"""
    print("正在启动浏览器")
    driver = webdriver.Chrome()
    yield driver  # 返回参数，但是程序不终止

    driver.quit()
