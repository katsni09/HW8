# Написати валідації за допомогою регулярних виразів:
#
# - домашній номер телефону (тільки цифри та довжина номера)

import re
list = ['123123123', '345345345', '567567567']
for value in list:
    # search = re.match(r'\d{9}', value))
    if re.match(r'\d{9}', value):
        print('yes', len(value))
    else:
        print('no')




