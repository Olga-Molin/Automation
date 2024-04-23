#class BasePage:
    #def init(self, driver):
        #self.driver = driver

    #def open_url(self, url):
        #self.driver.get(url)
        #self.driver.implicitly_wait(4)
        #self.driver.maximize_window()

#class LoginPage(BasePage):
    #def init(self, driver):
        #super().init(driver)

    #def login(self, username, password):
        #self.driver.find_element(By.CSS_SELECTOR, value="#user-name").send_keys(username)
        #self.driver.find_element(By.CSS_SELECTOR, value="#password").send_keys(password)
        #self.driver.find_element(By.CSS_SELECTOR, value="#login-button").click()

#class ShopPage(BasePage):
    #def init(self, driver):
        #super().init(driver)

    #def add_items_to_cart(self):
        #self.driver.find_element(By.CSS_SELECTOR, value='#add-to-cart-sauce-labs-backpack').click()
        #self.driver.find_element(By.CSS_SELECTOR, value='#add-to-cart-sauce-labs-bolt-t-shirt').click()
        #self.driver.find_element(By.CSS_SELECTOR, value='#add-to-cart-sauce-labs-onesie').click()
        #self.driver.find_element(By.CSS_SELECTOR, value='#shopping_cart_container').click()

#class CheckoutPage(BasePage):
    #def init(self, driver):
        #super().init(driver)

    #def checkout(self, first_name, last_name, postal_code):
        #self.driver.find_element(By.CSS_SELECTOR, value='#checkout').click()
        #self.driver.find_element(By.CSS_SELECTOR, value='#first-name').send_keys(first_name)
        #self.driver.find_element(By.CSS_SELECTOR, value='#last-name').send_keys(last_name)
        #self.driver.find_element(By.CSS_SELECTOR, value='#postal-code').send_keys(postal_code)
        #self.driver.find_element(By.CSS_SELECTOR, value='#continue').click()
        
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, value='#user-name').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, value='#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, value='#login-button').click()

class ShopPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_items_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, value='#add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.CSS_SELECTOR, value='#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.CSS_SELECTOR, value='#add-to-cart-sauce-labs-onesie').click()
        self.driver.find_element(By.CSS_SELECTOR, value='#shopping_cart_container').click()

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def checkout(self, first_name, last_name, postal_code):
        self.driver.find_element(By.CSS_SELECTOR, value='#checkout').click()
        self.driver.find_element(By.CSS_SELECTOR, value='#first-name').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, value='#last-name').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, value='#postal-code').send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR, value='#continue').click()        

   
   
   
   
   
   
   
   