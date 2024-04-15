import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@pytest.fixture
def driver():
    yield driver
    sleep(2)

def test_form_submission (driver):
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    first_n = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='first-name']")))
    first_n.send_keys('Иван')
    
    last_n = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='last-name']")))
    last_n.send_keys('Петров')

    address = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='address']")))
    address.send_keys('Ленина, 55-3')

    email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='e-mail']")))
    email.send_keys('test@skypro.com')

    phone_n = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='phone']")))
    phone_n.send_keys('+7985899998787')

    city = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='city']")))
    city.send_keys("Москва")

    country = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='country']")))
    country.send_keys("Россия")

    job_p = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='job-position']")))
    job_p.send_keys("QA")

    company = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='company']")))
    company.send_keys("SkyPro")

    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    button.click()

    zip_code_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '#zip-code')))

    assert zip_code_field.value_of_css_property('background-color') == 'rgba(248, 215, 218, 1)'
     
    fields = [first_n, last_n, address, email, phone_n, city, country, job_p, company]
    for field in fields:
        field_error = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ("div.alert.py-2.alert-success")))
)
    assert field_error.value_of_css_property('background-color') == 'rgba(209, 231, 221, 1)'
    driver.quit()
    