"""
Запустите фоновый процесс который следит за сроком подписки пользователя( для примера 10 секунд) если время подписки вышло выведите надпись "Ваша подписка закончилась."
и завершите работу программы. В основной программе сыграйте с пользователем в игру "угадай число".
"""

import multiprocessing
import time

# Функция-таймер, которая будет запущена в отдельном процессе
def timer(subscription_time, end_event):
    time.sleep(subscription_time)
    end_event.set()

if __name__ == '__main__':
    # Задаем время подписки (для примера - 10 секунд)
    subscription_time = 10

    # Создаем событие для завершения работы приложения
    end_event = multiprocessing.Event()
    
    # Запускаем процесс-таймер
    timer_process = multiprocessing.Process(target=timer, args=(subscription_time, end_event))
    timer_process.start()
    
    # Запускаем игру "угадай число"
    number = 42
    while True:
        guess = input("Угадайте число от 1 до 100: ")
        
        if int(guess) == number:
            print("Вы угадали!")
            break
    
        if end_event.is_set():
            print("Ваша подписка закончилась.")
            break
    
    # Ожидаем завершения процесса-таймера
    timer_process.join()
