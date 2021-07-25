# from selenium.webdriver.common.keys import Keys


class Create_Customer:
    Sales_Button_by_xpath = "//a[normalize-space()='Sales']"
    Click_customer_button_by_xpath = "//span[normalize-space()='Customers']"
    Click_Create_Button_by_xpath = "//button[normalize-space()='Create']"
    # Select_office_By_xpath = "//input[@class='o_input'][@type='text'][@placeholder='Name']"
    Customer_Name_by_xpath = "//input[@class='o_input'][@type='text'][@placeholder='Name']"
    # Street_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/input[1]"
    # City_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/input[3]"
    # AsotaIT_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]/input[1]"
    # ZipCode_by_path = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/input[4]"
    # AmericanSomoa_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[2]/div[1]/input[1]"
    # TaxID_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[1]/tbody[1]/tr[3]/td[2]/div[1]/input[1]"
    # JobPosition_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[2]/tbody[1]/tr[1]/td[2]/input[1]"
    # phoneField_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[5]/table[2]/tbody[1]/"
    # MobileField_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[2]/tbody[1]/tr[7]/td[2]/div[1]/input[1]"
    # emailField_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[2]/tbody[1]/tr[11]/td[2]/div[1]/input[1]"
    # WebsiteField_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[2]/tbody[1]/tr[12]/td[2]/input[1]"
    # Title_by_xpath = "//a[normalize-space()='Madam']"
    # Tags_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[2]/tbody[1]/tr[16]/td[2]/div[1]"
    # AddImage_by_xpath = "//button[@title='Edit']"
    # AddButton_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[6]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def click_SalesButton(self):
        self.driver.find_element_by_xpath(self.Sales_Button_by_xpath).click()

    def Click_Customer(self):
        self.driver.find_element_by_xpath(self.Click_customer_button_by_xpath).click()

    def create_button(self):
        self.driver.find_element_by_xpath(self.Click_Create_Button_by_xpath).click()

    # def Click_office(self):
    #     self.driver.find_element_by_xpath(self.Select_office_By_xpath).click()

    def CustomerName(self, name):
        self.driver.find_element_by_xpath(self.Customer_Name_by_xpath).clear()
        self.driver.find_element_by_xpath(self.Customer_Name_by_xpath).send_keys(name)
    #
    # def Street(self, street):
    #     self.driver.find_element_by_xpath(self.Street_by_xpath).clear()
    #     self.driver.find_element_by_xpath(self.Street_by_xpath).send_keys(street)
    #
    # def City(self, city):
    #     self.driver.find_element_by_xpath(self.City_by_xpath).clear()
    #     self.driver.find_element_by_xpath(self.City_by_xpath).send_keys(city)
    #
    # def ASOTA(self):
    #     Asota =self.driver.find_element_by_xpath(self.AsotaIT_by_xpath)
    #     Asota.sendKeys(Keys.DOWN)
    #     Asota.sendKeys(Keys.RETURN)
    #
    #
    # def ZipCode(self, Zip):
    #     self.driver.find_element_by_xpath(self.ZipCode_by_path).clear()
    #     self.driver.find_element_by_xpath(self.ZipCode_by_path).send_keys(Zip)
    #
    # def Americansomoa(self):
    #     America = self.driver.find_element_by_xpath(self.AmericanSomoa_by_xpath)
    #     America.sendKeys(Keys.DOWN)
    #     America.sendKeys(Keys.RETURN)
    #
    # def TaxID(self, TaxID):
    #     self.driver.find_element_by_xpath(self.TaxID_by_xpath).clear()
    #     self.driver.find_element_by_xpath(self.TaxID_by_xpath).send_keys(TaxID)
    #
    # def Job_Position(self, Job):
    #     self.driver.find_element_by_xpath(self.JobPosition_by_xpath).clear()
    #     self.driver.find_element_by_xpath(self.JobPosition_by_xpath).send_keys(Job)
    #
    # def PhoneField(self, Phone):
    #     self.driver.find_element_by_xpath(self.phoneField_by_xpath).clear()
    #     self.driver.find_element_by_xpath(self.phoneField_by_xpath).send_keys(Phone)
    #
    # def MobileField(self, Mobile):
    #     self.driver.find_element_by_xpath(self.MobileField_by_xpath).clear()
    #     self.driver.find_element_by_xpath(self.MobileField_by_xpath).send_keys(Mobile)
    #
    # def EmailField(self, email):
    #     self.driver.find_element_by_xpath(self.emailField_by_xpath).clear()
    #     self.driver.find_element_by_xpath(self.emailField_by_xpath).send_keys(email)
    #
    # def Title(self):
    #     Title = self.driver.find_element_by_xpath(self.Title_by_xpath)
    #     Title.sendKeys(Keys.DOWN)
    #     Title.sendKeys(Keys.RETURN)
    #
    # def Tags(self, tag):
    #     Tag = self.driver.find_element_by_xpath(self.Tags_by_xpath).send_keys(tag)
    #     Tag.sendKeys(Keys.DOWN)
    #     Tag.sendKeys(Keys.RETURN)
    #
    # def click_AddImage(self, image):
    #     self.driver.find_element_by_xpath(self.AddImage_by_xpath).send_Keys(image)
    #
    # def click_Add(self):
    #     self.driver.find_element_by_xpath(self.AddButton_by_xpath).click()
