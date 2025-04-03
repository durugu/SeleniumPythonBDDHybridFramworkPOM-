from features.pages.AccountSuccessPage import AccountSuccessPage
from features.pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    privacy_policy_option_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_button_xpath = "//input[@value='1'][@name='newsletter']"
    duplicate_email_warning_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    privacy_policy_warning_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    first_name_warning_xpath = "//div[contains(text(),'First Name must be between 1 and 32 characters!')]"
    last_name_warning_xpath = "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]"
    email_warning_xpath = "//div[contains(text(),'E-Mail Address does not appear to be valid!')]"
    telephone_warning_xpath = "//div[contains(text(),'Telephone must be between 3 and 32 characters!')]"
    password_warning_xpath = "//div[contains(text(),'Password must be between 4 and 20 characters!')]"

    def enter_first_name(self, first_name_text):
        self.type_into_elements("first_name_field_id", self.first_name_field_id, first_name_text)

    def enter_last_name(self, last_name_text):
        self.type_into_elements("last_name_field_id", self.last_name_field_id, last_name_text)

    def enter_email(self, email_text):
        self.type_into_elements("email_field_id", self.email_field_id, email_text)

    def enter_telephone(self, telephone_text):
        self.type_into_elements("telephone_field_id", self.telephone_field_id, telephone_text)

    def enter_password(self, password_text):
        self.type_into_elements("password_field_id", self.password_field_id, password_text)

    def enter_password_confirm(self, password_confirm_text):
        self.type_into_elements("confirm_password_field_id", self.confirm_password_field_id, password_confirm_text)

    def select_privacy_policy(self):
        self.click_on_element("privacy_policy_option_name", self.privacy_policy_option_name)

    def click_on_continue_button(self):
        self.click_on_element("continue_button_xpath", self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def select_yes_newsletter_option(self):
        self.click_on_element("yes_radio_button_xpath", self.yes_radio_button_xpath)

    def display_status_of_duplicate_email_warning(self, expected_warning_text):
        return self.retrieved_element_text_contains("duplicate_email_warning_xpath", self.duplicate_email_warning_xpath, expected_warning_text)

    def display_status_of_all_warning_messages(self,expected_privacy_warning,expected_first_name_warning,expected_last_name_warning,expected_email_warning,expected_telephone_warning,expected_password_warning):
        privacy_status = self.retrieved_element_text_contains("privacy_policy_warning_xpath", self.privacy_policy_warning_xpath, expected_privacy_warning)
        first_name_status = self.retrieved_element_text_equals("first_name_warning_xpath", self.first_name_warning_xpath, expected_first_name_warning)
        last_name_status = self.retrieved_element_text_equals("last_name_warning_xpath", self.last_name_warning_xpath, expected_last_name_warning)
        email_status = self.retrieved_element_text_equals("email_warning_xpath", self.email_warning_xpath, expected_email_warning)
        telephone_status = self.retrieved_element_text_equals("telephone_warning_xpath", self.telephone_warning_xpath, expected_telephone_warning)
        password_status = self.retrieved_element_text_equals("password_warning_xpath", self.password_warning_xpath, expected_password_warning)
        return self.return_and_status(privacy_status,first_name_status,last_name_status,email_status,telephone_status,password_status)
