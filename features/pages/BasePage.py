from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def click_on_element(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.click()

    def verify_page_title(self,expected_title):
        return self.driver.title.__eq__(expected_title)

    def type_into_elements(self, locator_type, locator_value, text_to_entered):
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text_to_entered)

    def get_element(self, locator_type, locator_value, timeout=13):
        wait = WebDriverWait(self.driver, timeout)

        if locator_type.endswith("_id"):
            return wait.until(EC.presence_of_element_located((By.ID, locator_value)))
        elif locator_type.endswith("_name"):
            return wait.until(EC.presence_of_element_located((By.NAME, locator_value)))
        elif locator_type.endswith("_classname"):
            return wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator_value)))
        elif locator_type.endswith("_link_text"):
            return wait.until(EC.presence_of_element_located((By.LINK_TEXT, locator_value)))
        elif locator_type.endswith("_xpath"):
            return wait.until(EC.presence_of_element_located((By.XPATH, locator_value)))
        elif locator_type.endswith("_css"):
            return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator_value)))
        return None

    def retrieved_element_text_contains(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__contains__(expected_text)

    def retrieved_element_text_equals(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__eq__(expected_text)

    def return_and_status(self,privacy_status,first_name_status,last_name_status,email_status,telephone_status,password_status):
        if privacy_status and first_name_status and last_name_status and email_status and telephone_status and password_status:
            return True
        else:
            return False

    def display_status(self,locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        return element.is_displayed()
    