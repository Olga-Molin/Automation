import pytest
import requests
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable


api = CompanyApi("https://x-clients-be.onrender.com")
db = CompanyTable("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")

def test_get_companies():
    api_result = api.get_company_list
    db_result = db.get_companies()
    assert len(api_result) == len(db_result)

def test_add_new_company():
    body = api.get_company_list()
    len_before = len(body)
    name = "SkyPro"
    descr = "testing"
    result = db.create(name, descr)
    new_id = result["id"]
    body = api.get_company_list()
    len_after = len(body)
    db.delete(new_id)
    
    assert len_after - len_before == 1
    for company in body:
        if company["id"] == new_id:
            assert body[-1]["companyId"] == new_id
            assert body[-1]["name"] == "SkyPro"
            assert body[-1]["description"] == "testing"
    
def test_get_one_company():
    name = "HW9"
    descr = "testing"
    db.create(name, descr)
    max_id = db.get_max_id()
    new_company = api.get_employee_by_id(max_id)
    db.delete(max_id)
    
    assert new_company["id"] == max_id
    assert new_company["name"] == name
    assert new_company["description"] == descr

#надо добавить в компанию нового сотрудника и получить его id
def test_add_new_employee():
    name = "SkyPro"
    descr = "testing"
    company = db.create(name, descr)
    new_id = company["id"]
    first_name = "Ivan"
    last_name = "Testov"
    phone = "+79050666598"
    db.create_employee(first_name, last_name, phone, new_id)
    employee_id = db.get_max_id()
    get_info = api.get_employee_by_id(employee_id)
    db.delete(employee_id)
    db.delete(new_id)

    assert get_info["id"] > 0
    resp = api.get_company_list(new_id)
    assert resp[0]["employeeId"] == employee_id
    assert resp[0]["firstName"] == first_name
    assert resp[0]["isActive"] == True
    assert resp[0]["lastName"] == last_name
    assert resp[0]["phone"] == phone

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
    #get_info = api.get_employee_by_id(employee_id)
    new_name = "Updated"
    new_descr = "_upd_"
    edited = db.create_employee(max_id, new_name, new_descr)
    db.delete(employee_id)
    db.delete(max_id)

    api.update_employee_info(max_id, new_name, new_descr)
    assert edited["id"] == max_id
    assert edited["name"] == new_name
    assert edited["description"] == new_descr
    assert edited["isActive"] == True