import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.test_Three import LoginPage
from pages.test_Three import ShopPage
from pages.test_Three import CheckoutPage
from pages.test_Three import BasePage

def test_shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    login_page = LoginPage(driver)
    shop_page = ShopPage(driver)
    checkout_page = CheckoutPage(driver)
    
    login_page.open_url("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    shop_page.add_items_to_cart()
    checkout_page.checkout("Olga", "Molyn", "188680")

    txt = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label'))).text
    driver.quit()
    assert txt == "Total: $58.29"