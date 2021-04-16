from selenium.webdriver.common.by import By
from config import config
from common.base_page import BasePage
from data.locator_data import home_locator
from pages.product_page import ProductPage
from pages.workers_page import WorkersPage


class HomePage(BasePage):
    url = config.HOST + '#/dashboard'
    locator = home_locator

    def get(self):
        """访问首页"""
        self.wb.get(self.url)
        return self

    def get_user_account(self):
        """获取用户账号信息"""
        # e = self.wait_element_visible(self.user_account_locator)
        e = self.wait_element_visible(self.locator['user_account_locator'])
        return e.text

    def get_operation(self):
        """点击运营管理标签"""
        # e = self.find(self.operation_locator)
        e = self.find(self.locator['operation_locator'])
        e.click()
        return self

    def click_product_list(self):
        """点击箭头打开产品管理"""
        # e = self.finds(self.niu_product_locator)
        e = self.finds(self.locator['niu_product_locator'])
        e[0].click()
        return self

    def click_product_detail(self):
        """点击产品管理进入详情页"""
        # e = self.finds(self.niu_product_locator)
        e = self.finds(self.locator['niu_product_locator'])
        e[1].click()
        return ProductPage(self.wb)

    def click_workers_list(self):
        """点击箭头打开设备管理"""
        #  = self.finds(self.niu_workers_locator)
        e = self.finds(self.locator['niu_workers_locator'])
        e[0].click()
        return self

    def click_workers_detail(self):
        """点击设备管理进入详情页"""
        # e = self.finds(self.niu_workers_locator)
        e = self.finds(self.locator['niu_workers_locator'])
        e[1].click()
        return WorkersPage(self.wb)

    def click_flightsheets_detail(self):
        """点击设备飞行表汇总详情页"""
        # e = self.find(self.niu_workers_flightsheets_locator)
        e = self.find(self.locator['niu_workers_flightsheets_locator'])
        e.click()
        return self  # WorkersFlightsheetsPage(self.wb)

    def click_profits_list(self):
        """点击箭头打开收益管理"""
        # e = self.finds(self.niu_profits_locator)
        e = self.finds(self.locator['niu_profits_locator'])
        e[0].click()
        return self

    def click_profits_detail(self):
        """点击收益管理详情页"""
        # e = self.finds(self.niu_profits_locator)
        e = self.finds(self.locator['niu_profits_locator'])
        e[1].click()
        return self  # ProfitsPage(self.wb)

    def click_powers_list(self):
        """点击箭头打开耗电管理"""
        # e = self.finds(self.niu_powers_locator)
        e = self.finds(self.locator['niu_powers_locator'])
        e[0].click()
        return self

    def click_powers_detail(self):
        """点击耗电管理详情页"""
        # e = self.finds(self.niu_powers_locator)
        e = self.finds(self.locator['niu_powers_locator'])
        e[1].click()
        return self  # PowersPage(self.wb)

    def click_wallets_list(self):
        """点击箭头打开钱包管理"""
        # e = self.find(self.niu_wallets_locator)
        e = self.find(self.locator['niu_wallets_locator'])
        e.click()
        return self

    def click_localwallets_detail(self):
        """点击打开本地钱包管理详情页"""
        # e = self.find(self.niu_localwallets_locator)
        e = self.find(self.locator['niu_localwallets_locator'])
        e.click()
        return self  # LocalWalletsPage(self.wb)

    def click_walletsaddress_detail(self):
        """点击打开钱包地址管理详情页"""
        # e = self.find(self.niu_wallets_address_locator)
        e = self.find(self.locator['niu_wallets_address_locator'])
        e.click()
        return self  # WalletsAddressPage(self.wb)

    def click_recieveaccounts_detail(self):
        """点击打开收款账号详情页"""
        # e = self.find(self.niu_recieveaccounts_locator)
        e = self.find(self.locator['niu_recieveaccounts_locator'])
        e.click()
        return self  # RecieveaccountsPage(self.wb)

    def click_flightSheet_list(self):
        """点击箭头打开飞行表管理"""
        # e = self.finds(self.niu_flightSheet_locator)
        e = self.finds(self.locator['niu_flightSheet_locator'])
        e[0].click()
        return self

    def click_flightSheet_detail(self):
        """点击打开飞行表管理详情页"""
        # e = self.finds(self.niu_flightSheet_locator)
        e = self.finds(self.locator['niu_flightSheet_locator'])
        e[1].click()
        return self  # FlightSheetPage(self.wb)

    def click_farms_list(self):
        """点击箭头打开矿场管理"""
        # e = self.finds(self.niu_farms_locator)
        e = self.finds(self.locator['niu_farms_locator'])
        e[0].click()
        return self

    def click_farms_detail(self):
        """点击打开矿场管理详情页"""
        # e = self.finds(self.niu_farms_locator)
        e = self.finds(self.locator['niu_farms_locator'])
        e[1].click()
        return self  # FarmsPage(self.wb)

    def click_list(self, name):
        list_locator = (By.XPATH, "//span[@title = '" + name + "']")
        e = self.find(list_locator)
        e.click()
        return self

    def click_detail(self, name):
        detail_locator = (By.XPATH, "//span[@title = '" + name + "']")
        e = self.wait_elements_visible(detail_locator)
        if len(e) > 1:
            e[1].click()
            return self
        else:
            e[0].click()
            return self

    def get_element(self, name):
        element_locator = (By.XPATH, "//span[text()='" + name + "']")
        self.find(element_locator)
        return name
