from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver(): 
    yield driver
    sleep(2)

def test_calculator(driver):
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    delay_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#delay')))
    delay_input.clear()
    delay_input.send_keys('45')

    seven = driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='7']")
    seven.click()
    sleep(1)
    plus = driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='+']")
    plus.click()
    sleep(1)
    eight = driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='8']")
    eight.click()
    sleep(1)
    equally = driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='=']")
    equally.click()
    sleep(1)
    WebDriverWait(driver, 45).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div[class='screen']"), "15"))

    result = driver.find_element(By.CSS_SELECTOR, "div.screen").text
    assert result == "15"
    sleep(1)
    

