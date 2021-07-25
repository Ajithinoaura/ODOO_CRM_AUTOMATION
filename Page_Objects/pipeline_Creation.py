class crm_PipelineCreation():
    # create the pipeline
    tap_create_button_by_xpath = "//button[contains(text(),'Create')]"
    # create_organisation_by_xpath = "//*[@class='o_input ui-autocomplete-input']"
    # create_button_press_by_xpath = "//span[normalize-space()='Create']"
    opportunity_by_xpath = "//*[@class='o_field_char o_field_widget o_input o_required_modifier']"
    lead_emailField_by_xpath = "//*[@name='email_from']"
    lead_phoneField_by_xpath = "//*[@name='phone']"
    lead_expectedRevenue_by_xpath = "//*[@class='o_input']"
    # self.lead_expectedRevenue_by_xpath = "//*[@class='o_input']"
    lead_addButton_by_xpath = "//body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]"

    # #     Edit the pipeline
    select_pipeline_by_path = "//*[@class='oe_kanban_color_0 oe_kanban_global_click o_kanban_record oe_kanban_card_danger']"
    # self.select_elipsis_by_xpath = "//a[@aria-expanded='false']//span[@class='fa fa-ellipsis-v']"
    Click_edit_by_xpath = "//*[@class='btn btn-primary o_form_button_edit']"
    Edit_opportunity_by_xpath = "//*[@name='name']"
    Edit_emailField_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[5]/table[2]/tbody[1]/tr[8]/td[2]/div[1]/input[1]"
    Edit_phoneField_by_xpath = "/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[5]/table[2]/tbody[1]/tr[9]/td[2]/div[1]/input[1]"
    add_description_by_xpath = "//*[@name='description']"
    click_save_by_xpath = "//*[@class='btn btn-primary o_form_button_save']"

    def __init__(self, driver):
        self.driver = driver

    def click_createButton(self):
        self.driver.find_element_by_xpath(self.tap_create_button_by_xpath).click()

    # def create_OrganisationFiled(self, opportunityName):
    #     self.driver.find_element_by_xpath(self.create_organisation_by_xpath).send_keys(opportunityName)
    #
    # def create_button(self):
    #     self.driver.find_element_by_xpath(self.create_button_press_by_xpath).click()

    def opportunity_field(self, opportunity):
        self.driver.find_element_by_xpath(self.opportunity_by_xpath).clear()
        self.driver.find_element_by_xpath(self.opportunity_by_xpath).send_keys(opportunity)

    def enter_emailField(self, email):
        self.driver.find_element_by_xpath(self.lead_emailField_by_xpath).clear()
        self.driver.find_element_by_xpath(self.lead_emailField_by_xpath).send_keys(email)

    def enter_phoneFiled(self, phone):
        self.driver.find_element_by_xpath(self.lead_phoneField_by_xpath).clear()
        self.driver.find_element_by_xpath(self.lead_phoneField_by_xpath).send_keys(phone)

    def enter_expectedRevenue_Field(self, revenue):
        self.driver.find_element_by_xpath(self.lead_expectedRevenue_by_xpath).clear()
        self.driver.find_element_by_xpath(self.lead_expectedRevenue_by_xpath).send_keys(revenue)

    def click_addButton(self):
        self.driver.find_element_by_xpath(self.lead_addButton_by_xpath).click()

    # Edit pipeline

    def Select_pipeline(self):
        self.driver.find_element_by_xpath(self.select_pipeline_by_path).click()

    # def Select_elipsis(self):
    #     self.driver.find_element_by_xpath(self.select_elipsis_by_xpath).click()

    def click_edit(self):
        self.driver.find_element_by_xpath(self.Click_edit_by_xpath).click()

    def Edit_opportunities(self, newOpportunity):
        self.driver.find_element_by_xpath(self.Edit_opportunity_by_xpath).clear()
        self.driver.find_element_by_xpath(self.Edit_opportunity_by_xpath).send_keys(newOpportunity)

    def Edit_Email_1(self, Email):
        self.driver.find_element_by_xpath(self.Edit_emailField_by_xpath).clear()
        self.driver.find_element_by_xpath(self.Edit_emailField_by_xpath).send_keys(Email)

    def Edit_phone_1(self, phone):
        self.driver.find_element_by_xpath(self.Edit_phoneField_by_xpath).clear()
        self.driver.find_element_by_xpath(self.Edit_phoneField_by_xpath).send_keys(phone)

    def Add_description(self, description):
        self.driver.find_element_by_xpath(self.add_description_by_xpath).clear()
        self.driver.find_element_by_xpath(self.add_description_by_xpath).send_keys(description)

    def click_save(self):
        self.driver.find_element_by_xpath(self.click_save_by_xpath).click()
