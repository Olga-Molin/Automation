import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pagess.test_One import FormPage

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_form_elements():
    form_page = FormPage(driver)
    
    form_page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+79030655987", "Москва", "Россия", "QA", "SkyPro")
    zip_code_color = form_page.check_form_field_color("zip-code")
    assert zip_code_color == "rgba(248, 215, 218, 1)"
    other_fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field in other_fields:
        field_color = form_page.check_form_field_color(field)
        assert field_color == "rgba(209, 231, 221, 1)"
