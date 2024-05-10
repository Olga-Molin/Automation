import requests
import pytest
from sqlalchemy import create_engine
from sqlalchemy.sql import text
#класс по работе с БД
class CompanyTable:
    __scripts = {
        "select": text("select * from employee where deleted_at is Null"),
        "insert new": text("insert into company(\"name\", \"description\") values (:new_name, :new_descr)"),
        "get max id": text("select MAX(\"id\") from employee"),
        "select by id": text("select * from employee where id =:select_id"),
        "delete by id": text("delete from employee where id =:id_to_delete"),
        "insert new employee": text("insert into employee(\"company_id\", \"first_name\", \"last_name\", \"phone\") values (:new_id, :nfirst_name, :nlast_name, :phone)")
        }


    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_companies(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()
    
    def create(self, name, description):
        self.__db.execute(self.__scripts["insert new"], new_name = name, new_descr = description)
    
    def get_max_id(self):
        return self.__db.execute(self.__scripts["get max id"]).fetchall()[0]

    def get_company_by_id(self, id):
        return self.__db.execute(self.__scripts["select by id"], select_id = id).fetchAll()

    def create_employee(self, company_id, first_name, last_name, phone):
        self.__db.execute(self.__scripts["insert new employee"], new_id = company_id, nfirst_name = first_name, nlast_name = last_name, nphone = phone)

    def delete(self, id):
        self.__db.execute(self.__scripts ["delete by id"], id_to_delete = id)