#Задача №4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait # этот модуль используется, чтобы дождаться загрузки окна 
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(1)

try:
    # Ожидание появления модального окна
    modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "modal")))
    
    # Поиск кнопки Close и клик по ней
    close_button = modal.find_element(By.CSS_SELECTOR, ".modal-footer p")
    close_button.click()
    
finally:
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

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(1)

try:
    # Ожидание появления модального окна
    modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "modal")))
    
    # Нахождение кнопки Close и клик по ней
    close_button = modal.find_element(By.CSS_SELECTOR, ".modal-footer p") 
    close_button.click()
    
finally:
    driver.quit()