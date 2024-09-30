# Задача 1
# Изучить принципы создания декораторов в Python
# Написать декоратор, который будет оборачивать функцию следующим образом: перед выполнением функции напечатать текущую дату, а после выполнения функции - время ее выполнения. 
# Обернуть таким декоратором любую функцию, которая будет выполняться больше одной секунды.
# Примечание: конструкция создания декоратора приведена на изображении:
import time
import datetime

def my_decorator(func):
    print('==========')
    def modified():
        print('Текущая дата и время:', datetime.datetime.now())
        start_time = time.time()        
        result = func()
        end_time = time.time()
           
        if end_time - start_time > 1:
            print('Время выполнения:', end_time - start_time)

        return result
    return modified

@my_decorator
def hello():
    time.sleep(2)
    print('Hello!')


hello()

