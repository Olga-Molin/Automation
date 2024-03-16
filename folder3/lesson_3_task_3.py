from file_adress import Adress
from file_postage import Mailing

to_adress = Adress('188689', 'Воронеж', 'Звездная', '58', '48')
from_adress = Adress('199125', 'Санкт-Петербург', 'Есенина', '5', '125')
track = str('556677')
cost = int(500)

mailing = Mailing(to_adress, from_adress, track, cost)

print(f'Отправление {mailing.track} из {to_adress.index}, {to_adress.city}, {to_adress.street}, {to_adress.house} - {to_adress.apartament} в {from_adress.index}, {from_adress.city}, {from_adress.street}, {from_adress.house} - {from_adress.apartament}. Стоимость {mailing.cost} рублей.')
