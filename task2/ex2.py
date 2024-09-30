# Задача 2
# Изучить регулярные выражения в Python: модуль re, методы re.match, re.sub, метасимволы
# Используя регулярные выражения, написать программу, которая на входе получает телефонные номера из 10 символов, первые 2 символа которых "0", а на выходе - первые 2 "0" заменяются на "+". 
# Если на вход было подано некорректное значение - воспроизвести звук ошибки.
# Пояснение: для воспроизведения звука можно использовать дополнительный модуль playsound: https://pypi.org/project/playsound/

import re
from playsound import playsound 

my_input = ['0098765432', '009876543', '0987654321']

pattern = r'^00\d{8}$'
error_sound = 'error_sound.mp3'

def check_phone_number(number):

    if re.match(pattern, number):
        result = re.sub(r'^00', '+', number)
        return result
    else: 
        playsound(error_sound)
        return "Invalid phone number"


for number in my_input:
    print(check_phone_number(number))