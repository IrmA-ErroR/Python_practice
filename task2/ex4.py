# Задача 4
# Изучить регулярные выражения в Python: модуль re, метод re.compile: 
# Используя регулярные выражения, написать программу, которая будет проверять, является ли набранный текст электронной почтой

import re

emails_list = ["example@example.com", "user@domain.com", "invalid-email@", "another_test@domain.org", "sveta@mail.ru"]

def check_valid_email(string):
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if pattern.match(email):
        return 'VALID'
    else:
        return 'INVALID'


for email in emails_list:
    print(f'{email} - {check_valid_email(email)}')
