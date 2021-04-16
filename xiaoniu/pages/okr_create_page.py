from selenium.webdriver.common.by import By

from common.base_page import BasePage
from config import config


class OkrCreatePage(BasePage):
    url = config.HOST + '/#/project/okrs/add'
    okr_name_locator = (By.XPATH, "//input[@name='name']")

    okr_type_locator = (By.XPATH, "//app-select-dictionary[@placeholder= '请选择类型']")
    okr_type_click_locator = (By.XPATH, "//nz-option-item[@title = '业绩OKR']")

    okr_department_locator = (By.XPATH, "//nz-tree-select[@nzplaceholder= '请选择或搜索']")
    okr_department_click_locator = (By.XPATH, "//nz-tree-node-title[@title = '平台运营部']")

    okr_team_locator = (By.XPATH, "//div[@class='tag ng-star-inserted']")

    okr_auditor_locator = (By.XPATH, "//se[@label='审计员']//div[@class = 'tree-employee']")
    okr_confirm_locator = (By.XPATH, "//se[@label='确认人']//div[@class = 'tree-employee']")
    okr_auditor_click_locator = (By.XPATH, "//nz-tree-node-title[@title = '李雍彦']")

    okr_begin_time_locator = (By.XPATH, "//app-date-picker[@name='beginTime']//input")
    okr_end_time_locator = (By.XPATH, "//app-date-picker[@name='endTime']//input")
    okr_description_locator = (By.XPATH, "//textarea[@name= 'description']")

    okr_get_team_window_locator = (By.XPATH, "//i[@class = 'anticon anticon-ellipsis ng-star-inserted']")
    okr_team_number_locator = (By.XPATH, "//tr[@class = 'ant-table-row ng-star-inserted']")
    okr_check_box_locator = (By.XPATH, ".//input[@type = 'checkbox']")
    okr_submit_locator = (By.XPATH, "//button[@type = 'submit']")
    okr_save_locator = (By.XPATH, "//button[@m-acl = 'save']")

    def get(self):
        self.wb.get(self.url)
        return self

    def save_okr(self, okrname, begintime, endtime, description):
        """产品名称"""
        okr_name = self.find(self.okr_name_locator)
        okr_name.send_keys(okrname)
        """类型"""
        self.unusual_select(self.okr_type_locator, self.okr_type_click_locator)
        """所属部门"""
        self.unusual_select(self.okr_department_locator, self.okr_department_click_locator)
        """团队"""
        self.get_team_window(self.okr_get_team_window_locator, self.okr_team_number_locator, self.okr_submit_locator)
        """审计员"""
        self.unusual_select(self.okr_auditor_locator, self.okr_auditor_click_locator)
        """确认人"""
        self.unusual_select(self.okr_confirm_locator, self.okr_auditor_click_locator)

        """启动时间"""
        okr_begin_time = self.find(self.okr_begin_time_locator)
        okr_begin_time.send_keys(begintime)
        """计划完成时间"""
        okr_end_time = self.find(self.okr_end_time_locator)
        okr_end_time.send_keys(endtime)
        """okr描述"""
        okr_description = self.find(self.okr_description_locator)
        okr_description.send_keys(description)
        okr_description.click()
        """确定"""
        okr_save = self.wait_element_clickable(self.okr_save_locator)
        okr_save.click()
        return self

    def get_team_window(self, locator, locators, locator_submit):
        e = self.find(locator)
        e.click()
        team_nums = self.finds(locators)
        for i in range(len(team_nums)):
            team_name_index = "//tr[@data-index = {}]//span[@title= '李雍彦无敌团队']".format(str(i))
            team_name = self.find_split('xpath', team_name_index)
            if team_name is not None:
                check_box_index = "//tr[@data-index = {}]//input[@type= 'checkbox']".format(str(i))
                okr_check_box = self.find_split('xpath', check_box_index)
                okr_check_box.click()
                okr_submit = self.wait_element_clickable(locator_submit)
                okr_submit.click()
                return self
        print("没有找到元素")
        return self
