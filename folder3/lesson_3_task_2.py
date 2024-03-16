from smartphone import Smartphone
catalog = []


phone1 = Smartphone('Samsung', 'Galaxy S6', '+79213355533')
phone2 = Smartphone('LG', 'G4', '+79032555522')
phone3 = Smartphone('Apple', 'iPhone 6', '+79095555555')
phone4 = Smartphone('Google', 'Nexus 6', '+79056611133')
phone5 = Smartphone('HTC', 'One M9', '+79012222255')


catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f'{phone.brand_phone}  {phone.phone_model}  {phone.phone_number}')