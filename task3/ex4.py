# 4. Работа с форматом XML (модуль xml.etree.ElementTree)
# * Создать файл формате XML из редактора
# * Записать в файл новые данные из консоли.
# * Прочитать файл в консоль.
# * Удалить файл.

import xml.etree.ElementTree as ET
import os
import re


def create_xml_file(file_name, root_element):
    tree = ET.ElementTree(root_element)
    tree.write(file_name)
    print(f"Файл {file_name} создан и данные записаны.")

def read_xml_file(file_name):
    if os.path.exists(file_name):
        tree = ET.parse(file_name)
        root = tree.getroot()
        print(f"Содержимое файла {file_name}:")
        for elem in root:
            print(f"{elem.tag}:")
            for sub_elem in elem:
                print(f"  {sub_elem.tag}: {sub_elem.text}")
    else:
        print(f"Файл {file_name} не существует")


def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Файл {file_name} успешно удален")
    else:
        print(f"Файл {file_name} не существует")


def main():
    # user_file_name = input("Введите имя файла: ")
    # file_name = re.sub(r'[^a-zA-Z0-9_-]', '', user_file_name) + ".xml"
    file_name = "test.xml"
    root = ET.Element("users_database")

    while True:
        user_name = input("Введите имя пользователя (или 'exit' для завершения): ")
        if user_name.lower() == 'exit':
            break
        user_age = input("Введите возраст: ")

        # Добавляем данные каждого пользователя как подэлемент <user>
        user_element = ET.SubElement(root, 'user')        
        name_element = ET.SubElement(user_element, 'name')
        name_element.text = user_name
        age_element = ET.SubElement(user_element, 'age')
        age_element.text = user_age

    create_xml_file(file_name, root)

    read_xml_file(file_name)

    delete_file(file_name)


if __name__ == "__main__":
    main()
        