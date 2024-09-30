# Задача 3
# Изучить регулярные выражения в Python: модуль re, методы re.match, re.sub, метасимволы
# Напишите программу, которая принимает слово в качестве ввода и выводит "Match", если слово состоит из 4 букв, начинается с "m" и заканчивается на "е". 
# Программа должна выводить "No match", через всплывающее уведомление tkinter.messagebox, метод showerror(), если перечисленные условия не выполнены.

import re
from tkinter import *
from tkinter.messagebox import showerror, showinfo

list_of_words = ['mame', 'mate', 'metro']

def check_word(word):
    pattern = r'^m\w{2}e$'
    if re.match(pattern, word):
        print('Match')
        # showinfo(title=None, message='Match')
    else:
        showerror(title=None, message='No match')


for word in list_of_words:
    check_word(word)