import pytest
import requests
from test_Em_Api9 import CompanyEm
from test_Em_Api import Company


api = Company("https://x-clients-be.onrender.com")
db = CompanyEm("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")

def test_get_companies():
    api_result = api.get_list_employee()
    db_result = db.get_companies()
    assert len(api_result) == len(db_result)

def test_add_new_company():
    body = api.get_list_employee()
    len_before = len(body)
    name = "SkyPro"
    descr = "testing"
    result = api.create_company(name, descr)
    new_id = result["id"]
    body = api.get_list_employee()
    len_after = len(body)
    
    resp = api.get_list_employee(new_id)
    assert resp[-1]["companyId"] == new_id
    assert resp[-1]["name"] == "SkyPro"
    assert resp[-1]["description"] == "testing"
    
def test_get_one_company():
    name = "SkyPro"
    descr = "testing"
    db.create(name, descr)
    max_id = db.get_max_id()

    new_company = api.get_employee_by_id(max_id)
    assert new_company["id"] == max_id
    assert new_company["name"] == name
    assert new_company["description"] == descr

def test_edit():
    name = "SkyPro"
    description = "Descr"
    db.create(name, description)
    max_id = db.get_max_id()
    new_name = "Updated"
    new_descr = "_upd_"
    edited = api.edit(max_id, new_name, new_descr)
    # Удаляем компанию:
    db.delete(max_id)
    assert edited["id"] == max_id
    assert edited["name"] == new_name
    assert edited["description"] == new_descr
    