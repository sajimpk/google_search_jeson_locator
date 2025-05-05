import json
from selenium.webdriver.common.by import By

with open("config/locators.json") as f:
    LOCATORS = json.load(f)

class GooglePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_search_text(self, text):
        locator_type, locator_value = LOCATORS["search_box"].split(":")
        self.driver.find_element(getattr(By, locator_type.upper()), locator_value).send_keys(text)

    def click_search(self):
        locator_type, locator_value = LOCATORS["search_button"].split(":")
        self.driver.find_element(getattr(By, locator_type.upper()), locator_value).submit()
