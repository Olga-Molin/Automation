import requests
import pytest
from sqlalchemy import create_engine
from sqlalchemy.sql import text
#класс по работе с БД
class CompanyTable:
    __scripts = {
        "select": text("select * from employee where deleted_at is Null"),
        "insert new": text("insert into company(\"name\", \"description\") values (:new_name, :new_descr)"),
        "get max id employee": text("select MAX(\"id\") from employee"),
        "get max id company": text("select MAX(\"id\") from company"),
        "select by id": text("select * from employee where id =:select_id"),
        "delete employee": text("delete from employee where id =:id_to_delete"),
        "delete company":text("delete from company where id =:new_id"),
        "insert new employee": text("insert into employee(\"company_id\", \"first_name\", \"last_name\", \"phone\") values (:new_id, :first_name, :last_name, :phone)")
        }

    def __init__(self, db):
        self.__db = create_engine(db)

    def get_companies(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()
    
    def create(self, name, description):
        self.__db.execute(self.__scripts["insert new"], new_name = name, new_descr = description)

    def get_max_id_company(self):
        return self.__db.execute(self.__scripts["get max id company"]).fetchall()[0]    
    
    def get_max_id_emp(self):
        return self.__db.execute(self.__scripts["get max id employee"]).fetchall()[0]

    def get_company_by_id(self, id):
        return self.__db.execute(self.__scripts["select by id"], select_id = id).fetchAll()

    def create_employee(self, company_id, first_name, last_name, phone):
        self.__db.execute(self.__scripts["insert new employee"], new_id = company_id, first_name = first_name, last_name = last_name, phone = phone)

    def delete_employee(self, id):
        self.__db.execute(self.__scripts ["delete employee"], id_to_delete = id)

    def delete_company(self, id):
        self.__db.execute(self.__scripts ["delete company"], new_id = id)  