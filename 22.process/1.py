"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""

import multiprocessing

# Функция для подсчета суммы четных чисел
def sum_even(start, end):
    result = 0
    for i in range(start, end):
        if i % 2 == 0:
            result += i
    print("Сумма четных чисел:", result)

# Функция для подсчета суммы нечетных чисел
def sum_odd(start, end):
    result = 0
    for i in range(start, end):
        if i % 2 != 0:
            result += i
    print("Сумма нечетных чисел:", result)

if __name__ == '__main__':
    
    # Создание процессов
    p1 = multiprocessing.Process(target=sum_even, args=(1, 1000000))
    p2 = multiprocessing.Process(target=sum_odd, args=(1, 1000000))
    
    # Запуск процессов
    p1.start()
    p2.start()
    
    # Ожидание завершения процессов
    p1.join()
    p2.join()