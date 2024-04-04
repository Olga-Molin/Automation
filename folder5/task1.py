# для Chrome
#Задача №1
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

#Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(1)

#Пять раз кликните на кнопку Add Element
for x in range(5):
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    add_button.click()

#Соберите со страницы список кнопок Delete
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

print(len(delete_buttons))

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

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

sleep(1)

# Пять раз кликните на кнопку "Add Element"
for i in range(5):
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()

# Соберите со страницы список кнопок "Delete"
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

# Выведите на экран размер списка
print(len(delete_buttons))
