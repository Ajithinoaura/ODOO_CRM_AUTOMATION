# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
from Page_Objects.loginPage import Login
# from Page_Objects.create_newAccount import NewAccountPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils


class Test_002_login_DDT:
    baseURL = ReadConfig.getapplicationURL()
    path = "C:\\Users\\SKYNETT DRONES\\workspce_python\\Odoo_CRM_Automation\\Test_Data\\OdooCRMloginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_DDT(self, setup):
        self.logger.info("*************** Test_002_DDT_login ***************")
        self.logger.info("*************** Verifying Login DDT Test ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("No of rows in excel", self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

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
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("****** Failed *******")
                    lst_status.append("Pass")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("***** Failed *******")
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("****** Passed *******")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("******** Login DDT Test is Passed ")
            self.driver.close()
            assert True
        else:
            self.logger.info("******** Login DDT Test is Failed ")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed Test_002_DDT_login ************* ")
