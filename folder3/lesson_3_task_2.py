from smartphone import Smartphone
catalog = [
    Smartphone('Samsung', 'Galaxy S6', '+79213355533'),
    Smartphone('LG', 'G4', '+79032555522'),
    Smartphone('Apple', 'iPhone 6', '+79095555555'),
    Smartphone('Google', 'Nexus 6', '+79056611133'),
    Smartphone('HTC', 'One M9', '+79012222255')
]
for phone in catalog:
    print(f'{phone.brand_phone}  {phone.phone_model}  {phone.phone_number}')