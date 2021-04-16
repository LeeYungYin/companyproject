from selenium.webdriver.common.by import By


class UserPage():
    # 查看余额
    money_locator = (By.XPATH, "//li[@class= 'color_sub']")

    def __init__(self, wb):
        self.wb = wb

    def get_money(self):
        """获取余额"""
        e = self.wb.find_element(*self.money_locator)
        return e.text[:-1]
