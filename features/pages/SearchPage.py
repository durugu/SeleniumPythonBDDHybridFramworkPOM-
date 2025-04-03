from features.pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_product_link_text = "HP LP3065"
    message_xpath = "//p[contains(text(),'There is no product that matches the search criter')]"

    def display_status_of_valid_product(self):
        return self.display_status("valid_product_link_text",self.valid_product_link_text)

    def display_status_of_message(self, expected_message_text):
        return self.retrieved_element_text_equals("message_xpath", self.message_xpath, expected_message_text)
