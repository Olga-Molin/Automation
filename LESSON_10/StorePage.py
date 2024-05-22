from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest
import allure

@allure.epic("Заполнение формы")
@allure.severity("blocker")
class StorePage:
    @allure.feature("create")
    @allure.title("Создание драйвера")
    def __init__(self, driver):
        """Эта функция создает драйвер
           открывает страницу по указанному адресу
           ожидает 4 секунды
           и разворачивает окно на весь экран
        """
        with allure.step("Создание экземпляра драйвера"):
            self.driver = driver
        with allure.step("Драйвер используется для открытия URL страницы"):
            self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        with allure.step("Установка ожидания, драйвер будет ожидать загрузки элементов на странице 4 секунды"):
            self.driver.implicitly_wait(4)
        with allure.step("Драйвер максимизирует окно браузера"):
            self.driver.maximize_window()

    @allure.feature("read")
    @allure.title("Заполнение")
    @allure.description("Форма заполняется входными значениями: имя, фамилия, адрес, эл.адрес, телефон, город, страна, должность, компания")
    def fill_form(self, first_name: str, last_name: str, address: str, email: str, phone: int, city: str, country: str, job_position: str, company: str) -> None:
        """Эта функция заполняет форму исходными значениями
        """
        with allure.step("Поиск и заполнение поля 'Имя'"):
            self.driver.find_element(By.CSS_SELECTOR, value="input[name='first-name']").send_keys(first_name)
        with allure.step("Поиск и заполнение поля 'Фамилия'"):
            self.driver.find_element(By.CSS_SELECTOR, value="input[name='last-name']").send_keys(last_name)
        with allure.step("Поиск и заполнение поля 'Адрес'"):
            self.driver.find_element(By.CSS_SELECTOR, value="input[name='address']").send_keys(address)
        with allure.step("Поиск и заполнение поля 'Email'"):
            self.driver.find_element(By.CSS_SELECTOR, value="input[name='e-mail']").send_keys(email)
        with allure.step("Поиск и заполнение поля 'Телефон'"):
            self.driver.find_element(By.CSS_SELECTOR, value="input[name='phone']").send_keys(phone)
        with allure.step("Поиск и заполнение поля 'Город'"):
            self.driver.find_element(By.CSS_SELECTOR, value="input[name='city']").send_keys(city)
        with allure.step("Поиск и заполнение поля 'Страна'"):
            self.driver.find_element(By.CSS_SELECTOR, value="input[name='country']").send_keys(country)
        with allure.step("Поиск и заполнение поля 'Должность'"):
            self.driver.find_element(By.CSS_SELECTOR, value="input[name='job-position']").send_keys(job_position)
        with allure.step("Поиск и заполнение поля 'Компания'"):
            self.driver.find_element(By.CSS_SELECTOR, value="input[name='company']").send_keys(company)
        with allure.step("Нажатие кнопки 'Отправить' или 'Продолжить'"):
            self.driver.find_element(By.CSS_SELECTOR, value="button")

    @allure.title("Поиск кнопки Submit")
    @allure.feature("find")
    @allure.description("Нажатие кнопки Submit")
    def submit_form(self):
        """Эта функция ищет и нажимает кнопку Submit
        """
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    @allure.feature("find")
    @allure.title("Поиск полей")
    @allure.description("Поле Zip code подсвечено красным, остальные зеленым")
    def check_form_field_color(self, field_id: int) -> str:
        """Эта функция ищет поля подсвеченные красным и зеленым цветом
        """
        with allure.step("Поиск кнопки submit и нажатие на нее"):
            field_color = self.driver.find_element(By.CSS_SELECTOR, value=f"#{field_id}").value_of_css_property("background-color")
        with allure.step("проверка корректности поиска и взаимодействия с кнопкой Submit"):
            return field_color
    
    