# 5. Создание zip архива, добавление туда файла, определение размера архива (модуль zipfile)
# * Создать архив в форматер zip
# * Добавить файл, выбранный пользователем, в архив
# * Разархивировать файл и вывести данные о нем
# * Удалить файл и архив

import json
import xml.etree.ElementTree as ET
import os
import zipfile

from ex2 import create_file, read_file, delete_file

def create_zip_archive(zip_name, files):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file)
    print(f"Архив {zip_name} успешно создан")

def extract_zip_archive(zip_name, extract_path):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_path)
    print(f"Архив {zip_name} успешно извлечен")

def get_zip_size(zip_name):
    size = os.path.getsize(zip_name)
    print(f"Размер архива {zip_name}: {size} байт")

# Генерация данных
def generate_user_data():
    file_name = "test.txt"
    user_input = input("Введите строку для записи в файл: ")
    create_file(file_name, user_input)
    return file_name

def main():
    zip_name = "user_data.zip"
    test_file = generate_user_data()

    create_zip_archive(zip_name, [test_file])

    # Раземер архива
    get_zip_size(zip_name)

    extract_path = "."
    os.makedirs(extract_path, exist_ok=True)
    extract_zip_archive(zip_name, extract_path)

    print("\nСодержимое извлеченного файла:")
    extracted_data = os.path.join(extract_path, test_file)
    print("\t", read_file(extracted_data))

    delete_file(test_file)
    delete_file(zip_name)

if __name__ == "__main__":
    main()
