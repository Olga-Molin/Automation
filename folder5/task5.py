#Задача №5

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Откройте страницу http://the-internet.herokuapp.com/inputs

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")
sleep(10)

# Введите в поле текст 1000.
input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
input_element.send_keys("1000")

# Очистите это поле (метод clear).
input_element.clear()

# Введите в это же поле текст 999.
input_element.send_keys("999")

driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait # этот модуль используется, чтобы дождаться загрузки окна 
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
import os
from selenium import webdriver

driver = webdriver.Firefox()
# Откройте страницу
driver.get("http://the-internet.herokuapp.com/inputs")
sleep(1)

# Введите в поле текст 1000.
input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
input_element.send_keys("1000")
sleep(1)

# Очистите это поле (метод clear).
input_element.clear()
sleep(1)

# Введите в это же поле текст 999.
input_element.send_keys("999")
sleep(1)

# Закройте браузер.
driver.quit()