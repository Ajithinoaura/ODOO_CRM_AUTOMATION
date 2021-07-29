# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
# import pytest
from Page_Objects.loginPage import Login
from Page_Objects.pipeline_Creation import crm_PipelineCreation
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_004_login:
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    # def test_CRMPageNavigation(self, setup):
    #     self.driver = setup
    #     self.logger.info("*************** Login to Odoo ***************")
    #     self.driver.get(self.baseURL)
    #     self.lp = Login(self.driver)
    #     self.lp.enter_username(self.username)
    #     self.lp.enter_password(self.password)
    #     self.lp.login_button_press()
    #     self.driver.implicitly_wait(8)
    #     self.logger.info("*************** Navigation to CRM Page ***************")
    #     self.lp.navigate_dashboard()
    #     self.lp.click_crm()
    #     time.sleep(3)
    #     act_title = self.driver.title
    #     self.driver.implicitly_wait(5)
    #
    #     if act_title == "Odoo":
    #         self.logger.info("*************** CRM Main Page Verification Passed ***************")
    #         assert True
    #
    #     else:
    #         self.driver.save_screenshot("..\\Screenshots\\" + "test_CRMPageNavigation.png")
    #         self.driver.close()
    #         self.logger.warning("*************** CRM Main Page Verification Failed ***************")
    #         assert False
    #
    # time.sleep(2)
    # @pytest.mark.regression
    def test_Create_Pipeline(self, setup):
        self.driver = setup
        self.logger.info("*************** Login to Odoo ***************")
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.login_button_press()
        self.driver.implicitly_wait(8)
        self.logger.info("*************** Navigation to CRM Page ***************")
        self.lp.navigate_dashboard()
        self.lp.click_crm()
        self.PC = crm_PipelineCreation(self.driver)
        time.sleep(3)
        self.logger.info("*************** Creating Pipeline ***************")
        self.PC.click_createButton()
        self.PC.opportunity_field("Ragu")
        self.PC.enter_emailField("Raguvaran123@123")
        self.PC.enter_phoneFiled("9845673890")
        self.PC.enter_expectedRevenue_Field("1200")
        self.PC.click_createButton()
        self.logger.info("*************** Pipeline Created Successfully ***************")
        time.sleep(5)
        self.logger.info("*************** Pipeline Edit the Fields ***************")
        self.PC.Select_pipeline()
        self.PC.click_edit()
        self.PC.Edit_opportunities("Raja")
        self.PC.Edit_Email_1("rajaguru@gmail.com")
        self.PC.Edit_phone_1("8925747893")
        self.PC.Add_description("Raja is looking for to create business with us")
        self.PC.click_save()
        self.driver.close()
        self.logger.info("*************** Pipeline Edited Successfully ***************")

        self.logger.info("*************** Test Completed ***************")
