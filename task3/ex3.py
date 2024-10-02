# 3. Работа с форматом JSON (модуль json)
# * Создать файл формате JSON в любом редакторе или с использованием данных, введенных пользователем
# * Создать новый объект. Выполнить сериализацию объекта в формате JSON и записать в файл.
# * Прочитать файл в консоль
# * Удалить файл

import json
import os
import re


def create_json_file(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Файл {file_name} создан и данные записаны")

def read_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Файл {file_name} успешно удален")
    else:
        print(f"Файл {file_name} не существует")

def main():
    user_file_name = input("Введите имя файла: ")
    file_name = re.sub(r'[^a-zA-Z0-9_-]', '', user_file_name) + ".json"
    # file_name = "test.json"

    user_name = input("Введите ваше имя: ")
    user_age = int(input("Введите ваш возраст: "))
    # message = input("Введите сообщение: ")
    default_message = "Default message"

    user_data = {
        "name": user_name,
        "age": user_age,
        "message": default_message
    }

    create_json_file(file_name, user_data)

    data = read_json_file(file_name)
    print("Содержимое файла JSON:")
    print(json.dumps(data, indent=4))

    delete_file(file_name)


if __name__ == "__main__":
    main()

