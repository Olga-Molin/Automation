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
sleep(10)

#Пять раз кликните на кнопку Add Element
for x in range(5):
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    add_button.click()

#Соберите со страницы список кнопок Delete
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

print(len(delete_buttons))


#Задача №2
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#Откройте страницу http://uitestingplayground.com/dynamicid
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")

for i in range(3):
    blue_button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
    blue_button.click()

sleep(10)

driver.quit()


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
    blue_button = driver.find_element(By.CLASS_NAME, "button.btn-primary")
    blue_button.click()

sleep(10)
driver.quit()


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

sleep(10)

try:
    # Ожидание появления модального окна
    modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "modal")))
    
    # Поиск кнопки Close и клик по ней
    close_button = modal.find_element(By.CSS_SELECTOR, ".modal-footer p")
    close_button.click()
    
finally:
    driver.quit()

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

#Задача №6
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Откройте страницу
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")

# Находим поля для ввода имени пользователя и пароля

usernamefield = driver.find_elements(By.CSS_SELECTOR, "username")
passwordfield = driver.find_elements(By.CSS_SELECTOR, "password")
usernamefield.send_keys(Keys.RETURN)
passwordfield.send_keys(Keys.RETURN)

sleep(10)


# Вводим данные пользователя

usernamefield.send_keys("tomsmith") 
passwordfield.send_keys("SuperSecretPassword!")

# Нажимаем кнопку Login
loginbutton = driver.find_elements(By.CSS_SELECTOR, "button")
loginbutton.click()


