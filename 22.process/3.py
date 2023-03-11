import multiprocessing
import time

def currency_converter(conn, amount):
    # Курс валюты
    exchange_rate = 75
    
    # Вычисление количества валюты
    currency_amount = amount / exchange_rate
    
    # Отправка данных через канал обмена
    conn.send(currency_amount)
    
    # Закрытие соединения
    conn.close()

if __name__ == '__main__':
    # Создание канала обмена
    parent_conn, child_conn = multiprocessing.Pipe()
    
    # Создание процесса
    p = multiprocessing.Process(target=currency_converter, args=(child_conn, 1000))
    
    # Запуск процесса
    p.start()
    
    # Ожидание завершения процесса
    p.join()
    
    # Чтение данных из канала обмена
    currency_amount = parent_conn.recv()
    
    # Вывод результата
    print(f'Можно купить {currency_amount:.2f} валюты.')
