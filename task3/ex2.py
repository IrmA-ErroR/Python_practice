# 2. Работа с файлами (модуль os, shutil)
# * Создать файл
# * Записать в файл строку, введённую пользователем
# * Прочитать файл в консоль
# * Удалить файл

import os
import shutil

def create_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
        print(f"Файл {file_name} успешно создан")

def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Файл {file_name} успешно удален")
    else:
        print(f"Файл {file_name} не существует")


def main():
    file_name = "test.txt"

    user_input = input("Введите строку для записи в файл: ")

    create_file(file_name, user_input)

    print(f"Строка записана в файл {file_name}")

    content = read_file(file_name)
    print(f"Содержимое файла:\n\t{content}")

    delete_file(file_name)


if __name__ == "__main__":
    main()
