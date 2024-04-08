from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)

driver.get("https://uitestingplayground.com/textinput?")

element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.clear

element.send_keys("SkyPro")#Укажите в поле ввода текст SkyPro

button = driver.find_element(By.CSS_SELECTOR, 'button[id="updatingButton"]').click()#Нажмите на синюю кнопку
t = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]').text
print(t)#Получите текст кнопки и выведите в консоль (SkyPro)

driver.quit()
