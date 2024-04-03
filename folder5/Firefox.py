# для Firefox
#Задача №1

from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


import os
from selenium import webdriver

geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

sleep(10)

# Пять раз кликните на кнопку "Add Element"
for i in range(5):
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()



# Соберите со страницы список кнопок "Delete"
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

print(len(delete_buttons))

#Задача №2
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

import os
from selenium import webdriver

geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()

# driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
#Откройте страницу http://uitestingplayground.com/dynamicid
driver.get("http://uitestingplayground.com/dynamicid")

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

for i in range(3):
    blue_button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
    blue_button.click()

sleep(10)

driver.quit()

#Задача №3
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

import os
from selenium import webdriver

geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()

#Откройте страницу 
driver.get("http://uitestingplayground.com/classattr")

blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()

ok_button = driver.find_element(By.ID, "modalOkButton")
ok_button.click()

for _ in range(3):
    blue_button.click()
    ok_button.click()
    
    sleep(10)

driver.quit()

#Задача №4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


import os
from selenium import webdriver

geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(10)

try:
    # Ожидание появления модального окна
    modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "modal")))
    
    # Нахождение кнопки Close и клик по ней
    close_button = modal.find_element(By.CSS_SELECTOR, ".modal-footer p") 
    close_button.click()
    
finally:
    driver.quit()

#Задача №5
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService


import os
from selenium import webdriver

geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Введите в поле текст 1000.
input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
input_element.send_keys("1000")

# Очистите это поле (метод clear).
input_element.clear()

# Введите в это же поле текст 999.
input_element.send_keys("999")

driver.quit()

#Задача №6
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService


import os
from selenium import webdriver

geckodriver_path = "C:\\webdriver_firefox\\geckodriver\\geckodriver.exe"
os.environ["webdriver.gecko.driver"] = geckodriver_path

driver = webdriver.Firefox()

# Откройте страницу
driver.get("http://the-internet.herokuapp.com/login")

# Находим поля для ввода имени пользователя и пароля
usernamefield = driver.find_elements(By.CSS_SELECTOR, "username")
passwordfield = driver.find_elements(By.CSS_SELECTOR, "password")

# Вводим данные пользователя

usernamefield.send_keys("tomsmith")
passwordfield.send_keys("SuperSecretPassword!")

# Нажимаем кнопку Login
loginbutton = driver.find_elements(By.CSS_SELECTOR, "button")
loginbutton.click()