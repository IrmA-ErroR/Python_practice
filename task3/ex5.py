# 5. Создание zip архива, добавление туда файла, определение размера архива (модуль zipfile)
# * Создать архив в форматер zip
# * Добавить файл, выбранный пользователем, в архив
# * Разархивировать файл и вывести данные о нем
# * Удалить файл и архив

import json
import xml.etree.ElementTree as ET
import os
import zipfile
import time

from ex2 import create_file, read_file, delete_file

def create_zip_archive(zip_name, files):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file)
    print(f"\nАрхив {zip_name} успешно создан")

def extract_zip_archive(zip_name, extract_path):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_path)
    print(f"\nСодержимое архива {zip_name} успешно извлечено")

def get_zip_size(zip_name):
    size = os.path.getsize(zip_name)
    print(f"Размер архива {zip_name}: {size} байт")

# Генерация данных
def generate_user_data():
    file_name = "test.txt"
    user_input = input("Введите строку для записи в файл: ")
    create_file(file_name, user_input)
    return file_name

def delete_directory_contents(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Файл {file_path} успешно удален.")
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        except Exception as e:
            print(f"Ошибка при удалении файла {file_path}: {e}")

def main():
    zip_name = "user_data.zip"

    test_file = input("Введите путь к файлу для добавления в архив или команду generate: ")
    if test_file.lower() != "generate":
        while not os.path.exists(test_file):
            print("Файл не найден. Пожалуйста, введите корректный путь.")
            test_file = input("Введите путь к файлу для добавления в архив: ")
    else:
        test_file = generate_user_data()

    create_zip_archive(zip_name, [test_file])

    # Раземер архива
    get_zip_size(zip_name)

    extract_path = "./extracted_files"
    os.makedirs(extract_path, exist_ok=True)
    extract_zip_archive(zip_name, extract_path)

    for root, dirs, files in os.walk(extract_path):
        for file_name in files:
            extracted_data = os.path.join(root, file_name)
            print(extracted_data)

            # информация о файле
            file_size = os.path.getsize(extracted_data)
            last_modified_time = time.ctime(os.path.getmtime(extracted_data))
            print(f"\nСведения о файле {file_name}:")
            print(f"Размер файла: {file_size} байт")
            print(f"Последнее изменение: {last_modified_time}")
            print("Содержимое файла:")
            print("\n", read_file(extracted_data))
            
    if file_name == "test.txt":
        delete_file(test_file)

    delete_file(zip_name)

    delete_directory_contents(extract_path)
    os.rmdir(extract_path)
    print(f"Директория {extract_path} успешно удалена.")

if __name__ == "__main__":
    main()
