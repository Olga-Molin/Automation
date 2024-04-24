import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.test_Two import CalculatorPage

@pytest.mark.parametrize('number1, operator1, number2, operator2, result', [
    (int('7'), '+',int('8'), '=',int('15'))])

def test_slow_calculator(number1, number2, operator1, operator2, result):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calculator_page = CalculatorPage(driver)
    calculator_page.set_delay("3")
    calculator_page.click_number(number1)
    calculator_page.click_operator(operator1)
    calculator_page.click_number(number2)
    calculator_page.click_operator(operator2)
    calculator_page.assert_result ("15")
    driver.quit()