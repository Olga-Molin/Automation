from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest

class FormPage: 
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def fill_form(self, first_name, last_name, address, email, phone, city, country, job_position, company):
        self.driver.find_element(By.CSS_SELECTOR, value="input[name='first-name']").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, value="input[name='last-name']").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, value="input[name='address']").send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, value="input[name='e-mail']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, value="input[name='phone']").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, value="input[name='city']").send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, value="input[name='country']").send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, value="input[name='job-position']").send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, value="input[name='company']").send_keys(company)
        self.driver.find_element(By.CSS_SELECTOR, value="button").click()   

    def check_form_field_color(self, field_id):
        field_color = self.driver.find_element(By.CSS_SELECTOR, value=f"#{field_id}").value_of_css_property("background-color")
        return field_color
    
    