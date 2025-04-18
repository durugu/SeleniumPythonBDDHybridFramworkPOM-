from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage
from features.pages.RegisterPage import RegisterPage
from features.pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    my_account_option_xpath = "//span[normalize-space()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"
    search_box_field_name = "search"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"

    def click_on_my_account(self):
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)

    def select_login_option(self):
        self.click_on_element("login_option_link_text", self.login_option_link_text)
        return LoginPage(self.driver)

    def select_register_option(self):
        self.click_on_element("register_option_link_text", self.register_option_link_text)
        return RegisterPage(self.driver)

    def check_home_page_title(self, expected_title_text):
        return self.verify_page_title(expected_title_text)

    def enter_product_into_search_box_field(self, product_name):
        self.type_into_elements("search_box_field_name", self.search_box_field_name, product_name)

    def click_on_search_button(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)
