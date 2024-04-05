#Задача №3
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

#Откройте страницу http://uitestingplayground.com/classattr
driver.get("http://uitestingplayground.com/classattr")

#Кликните на синюю кнопку.
#Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково
for i in range(3):
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()
    sleep(1)
    driver.switch_to.alert.accept()
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

driver = webdriver.Firefox()

#Откройте страницу http://uitestingplayground.com/classattr
driver.get("http://uitestingplayground.com/classattr")
for i in range(3):
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()
    sleep(1)
    driver.switch_to.alert.accept()
driver.quit()


driver.quit()
