from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
wait = WebDriverWait(driver, 10)

username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#user-name")))
username_input.send_keys("standard_user")
sleep(1)
password_input = driver.find_element(By.CSS_SELECTOR, "#password")
password_input.send_keys("secret_sauce")
sleep(1)
login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
login_button.click()
sleep(1)

Sauce_Labs_Backpack = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
Sauce_Labs_Backpack.click()
sleep(1)

Sauce_Labs_Bolt_TShirt = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
Sauce_Labs_Bolt_TShirt.click()
sleep(1)

Sauce_Labs_Onesie = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
Sauce_Labs_Onesie.click()
sleep(1)
basket = driver.find_element(By.CSS_SELECTOR, "div[class='shopping_cart_container']")
basket.click()
sleep(1)
checkout= driver.find_element(By.CSS_SELECTOR, "#checkout")
checkout.click()
sleep(1)
first_n_input = driver.find_element(By.CSS_SELECTOR, "#first-name")
first_n_input.send_keys("Olga")
sleep(1)
last_n_input = driver.find_element(By.CSS_SELECTOR, "#last-name")
last_n_input.send_keys("Molyn")
sleep(1)
postal_code_input = driver.find_element(By.CSS_SELECTOR, "#postal-code")
postal_code_input.send_keys("188680")
sleep(1)
continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
continue_button.click()
total_price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
total_price_text = total_price.split('$')[1]  
driver.quit()

assert float(total_price_text.replace(',', '')) == 58.29
print(total_price_text)
