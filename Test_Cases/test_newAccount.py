# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
from Page_Objects.loginPage import Login
from Page_Objects.create_newAccount import NewAccountPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import excel_utilities


class Test_003_NewAccountCreation:
    baseURL = ReadConfig.getapplicationURL()
    path = "C:\\Users\\SKYNETT DRONES\\workspce_python\\Odoo_CRM_Automation\\Test_Data\\OdooCRMloginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_DDT(self, setup):
        self.logger.info("*************** Verifying Login DDT Test ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)

        self.rows = excel_utilities.getRowCount(self.path, 'Sheet1')
        print("No of rows in excel", self.rows)

        for r in range(2, self.rows + 1):
            self.user = excel_utilities.readData(self.path, 'Sheet1', r, 1)
            self.password = excel_utilities.readData(self.path, 'Sheet1', r, 2)
            self.exp = excel_utilities.readData(self.path, 'Sheet1', r, 3)

            self.lp.enter_username(self.user)
            self.lp.enter_password(self.password)
            self.lp.login_button_press()
            self.driver.implicitly_wait(10)

            act_title = self.driver.title
            exp_title = "Odoo"
            time.sleep(3)

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Passed *******")
                    time.sleep(2)
                    self.lp.find_userIcon()
                    self.lp.logout_fromOdoo()

                elif self.exp == "Fail":
                    self.logger.info("****** New Account Creation  *******")

                    self.NA = NewAccountPage(self.driver)
                    self.NA.create_newAccount()
                    self.NA.newAccount_emailField("ajithannadurai333@gmail.com")
                    self.NA.newAccount_userName("AjithKumar")
                    self.NA.newAccount_passwordField("Ajith@1234")
                    self.NA.newAccount_conformPasswordField("Ajith@1234")
                    self.NA.newAccount_signInButton()
                    time.sleep(3)
                    self.logger.info("****** New Account has been Created *******")
                    self.driver.close()
                    break
                else:
                    self.driver.close()
                    self.logger.info("****** New Account Creation Failed *******")

        self.logger.info("****** Test completed *******")
