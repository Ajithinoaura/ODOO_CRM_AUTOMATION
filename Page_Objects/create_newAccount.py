class NewAccountPage:
    doNotHaveAn_account_linkText = "Don't have an account?"
    newAccount_emailField_xpath = "//input[@id='login']"
    enter_yourName = "//input[@id='name']"
    newAccount_passwordField_xpath = "//input[@id='password']"
    newAccount_conformPasswordField_xpath = "//input[@id='confirm_password']"
    newAccount_sighUpButton_xpath = "//button[normalize-space()='Sign up']"

    def __init__(self, driver):
        self.driver = driver

    def create_newAccount(self):
        self.driver.find_element_by_link_text(self.doNotHaveAn_account_linkText).click()

    def newAccount_emailField(self, emailField):
        self.driver.find_element_by_xpath(self.newAccount_emailField_xpath).send_keys(emailField)

    def newAccount_userName(self, name):
        self.driver.find_element_by_xpath(self.enter_yourName).send_keys(name)

    def newAccount_passwordField(self, password):
        self.driver.find_element_by_xpath(self.newAccount_passwordField_xpath).send_keys(password)

    def newAccount_conformPasswordField(self, conformPassword):
        self.driver.find_element_by_xpath(self.newAccount_conformPasswordField_xpath).send_keys(conformPassword)

    def newAccount_signInButton(self):
        self.driver.find_element_by_xpath(self.enter_yourName).click()
