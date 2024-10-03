# Разработайте программное обеспечение проверки криптостойкости паролей с использованием атаки методом грубой силы (брутфорс). 
# Найдите с помощью алгоритма полного перебора пятибуквенные пароли, соответствующие следующим хэш-значениям SHA-256 и выведите их на экран:
import hashlib
import itertools
import time

# Первый хэш:
h_1 = "1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad"
# Второй хэш:
h_2 = "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b"
# Третий хэш:
h_3 = "74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f"

# Хэш значения могут считываться из файла или непосредственно с консоли (формы для ввода хэш-значения).
# Ваша программа должна перебрать все возможные пароли, состоящие только из пяти строчных букв английского алфавита ASCII.
# Программа должна иметь возможность запуска перебора в однопоточном режиме или в многопоточном режиме (количество потоков 
# может задаваться пользователем). Для каждого режима необходимо выводить затраченное время на подбор.
# Код должен быть стойким к ошибкам ввода (предполагается использование конструкций обработки ошибок try:... except:... и 
# дополнительных проверок входных данных). Программа должна содержать интерфейс для ввода данных и выбора действий, 
# тип интерфейса: графический или консольный

alphabet = 'abcdefghijklmnopqrstuvwxyz'

from concurrent.futures import ThreadPoolExecutor


# Функция вычисления SHA-256
def compute_sha256(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


# Однопоточный режим 
def brute_force_single_thread(hash_list):
    start_time = time.time()

    for password_tuple in itertools.product(alphabet, repeat=5):
        password = ''.join(password_tuple)
        hashed_password = compute_sha256(password)
        
        if hashed_password in hash_list:
            print(f"Пароль найден: {password} для хэша: {hashed_password}")

    elapsed_time = time.time() - start_time
    print(f"Однопоточный брутфорс завершен за {elapsed_time:.2f} секунд")


# Многопоточный режим 
def brute_force_multi_thread(hash_list, num_threads):
    start_time = time.time()

    # Создание пула потоков
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for password_tuple in itertools.product(alphabet, repeat=5):
            password = ''.join(password_tuple)
            futures.append(executor.submit(check_password, password, hash_list))
        
        for future in futures:
            if future.result() is not None:
                print(f"Пароль найден: {future.result()}")

    elapsed_time = time.time() - start_time
    print(f"Многопоточный брутфорс завершен за {elapsed_time:.2f} секунд")


# Функция проверки пароля
def check_password(password, hash_list):
    hashed_password = compute_sha256(password)
    if hashed_password in hash_list:
        return password
    return None


def main():
    hash_list = [h_1, h_2, h_3]

    # Выбор режима работы
    mode = input("Выберите режим (single / multi): ").strip().lower()

    if mode == "single":
        brute_force_single_thread(hash_list)
    elif mode == "multi":
        try:
            num_threads = int(input("Введите количество потоков: "))
            if num_threads < 1:
                raise ValueError("Количество потоков должно быть больше 0.")
            brute_force_multi_thread(hash_list, num_threads)
        except ValueError as e:
            print(f"Ошибка: {e}")
    else:
        print("Неверный выбор режима")


if __name__ == "__main__":
    main()

