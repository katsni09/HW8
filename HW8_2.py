# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
import re

list_of_phone_numbers = ["+15199807555", "519980-7555", "15199899999999999", "+12236980765"]
for values in list_of_phone_numbers:
    if re.match(r'\+\d{11,}', values) or re.match(r'\d{11 ,}', values):
        print('yes')
    else:
        print('no')
