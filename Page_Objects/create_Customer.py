# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
import time


class Create_Customer:
    Sales_Button_by_xpath = "//a[normalize-space()='Sales']"
    Click_customer_button_by_xpath = "//span[normalize-space()='Customers']"
    Click_Create_Button_by_xpath = "//button[contains(text(),'Create')]"
    # Select_office_By_xpath = "//input[@class='o_input'][@type='text'][@placeholder='Name']"
    Customer_Name_by_xpath = "//input[@class='o_input'][@type='text'][@placeholder='Name']"
    Street_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/input[1]"
    City_by_name = "city"
    # State_by_xpath = "//div[contains(@name,'state_id')]"
    ZipCode_by_path = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/input[4]"
    AmericanSomoa_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[2]/div[1]/input[1]"
    TaxID_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[1]/tbody[1]/tr[3]/td[2]/div[1]/input[1]"
    JobPosition_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[2]/tbody[1]/tr[1]/td[2]/input[1]"
    phoneField_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[2]/tbody[1]/tr[4]/td[2]/div[1]/input[1]"
    MobileField_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[2]/tbody[1]/tr[7]/td[2]/div[1]/input[1]"
    emailField_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[2]/tbody[1]/tr[11]/td[2]/div[1]/input[1]"
    WebsiteField_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[2]/tbody[1]/tr[12]/td[2]/input[1]"
    # Title_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[2]/tbody[1]/tr[13]/td[2]/div[1]/div[1]/input[1]"
    # Tags_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[2]/tbody[1]/tr[16]/td[2]/div[1]"
    # AddImage_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]"
    AddButton_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[6]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]"
    Save_Button_by_xpath = "//span[normalize-space()='Save & Close']"

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

    def Street(self, street):
        self.driver.find_element_by_xpath(self.Street_by_xpath).clear()
        self.driver.find_element_by_xpath(self.Street_by_xpath).send_keys(street)

    def City(self, city):
        self.driver.find_element_by_name(self.City_by_name).send_keys(city)

    # def State(self, state):
    #     dropArrow = self.driver.find_element_by_xpath(self.State_by_xpath)
    #     dropArrow.send_keys(state)
    #     if "tamilnadu (PE)" in dropArrow.text:
    #         dropArrow.click()
    #     time.sleep(2)
    # state.submit()
    # obj = self.driver.switch_to.alert
    # obj.accept()
    # txt = self.driver.find_element_by_xpath("//h4[normalize-space()='Create: State']")
    # print(txt.text)
    # time.sleep(5)
    # box1 = self.driver.find_element_by_name('code').send_keys("015")
    # button = self.driver.find_element_by_xpath("//span[normalize-space()='Save']")
    # button.click()

    def ZipCode(self, Zip):
        self.driver.find_element_by_xpath(self.ZipCode_by_path).clear()
        self.driver.find_element_by_xpath(self.ZipCode_by_path).send_keys(Zip)

    def Americansomoa(self, country):
        dropArrow = self.driver.find_element_by_xpath(self.AmericanSomoa_by_xpath)
        dropArrow.send_keys(country)
        # dropArrow.submit()
        # if "Afghanistan" in dropArrow.text:
        #     dropArrow.submit()
        # dropdown1 = self.driver.find_element_by_xpath("//td[contains(text(),'American Samoa')]")
        # dropdown1.click()
        # el = self.driver.find_element_by_xpath("//div[contains(@name,'country_id')]")
        # for option in el.find_elements_by_xpath("//td[contains(text(),'Afghanistan')]"):
        #     time.sleep(1)
        #     if "Afghanistan" in option.text:
        #         option.click()
        #         time.sleep(1)  # select() in earlier versions of webdriver
        #         break

    def TaxID(self, TaxID):
        self.driver.find_element_by_xpath(self.TaxID_by_xpath).clear()
        self.driver.find_element_by_xpath(self.TaxID_by_xpath).send_keys(TaxID)

    def Job_Position(self, Job):
        self.driver.find_element_by_xpath(self.JobPosition_by_xpath).clear()
        self.driver.find_element_by_xpath(self.JobPosition_by_xpath).send_keys(Job)

    def PhoneField(self, Phone):
        self.driver.find_element_by_xpath(self.phoneField_by_xpath).clear()
        self.driver.find_element_by_xpath(self.phoneField_by_xpath).send_keys(Phone)

    def MobileField(self, Mobile):
        self.driver.find_element_by_xpath(self.MobileField_by_xpath).clear()
        self.driver.find_element_by_xpath(self.MobileField_by_xpath).send_keys(Mobile)

    def EmailField(self, email):
        self.driver.find_element_by_xpath(self.emailField_by_xpath).clear()
        self.driver.find_element_by_xpath(self.emailField_by_xpath).send_keys(email)

    def Website(self, website):
        self.driver.find_element_by_xpath(self.WebsiteField_by_xpath).clear()
        self.driver.find_element_by_xpath(self.WebsiteField_by_xpath).send_keys(website)

    # def Title(self, title):
    #     dropArrow = self.driver.find_element_by_xpath(self.Title_by_xpath)
    #     dropArrow.send_keys(title)
    #     dropArrow.submit()
    #     time.sleep(3)
    #     dropdown1 = self.driver.find_element_by_xpath("//button[@class='btn btn-primary']")
    #     dropdown1.click()



        # selectItem = 'Doctor'
        # # First click on the All reviews element to open up the dorpdown element
        #     # Select item from menu dropdown by text
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/table[2]/tbody[1]/tr[13]/td[2]/div[1]/div[1]/input[1]" + selectItem + "']"))).click()

    # def Tags(self, tag):
    #     dropArrow = self.driver.find_element_by_xpath(self.Tags_by_xpath)
    #     dropArrow.send_keys(tag)
    #     dropArrow.submit()

    # def click_AddImage(self):
    #     add_image = self.driver.find_element_by_xpath(self.AddImage_by_xpath)
    #     add_image.click()
    #     time.sleep(5)
    #     add_image.send_Keys("C:/Users/SKYNETT DRONES/Pictures/Hero.jpg")
    #     add_image.submit()

    def click_Add(self):
        self.driver.find_element_by_xpath(self.AddButton_by_xpath).click()

    def save(self):
        self.driver.find_element_by_xpath(self.Save_Button_by_xpath).click()
