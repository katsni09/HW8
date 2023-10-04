# - email (наявність @, домену: gmail.com наприклад,
# мінімальна довжина та максимальна на ваш вибір)
import re
list_of_emails = ["katesnit19@gmail.com", "katesnit19gmail.com,", "katesnit@", "katesnit@gmail.com", "katesnit@com"]

for values in list_of_emails:
    if re.match(r'\w{3,}+@gmail\.com', values):
        print('yes')
    else:
        print('no')