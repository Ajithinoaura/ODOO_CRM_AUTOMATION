# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
from Page_Objects.loginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_login:
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*************** Test_001_login ***************")
        self.logger.info("*************** Verifying Login Test ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.login_button_press()
        self.driver.close()

        self.logger.info("*************** Login Test Passed ***************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_CRMPageNavigation(self, setup):
        self.logger.info("*************** Verifying Odoo Main Page ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.login_button_press()
        self.driver.implicitly_wait(8)
        self.logger.info("*************** Navigation to CRM Page ***************")
        self.lp.navigate_dashboard()
        self.lp.click_crm()
        time.sleep(3)
        act_title = self.driver.title
        time.sleep(3)

        if act_title == "Odoo":
            self.driver.close()
            self.logger.info("*************** CRM Main Page Verification Passed ***************")
            assert True
        else:
            self.driver.save_screenshot("..\\Screenshots\\" + "test_CRMPageNavigation.png")
            self.driver.close()
            self.logger.warning("*************** CRM Main Page Verification Failed ***************")
            assert False
