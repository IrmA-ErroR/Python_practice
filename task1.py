# БИСО-01-20 Кабанова С.О.
## Задание 1 02.09.2024

import os

# Зайти в онлайн компилятор: https://www.online-python.com/
# Выполненные задания прислать на почту: mamaev@mirea.ru

print('\nЗадача 1')
# Есть список 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Выведите все элементы, которые меньше 5.
def less_then(arr):
    arr.sort()
    print(*[item for item in arr if item < 5])
    return None

less_then(a)


print('\nЗадача 2')
# Даны списки:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

def both(a, b):
    my_array = list(set(a) & set(b))
    return my_array

print(both(a, b))


print('\nЗадача 3')
# Напишите программу, которая использует цикл, для первых 10 чисел. 
# В каждом цикле, ваша задача заключается в том, что бы вывести сумму, предыдущего и текущего числа.

def strange_summ():
    for i in range(10):
        print(f'Числа: {i} и {i+1} , сумма: {i+i+1}')

strange_summ()
 
print('\nЗадача 4')
# При заданном целом числе n посчитайте n + nn + nnn.

def my_function(n):
    return n + n*n + n*n*n

n = 2
print(my_function(int(input('Введите число: '))))

print('\nЗадача 5')
# Выведите список файлов в указанной директории.

def files_dir(my_path):
    files = os.listdir(my_path)
    return files

print('Файлы директории:', files_dir(input('Введите путь: ')))

print('\nЗадача 6')
# Сложите цифры целого числа.

def digit_summ(n):
    s = 0
    for i in str(n):
        s += int(i) 
    return s

print('Сумма цифр:', digit_summ(int(input('Введите число: '))))