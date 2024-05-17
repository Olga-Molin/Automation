import pytest
import requests
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable
from faker import Faker

fake = Faker("ru_Ru")
first_name = fake.first_name()
last_name = fake.last_name()
phone = fake.phone_number()
name = fake.company()
description = fake.domain_name()

api = CompanyApi("https://x-clients-be.onrender.com")
db = CompanyTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

#Получение списка компаний через api и БД, сравнение их
def test_get_companies():
    api_result = api.get_company_list()
    db_result = db.get_companies()
    assert len(api_result) == len(db_result)
    
#Создание нового сотрудника в новой компании и получение списка сотрудников для компании
def test_get_list_employees():
    db.create(name, description)
    new_id = db.get_max_id_company()
    db.create_employee(new_id, first_name, last_name, phone)
    employee_id = db.get_max_id_emp()
    get_info = api.get_company_list(str(new_id))
    db.delete_employee(employee_id)
    db.delete_company(new_id)

    assert get_info[-1]["id"] == new_id
    for employee in get_info:
        if employee["id"] == employee_id:
            assert employee[-1]["employeeId"] == employee_id
            assert employee["firstName"] == first_name
            assert employee["isActive"] == True
            assert employee["lastName"] == last_name
            assert employee["phone"] == phone

#Добавление нового сотрудника в новую компанию
def test_add_new_employee():
    db.create(name, description)
    new_id = db.get_max_id_company()
    api.add_new_employee(new_id, first_name, last_name, phone)
    employee_id = db.get_max_id_emp()
    get_info = api.get_company_list(str(new_id))
    db.delete_employee(employee_id)
    db.delete_company(new_id)
    
    assert get_info[-1]["id"] == new_id
    for employee in get_info:
        if employee["id"] == employee_id:
            assert employee[-1]["employeeId"] == employee_id
            assert employee["firstName"] == first_name
            assert employee["isActive"] == True
            assert employee["lastName"] == last_name
            assert employee["phone"] == phone

#Получение созданного сотрудника по id
def test_get_new_employee_by_id():
    db.create(name, description)
    new_id = db.get_max_id_company()
    db.create_employee(new_id, first_name, last_name, phone)
    employee_id = db.get_max_id_emp()
    get_info = api.get_employee_by_id(str(employee_id))# получение сотрудника по id 
    db.delete_employee(employee_id)
    db.delete_company(new_id)
    
    assert get_info["id"] == employee_id
    for employee in get_info:
        if employee[1] == employee_id:
            assert employee[1]["employeeId"] == employee_id
            assert employee["firstName"] == first_name
            assert employee["isActive"] == True
            assert employee["lastName"] == last_name
            assert employee["phone"] == phone

#Изменение информации о сотруднике
def test_edit():
    db.create(name, description)
    new_id = db.get_max_id_company()
    db.create_employee(new_id, first_name, last_name, phone)
    employee_id = db.get_max_id_emp()
    new_name = "Last test"
    new_descr = "_upd_"
    edited = api.update_employee_info(new_id, new_name, new_descr)
    db.delete_employee(employee_id)
    db.delete_company(new_id)

    assert edited["id"] == new_id
    for employee in edited:
        if employee["id"] == employee_id:
            assert employee[0]["employeeId"] == employee_id
            assert employee["firstName"] == first_name
            assert employee["isActive"] == True
            assert employee["lastName"] == last_name
            assert employee["phone"] == phone

    #assert edited["id"] == new_id
    #assert edited["name"] == new_name
    #assert edited["description"] == new_descr
    #assert edited["isActive"] == True