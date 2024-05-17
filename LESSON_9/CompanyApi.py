import requests
import pytest
#класс по работе с api
class CompanyApi:

    def __init__(self, url):
        self.url = url

    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(f"{self.url}/auth/login", json=creds)
        return resp.json()["userToken"]

    def create_company(self, name, description=''):
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(f"{self.url}/company", json=company, headers=my_headers)
        return resp.json()

    #def get_company_list(self, id):
        #my_params = {
            #"company": id
        #}
        #resp = requests.get(f"{self.url}/employee", params=my_params)
        #return resp.json()

    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()
    
    def get_employee_by_id(self, id_employee: int):
        resp = requests.get(f"{self.url}/employee/{id_employee}")
        return resp.json()

    def add_new_employee(self, new_id: int, first_name: str, last_name: str, phone: int):
        employee = {
            "id": 1,
            "firstName": first_name,
            "lastName": last_name,
            "middleName": "-",
            "companyId": new_id,
            "email": "test@test.ru",
            "url": "string",
            "phone": phone,
            "birthdate": "2023-12-25T18:54:13.783Z",
            "isActive": 'true'
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(f"{self.url}/employee", headers=my_headers, json=employee)
        return resp.json()

    def update_employee_info(self, id_employee: int, last_name: str, email: str):
        user_info = {
            "lastName": last_name,
            "email": email,
            "isActive": True
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(f"{self.url}/employee/{id_employee}", headers=my_headers, json=user_info)
        return resp.json()