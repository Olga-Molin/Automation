import requests
import pytest

from test_employee_Api import EmployeeApi

url = "https://x-clients-be.onrender.com"
api = EmployeeApi(url)

def test_create_new_employee():
    user = 'raphael'
    password = 'cool-but-crude'
    api.get_token(user, password)
    name = "Имя"
    description = "Описание"
    company_id = api.create_new_company(name, description)
    employee_before = api.get_employee(company_id)
    new_employee = api.add_employee(
        id="1012",
        first_name="Olga",
        last_name="Molyn",
        middle_name="Nikolaevna",
        company_id=company_id,
        mail="molynOlga@mail.com",
        employee_url="https://example.com",
        phone="89036588479",
        birthdate="1985-05-01T11:16:23.575Z",
        is_active=True
)
    employee_after = api.get_employee(company_id)
    assert len(employee_before) < len(employee_after)
    assert employee_after[-1]["id"] == new_employee["id"]
    assert employee_after[-1]["firstName"] == 'Olga'
    assert employee_after[-1]["lastName"] == 'Molyn'
    assert employee_after[-1]["middleName"] == 'Nikolaevna'
    assert employee_after[-1]["companyId"] == company_id
    assert employee_after[-1]["email"] == "molynOlga@mail.com"
    assert employee_after[-1]["avatar_url"] == "https://example.com"
    assert employee_after[-1]["phone"] == "89036588479"
    assert employee_after[-1]["birthdate"] == "1985-05-01"
    assert employee_after[-1]["isActive"] == True

def test_get_employee_id():
    user = 'musa'
    password = 'music-fairy'
    api.get_token(user, password)
    name = "ООО Мечта"
    description = "Любой каприз за ваши деньги"
    company_id = api.create_new_company(name, description)
    returned_id = api.add_employee(
        id="1313",
        first_name="Sima",
        last_name="Martyshkina",
        middle_name="Petrovna",
        company_id=company_id,
        mail="martyshka@mail.com",
        employee_url="https://zoo.com",
        phone="89050255698",
        birthdate="1988-08-08T11:16:23.575Z",
        is_active=True
)
    employee_id = api.get_employee_id(returned_id)
    assert employee_id["id"] == returned_id["id"]
    assert employee_id["firstName"] == "Sima"
    assert employee_id["lastName"] == "Martyshkina"
    assert employee_id["middleName"] == "Petrovna"
    assert employee_id["companyId"] == company_id
    assert employee_id["email"] == "martyshka@mail.com"
    assert employee_id["phone"] == "89050255698"
    assert employee_id["birthdate"] == "1988-08-08"
    assert employee_id["isActive"] == True

def test_update_employee():
    user =  'stella'
    password = 'sun-fairy'
    api.get_token(user, password)
    name = "Ромалы"
    description = "Гадаю недорого карты-таро"
    company_id = api.create_new_company(name, description)
    employee = api.add_employee(
        id="6699",
        first_name="Roza",
        last_name="Badoni",
        middle_name="Abramovna",
        company_id=company_id,
        mail="GypsiesRussia@mail.ru",
        employee_url="https://Gypsies of Russia.com",
        phone="89062544759",
        birthdate="1992-11-11T11:16:23.575Z",
        is_active=True
)
    api.change_employee(
        id=employee,
        change_lastName="Govani",
        change_email="GypsiesArmenia@mail.am",
        change_url="https://Gypsies of Armenia.com",
        change_phone="83745658955",
        change_active=False
)
    id_update_employee = api.get_employee_id(employee)
    assert id_update_employee["isActive"] == False
    assert id_update_employee["email"] == "GypsiesArmenia@mail.am"
    assert id_update_employee["avatar_url"] == "https://Gypsies of Armenia.com" 

    