import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, value= "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_number(self, number):
        self.driver.find_element(
            By.XPATH, f"//div[@class='keys']/span[text()='{number}']").click()

    def click_operator(self, operator):
        self.driver.find_element(
            By.XPATH, f"//div[@class='keys']/span[text()='{operator}']").click()
        
    def assert_result(self, expected_result):
        WebDriverWait(self.driver, timeout=46).until(
            EC.text_to_be_present_in_element(locator=
                (By.CSS_SELECTOR, ".screen"), text_= expected_result)
            )
        assert self.driver.find_element(
            By.CSS_SELECTOR, value=".screen").text == expected_result    