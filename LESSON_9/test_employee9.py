import pytest
import requests
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable
from faker import Faker

fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
phone = fake.phone_number()
company = fake.company()
description = fake.domain_name()


api = CompanyApi("https://x-clients-be.onrender.com")
db = CompanyTable("postgres://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")
#db = CompanyTable("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")
#Получение списка компаний через api и БД, сравнение их
def test_get_companies():
    api_result = api.get_company_list()
    db_result = db.get_companies()
    assert len(api_result) == len(db_result)
    
#Создание нового сотрудника в новой компании и получение списка сотрудников для компании
def test_get_list_employees():
    name = "SkyPro"
    descr = "testing"
    company = db.create(name, descr)
    new_id = company["id"]
    first_name = "Ivan"
    last_name = "Testov"
    phone = "+79050666598"
    db.create_employee(new_id, first_name, last_name, phone)
    employee_id = db.get_max_id()
    get_info = api.get_company_list(new_id)#получение списка сотрудников для компании
    db.delete_employee(employee_id)
    db.delete_company(new_id)

    assert get_info["id"] == employee_id
    assert get_info[0]["employeeId"] == employee_id
    assert get_info[0]["firstName"] == first_name
    assert get_info[0]["isActive"] == True
    assert get_info[0]["lastName"] == last_name
    assert get_info[0]["phone"] == phone

#Добавление нового сотрудника в новую компанию
def test_add_new_employee():
    name = "SkyPro"
    descr = "testing"
    company = db.create(name, descr)
    new_id = company["id"]
    first_name = "Ivan"
    last_name = "Testov"
    phone = "+79050666598"
    api.add_new_employee(new_id, first_name, last_name, phone)#создание сотрудника
    employee_id = db.get_max_id()
    get_info = api.get_employee_by_id(employee_id) 
    db.delete_employee(employee_id)
    db.delete_company(new_id)

    assert get_info["id"] == employee_id
    assert get_info[0]["employeeId"] == employee_id
    assert get_info[0]["firstName"] == first_name
    assert get_info[0]["isActive"] == True
    assert get_info[0]["lastName"] == last_name
    assert get_info[0]["phone"] == phone

#Получение созданного сотрудника по id
def test_get_new_employee_by_id():
    name = "SkyPro"
    descr = "testing"
    company = db.create(name, descr)
    new_id = company["id"]
    first_name = "Ivan"
    last_name = "Testov"
    phone = "+79050666598"
    db.create_employee(new_id, first_name, last_name, phone)
    employee_id = db.get_max_id()
    get_info = api.get_employee_by_id(employee_id)# получение сотрудника по id 
    db.delete_employee(employee_id)
    db.delete_company(new_id)

    assert get_info["id"] == employee_id
    assert get_info[0]["employeeId"] == employee_id
    assert get_info[0]["firstName"] == first_name
    assert get_info[0]["isActive"] == True
    assert get_info[0]["lastName"] == last_name
    assert get_info[0]["phone"] == phone

def test_edit():
    name = "SkyPro"
    description = "Descr"
    db.create(name, description)
    max_id = db.get_max_id
    first_name = "Ivan"
    last_name = "Testov"
    phone = "+79050666598"
    db.create_employee(first_name, last_name, phone, max_id)
    employee_id = db.get_max_id()
    new_name = "Updated"
    new_descr = "_upd_"
    edited = api.update_employee_info(max_id, new_name, new_descr)
    db.delete_employee(employee_id)
    db.delete_company(max_id)
    
    assert edited["id"] == employee_id
    assert edited["name"] == new_name
    assert edited["description"] == new_descr
    assert edited["isActive"] == True