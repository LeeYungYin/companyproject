from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import config
from common.base_page import BasePage


class LoginPage(BasePage):
    url = config.HOST + r"/#/passport/login"
    account_locator = (By.XPATH, "//input[@formcontrolname = 'account']")
    password_locator = (By.XPATH, "//input[@type = 'password']")
    submit_locator = (By.XPATH, "//button[@type = 'submit']")
    account_not_exist_locator = (By.XPATH, "//span[contains(text(),'手机号码不存在')]")
    account_is_empty_locator = (By.XPATH, "//div[contains(text(),'请输入手机号码')]")
    password_is_empty_locator = (By.XPATH, "//div[contains(text(),'请输入密码')]")

    def get(self):
        self.wb.get(self.url)
        return self

    def login(self, account, pwd):
        # 定位用户
        username_elem = self.find(self.account_locator)
        username_elem.send_keys(account)
        # 定位密码
        pwdname_elem = self.find(self.password_locator)
        pwdname_elem.send_keys(pwd)
        # 提交
        login_btn_elem = self.find(self.submit_locator)
        login_btn_elem.click()
        return self

    def get_account_not_exist_msg(self):
        """获取手机不存在信息"""
        e = self.wait_element_present(self.account_not_exist_locator)
        return e.text

    def get_account_is_empty_msg(self):
        """获取账号为空信息"""
        e = self.wait_element_visible(self.account_is_empty_locator)
        return e.text

    def get_password_is_empty_msg(self):
        """获取密码为空信息"""
        e = self.wait_element_visible(self.password_is_empty_locator)
        return e.text
