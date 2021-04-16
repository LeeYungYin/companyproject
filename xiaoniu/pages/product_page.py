from selenium.webdriver.common.by import By
from config import config
from common.base_page import BasePage


class ProductPage(BasePage):
    url = config.HOST + '#/product/products'
    refrech_locator = (By.XPATH, "//button[@title = '重置']")
    none_data_locator = (By.XPATH, "//p[contains(text(),'暂无数据')]")

    def get(self):
        """访问当前页面"""
        self.wb.get(self.url)
        return self

    def get_input(self, name: str, sendname):
        """获取插入的查询数据"""
        input_locator = (By.XPATH, '//input[@placeholder = "' + name + '"]')
        input_name = self.find(input_locator)
        input_name.send_keys(sendname)
        return self

    def product_refresh(self):
        self.refresh(self.refrech_locator)
        return self

    def get_data(self, name):
        """获取页面查询数据"""
        data_locator = (By.XPATH, "//td//*[contains(text(), '" + name + "')]")
        data_name = self.finds(data_locator)
        if data_name:  # 如果页面查询元素存在
            flag = True
            for i in range(len(data_name)):  # 如果遍历的文本都是和name一致的话，返回name
                if name not in data_name[i].text:
                    self.save_screenshot(name)
                    return self
            return flag, name
        else:  # 如果页面查询元素不存在
            flag = False
            no_okr_data = self.wait_element_visible(self.none_data_locator)
            if no_okr_data:
                return flag, no_okr_data.text
            return self

    def product_select(self, first, second):
        first_locator = (By.XPATH, "//se[@label = '" + first + "']//input")
        second_locator = (By.XPATH, "//div[text()='" + second + "']")
        self.unusual_select(first_locator, second_locator)
        return self
