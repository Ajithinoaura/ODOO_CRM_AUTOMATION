class Login:
    Email_textbox_id = "login"
    password_textbox_id = "password"
    Login_button_xpath = "//button[contains(text(),'Log in')]"
    navigate_dashboard_xpath = "//i[@class='fa fa-th-large']"
    click_crm_xpath = "//a[contains(text(),'CRM')]"
    User_icon_xpath = "//img[@alt='User']"
    logout_button_linkText = "Log out"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_id(self.Email_textbox_id).clear()
        self.driver.find_element_by_id(self.Email_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def login_button_press(self):
        self.driver.find_element_by_xpath(self.Login_button_xpath).click()

    def navigate_dashboard(self):
        self.driver.find_element_by_xpath(self.navigate_dashboard_xpath).click()

    def click_crm(self):
        self.driver.find_element_by_xpath(self.click_crm_xpath).click()

    def find_userIcon(self):
        self.driver.find_element_by_xpath(self.User_icon_xpath).click()

    def logout_fromOdoo(self):
        self.driver.find_element_by_link_text(self.logout_button_linkText).click()
