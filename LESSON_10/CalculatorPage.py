from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure

@allure.epic("Калькулятор")
@allure.severity("blocker")
class CalculatorPage:
    @allure.title("Создание драйвера")
    @allure.feature("create")
    def __init__(self, driver):
        """Эта функция создает двайвер
           открывает страницу по указанному адресу
           ожидает 4 секунды
           и разворачивает окно на весь экран
        """
        with allure.step("Создание экземпляра драйвера"):
            self.driver = driver
        with allure.step("Драйвер используется для открытия URL страницы"):
            self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        with allure.step("Установка ожидания, драйвер будет ожидать загрузки элементов на странице 4 секунды"):
            self.driver.implicitly_wait(4)
        with allure.step("Драйвер максимизирует окно браузера"):
            self.driver.maximize_window()

    @allure.feature("find")
    @allure.title("Отображение ответа через заданное время")
    def set_delay(self, delay: str) -> None:
        """Эта функция ищет элемент по локатору #delay
           очищает поле ввода
           заполняет поле данными
        """
        with allure.step("Использование метода с селектором CSS для поиска элемента с идентификатором #delay"):
            delay_input = self.driver.find_element(By.CSS_SELECTOR, value= "#delay")
        with allure.step("Очистка поля ввода"):
            delay_input.clear()
        with allure.step("Ввод нового значения"):
            delay_input.send_keys(delay)

    @allure.feature("find")
    @allure.title("Ввод числа")
    @allure.description("Числа 7 и 8")
    def click_number(self, number: str):
        """Эта функция ищет заданную кнопку (число)
           нажимает на нее
        """
        with allure.step("Нажатие на цифру в калькуляторе"):
            self.driver.find_element(
            By.XPATH, f"//div[@class='keys']/span[text()='{number}']").click()
        
    @allure.feature("find")
    @allure.title("Ввод символа")
    @allure.description("Символы + и =")
    def click_operator(self, operator: str) -> None:
        """Эта функция ищет заданную кнопку (символ)
           нажимает на нее
        """
        with allure.step("Нажатие на символ в калькуляторе"):
            self.driver.find_element(
            By.XPATH, f"//div[@class='keys']/span[text()='{operator}']").click()
        
    @allure.feature("assert")
    @allure.title("Проверка ожидаемого результата")
    @allure.description("поле ввода по локатору #delay введите значение 47")  
    def assert_result(self, expected_result: str) -> str:
        """Эта функция ожидает 47секунд, пока текст в элементе с CSS селектором `.screen` не станет равен `expected_result`
           После ожидания проверяется, действительно ли текст в элементе с CSS селектором `.screen` равен `expected_result`
           В целом, функция предназначена для проверки того, что на странице в элементе с указанным CSS селектором отображается ожидаемый текст
        """
        with allure.step("Задать ожидание"):
            WebDriverWait(self.driver, timeout=47).until(
            EC.text_to_be_present_in_element(
                locator=(By.CSS_SELECTOR, ".screen"), text_=expected_result)
            )
        with allure.step("Проверка соответствия текста в элементе равна ОР"):
            assert self.driver.find_element(
            By.CSS_SELECTOR, value=".screen").text == expected_result
        