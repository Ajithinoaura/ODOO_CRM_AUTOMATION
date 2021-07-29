import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import pytest
from Page_Objects.loginPage import Login
# from Page_Objects.pipeline_Creation import crm_PipelineCreation
from Page_Objects.create_Customer import Create_Customer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_005_login:
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.driver = setup
        self.logger.info("*************** Login to Odoo ***************")
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.login_button_press()
        self.driver.implicitly_wait(10)
        self.logger.info("*************** Navigation to CRM Page ***************")
        self.lp.navigate_dashboard()
        time.sleep(2)
        self.lp.click_crm()
        time.sleep(3)
        self.logger.info("*************** Navigate Customer page ***************")
        self.CD = Create_Customer(self.driver)
        self.CD.click_SalesButton()
        self.CD.Click_Customer()
        time.sleep(5)
        self.CD.create_button()
        time.sleep(5)
        self.CD.CustomerName("Ravi")
        self.CD.Street("Anumadhanoor")
        self.CD.Street("Anumadhanoor")
        self.CD.City("Thirupathur")
        # self.CD.State("tamilnadu (PE)")

        self.CD.ZipCode("635901")
        self.CD.Americansomoa("Afghanistan")
        self.CD.TaxID("ID000000001")
        self.CD.Job_Position("Avenger")
        self.CD.PhoneField("(65) 6892 2308")
        self.CD.MobileField("8925739053")
        self.CD.EmailField("nexusrobotech@gmail.com")
        self.CD.Website("www.Amazon.com")
        # self.CD.Title("Doctor")
        # self.CD.Tags("Happy Customer")
        # self.CD.click_AddImage()
        time.sleep(3)
        self.CD.click_Add()
        time.sleep(3)
        self.CD.save()
        time.sleep(2)
        self.driver.close()
        self.logger.info("*************** Customer Added Successfully ***************")
        self.logger.info("*************** Test Completed ***************")
