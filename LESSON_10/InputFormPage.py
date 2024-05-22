import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import allure

@allure.epic("Интернет магазин")
@allure.severity("blocker")
class BasePage:
    @allure.title("Создание драйвера")
    @allure.feature("create")
    def __init__(self, driver):
        """Эта функция создает драйвер
           
        """
        with allure.step("Создание экземпляра драйвера"):
            self.driver = driver   
    
    @allure.title("Открытие и разворачивание страницы")
    @allure.feature("open")
    def open_url(self, url):
        """Эта функция открывает страницу по указанному адресу
           ожидает 4 секунды
           и разворачивает окно на весь экран
        """
        with allure.step("Драйвер используется для открытия URL страницы"):
            self.driver.get(url)
        with allure.step("Установка ожидания, драйвер будет ожидать загрузки элементов на странице 4 секунды"):
            self.driver.implicitly_wait(4)
        with allure.step("Драйвер максимизирует окно браузера"):
            self.driver.maximize_window()

class LoginPage(BasePage):
    """Эта функция вызывается при создании нового объекта класса
       принимает один аргумент `driver`
       и вызывает конструктор базового класса с помощью вызова `super().__init__(driver)`
    """
    @allure.title("Создание драйвера")
    @allure.feature("create")
    def __init__(self, driver):
        with allure.step("Создание экземпляра драйвера"):
            super().__init__(driver)

    @allure.title("Авторизация пользователя standard_user")
    @allure.description("Поиск элементов и заполнение их")
    @allure.feature("find")
    def login(self, username: str, password: str) -> None:
        """Эта функция ищет элементы на веб-странице, используя CSS-селектор
           вводит значения в найденные поля
           нажимает на найденную кнопку, чтобы выполнить вход в систему
        """
        with allure.step("Поиск элемента на странице по заданному селектору, ввод имени"):
            self.driver.find_element(By.CSS_SELECTOR, value="#user-name").send_keys(username)
        with allure.step("Поиск элемента на странице по заданному селектору, ввод пароля"):
            self.driver.find_element(By.CSS_SELECTOR, value="#password").send_keys(password)
        with allure.step("Поиск элемента на странице по заданному селектору, клик по найденной кнопке для авторизации"):
            self.driver.find_element(By.CSS_SELECTOR, value="#login-button").click()

class ShopPage(BasePage):
    """Эта функция вызывается при создании нового объекта класса
       принимает один аргумент `driver`
       и вызывает конструктор базового класса с помощью вызова `super().__init__(driver)`
    """
    @allure.title("Создание драйвера")
    @allure.feature("create")
    def __init__(self, driver):
        with allure.step("Создание экземпляра драйвера"):
            super().__init__(driver)

    @allure.feature("add")
    @allure.title("Товар в корзине")
    @allure.description("Добавление товара в корзину: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie")

    def add_items_to_cart(self):
        """Эта функция находит элемент на веб-странице, используя CSS-селектор
           кликает по элементу, добавляя товар в корзину
           находит элемент с CSS-селектором  и кликает по нему
           переходит в корзину для просмотра добавленных товаров 
        """
        with allure.step("Поиск элемента с CSS-селектором, добавление товара в корзину"):
            self.driver.find_element(By.CSS_SELECTOR, value='#add-to-cart-sauce-labs-backpack').click()
        with allure.step("Поиск элемента с CSS-селектором, добавление товара в корзину"):
            self.driver.find_element(By.CSS_SELECTOR, value='#add-to-cart-sauce-labs-bolt-t-shirt').click()
        with allure.step("Поиск элемента с CSS-селектором, добавление товара в корзину"):
            self.driver.find_element(By.CSS_SELECTOR, value='#add-to-cart-sauce-labs-onesie').click()
        with allure.step("Поиск элемента с CSS-селектором, переход в корзину, просмотр выбранного товара"):
            self.driver.find_element(By.CSS_SELECTOR, value='#shopping_cart_container').click()

class CheckoutPage(BasePage):
    """Эта функция вызывается при создании нового объекта класса
       принимает один аргумент `driver`
       и вызывает конструктор базового класса с помощью вызова `super().__init__(driver)`
    """
    @allure.title("Создание драйвера")
    @allure.feature("create")
    def __init__(self, driver):
        with allure.step("Создание экземпляра драйвера"):
            super().__init__(driver)

    @allure.feature("find")
    @allure.title("Поиск элементов для дальнейшего оформления заказа")
    @allure.description("Поиск полей и заполнение личными данными")
    def checkout(self, first_name: str, last_name: str, postal_code: int) -> None:
        """Эта функция находит элементы на странице по их CSS селекторам
           нажимает на кнопку "Продолжить" для перехода к оформлению заказа
        """
        with allure.step("Нажать на кнопку 'Checkout' на странице корзины товаров"):
            self.driver.find_element(By.CSS_SELECTOR, value='#checkout').click()
        with allure.step("Ввести имя в поле First Name"):
            self.driver.find_element(By.CSS_SELECTOR, value='#first-name').send_keys(first_name)
        with allure.step("Ввести фамилию в поле Last Name"):
            self.driver.find_element(By.CSS_SELECTOR, value='#last-name').send_keys(last_name)
        with allure.step("Ввести почтовый индекс в поле Postal Code"):
            self.driver.find_element(By.CSS_SELECTOR, value='#postal-code').send_keys(postal_code)
        with allure.step("Нажать на кнопку 'Continue' для перехода к следующему шагу оформления заказа"):
            self.driver.find_element(By.CSS_SELECTOR, value='#continue').click()

    
    @allure.feature("find")
    @allure.title("Оформление заказа")
    def checkout(self):
        """Эта функция находит элемент (кнопку)
           и кликает на кнопку "Оформить заказ"
        """
        with allure.step("Найти кнопку'Оформить заказ' и нажать ее"):
            self.driver.find_element(By.ID, "checkout").click()

    @allure.feature("read")
    @allure.title("Личные данные")
    @allure.description("Заполнение полей личными данными")
    def fill_checkout_info(self, first_name: str, last_name:str, postal_code: int) -> None:
        """Эта функция заполняет информацию для оформления заказа
           вводит имя, фамилию и почтовый код в соответствующие поля на странице оформления заказа
        """
        with allure.step("Поиск поля для ввода значения first_name"):
            self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        with allure.step("Поиск поля для ввода значения last_name"):
            self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        with allure.step("Поиск поля для ввода значения postal_code"):
            self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    @allure.feature("assert")
    @allure.title("Стоимость заказа")
    @allure.description("Проверка, что итоговая сумма равна $58.29")
    def get_total(self):
        """Эта функция возвращает текст, содержащий общую стоимость товаров в корзине
        """
        with allure.step("Поиск элемента, извлечение из него общую стоимость товара"):
            return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
