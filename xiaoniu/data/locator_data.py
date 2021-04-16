from selenium.webdriver.common.by import By

home_locator = {"user_account_locator": (By.XPATH, "//div[@nzplacement  = 'bottomRight']"),
                "operation_locator": (By.XPATH, "//li[text() = '运营管理']"),
                "niu_product_locator": (By.XPATH, "//span[@title = '产品管理']"),
                "niu_workers_locator": (By.XPATH, "//span[@title = '设备管理']"),
                "niu_profits_locator": (By.XPATH, "//span[@title = '收益管理']"),
                "niu_powers_locator": (By.XPATH, "//span[@title = '耗电管理']"),
                "niu_wallets_locator": (By.XPATH, "//span[@title = '钱包管理']"),
                "niu_localwallets_locator": (By.XPATH, "//span[@title = '本地钱包管理']"),
                "niu_wallets_address_locator": (By.XPATH, "//span[@title = '//span[@title = '钱包地址管理']']"),
                "niu_recieveaccounts_locator": (By.XPATH, "//span[@title = '//span[@title = '收款帐号']"),
                "niu_flightSheet_locator": (By.XPATH, "//span[@title = '//span[@title = '飞行表管理']"),
                "niu_farms_locator": (By.XPATH, "//span[@title = '矿场管理']")
                }
