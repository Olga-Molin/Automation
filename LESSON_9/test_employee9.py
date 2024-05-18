import pytest
import requests
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable
from faker import Faker

fake = Faker("ru_Ru")
first_name = fake.first_name()
last_name = fake.last_name()
name = fake.company()
#email = fake.email

api = CompanyApi("https://x-clients-be.onrender.com")
db = CompanyTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

#Получение списка компаний через api(get/employee) и БД, сравнение их
def test_get_companies():
    api_result = api.get_company_list()
    db_result = db.get_companies()
    assert len(api_result) == len(db_result)
    
#Создание нового сотрудника(post/employee) в новой компании и получение сотрудника по id (get/employee{id})
def test_get_list_employees():
    description = "dz9"
    db.create(name, description)
    new_id = db.get_max_id_company()
    phone = "+79020255654"
    db.create_employee(new_id, first_name, last_name, phone)
    employee_id = db.get_max_id_emp()
    new_employer = api.get_employee_by_id(employee_id)
    db.delete_employee(employee_id)
    db.delete_company(new_id)
    
    assert new_employer.get("firstName") == first_name
    assert new_employer.get("lastName") == last_name
    assert new_employer.get("phone") == phone

#Добавление нового сотрудника в новую компанию
def test_add_new_employee():
    description = "dz9"
    db.create(name, description)
    new_id = db.get_max_id_company()
    phone = "+79020255654"
    get_info = api.add_new_employee(new_id, first_name, last_name, phone)
    employee_id = db.get_max_id_emp()
    db.delete_employee(employee_id)
    db.delete_company(new_id)

    assert get_info.get("id") == employee_id
   
#Изменение информации 
def test_edit():
    description = "dz9"
    db.create(name, description)
    new_id = db.get_max_id_company()
    phone = "+79020255654"
    db.create_employee(new_id, first_name, last_name, phone)
    employee_id = db.get_max_id_emp()
    new_name = "Last test"
    description = "holidays"
    edited = api.update_employee_info(new_id, new_name, description)
    db.delete_employee(employee_id)
    db.delete_company(new_id)

    #assert edited.get("description") == "holidays"
    #assert edited.get("employee_id") == employee_id
    #assert edited.get("phone") == "+79020255654"
    #assert edited.get("new_name") == "Last test"
