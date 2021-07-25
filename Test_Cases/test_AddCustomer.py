import time
from Page_Objects.loginPage import Login
# from Page_Objects.pipeline_Creation import crm_PipelineCreation
from Page_Objects.create_Customer import Create_Customer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_004_login:
    baseURL = ReadConfig.getapplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_Create_Pipeline(self, setup):
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
        time.sleep(1)
        self.lp.click_crm()
        self.CD = Create_Customer(self.driver)
        self.CD.click_SalesButton()
        self.CD.Click_Customer()
        act_title = self.driver.title
        self.driver.implicitly_wait(5)
        if act_title == "Customers - Odoo":
            print("Create button pressed")
            self.logger.info("*************** customer details could be added***************")

        else:
            self.driver.save_screenshot("..\\Screenshots\\" + "test_CRMPageNavigation.png")
            self.driver.close()
            self.logger.warning("*************** CRM Main Page Verification Failed ***************")

        self.CD.create_button()
        self.CD.CustomerName("Tony Stark")

        # self.CD.Click_office()
        # self.CD.Street("Anumadhanoor")
        # self.CD.City("Thirupathur")
        # self.CD.ASOTA()
        # self.CD.ZipCode("635901")
        # self.CD.Americansomoa()
        # self.CD.TaxID("ID000000001")
        # self.CD.Job_Position("Avenger")
        # self.CD.PhoneField("(65) 6892 2308")
        # self.CD.MobileField("8925739053")
        # self.CD.EmailField("nexusrobotech@gmail.com")
        # self.CD.Title()
        # self.CD.Tags("Live the moment")
        # self.CD.click_AddImage("D:\\Aeroajith\\Ironman.jpg")
        # self.CD.click_Add()
        time.sleep(2)
        self.driver.close()
        #
        # self.logger.info("*************** Customer Added Successfully ***************")
        # self.logger.info("*************** Test Completed ***************")
