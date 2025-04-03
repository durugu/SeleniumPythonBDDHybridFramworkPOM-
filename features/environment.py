import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities import configreader


def before_scenario(context,driver):
    browser_name = configreader.read_configuration("basic info","browser")

    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name == "edge":
        context.driver = webdriver.Edge()
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.get(configreader.read_configuration("basic info","url"))

def after_scenario(context,driver):
    context.driver.quit()

def after_step(context,step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name="failed_screenshot", attachment_type=AttachmentType.PNG)
