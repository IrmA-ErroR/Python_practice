# Задача 5
# Изучить регулярные выражения в Python: модуль re, метод re.findall: 
# Используя регулярные выражения, реализовать алгоритм, который будет выводить на экран все email-адреса, переданные в произвольном тексте

import re

text = "Какой-то текст example@example.com, в котором есть user@domain.com и invalid-email@, а еще №;%:?*() sveta@mail.ru"
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
result = re.findall(pattern, text)

print(result)

