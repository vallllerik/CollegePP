"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""

import multiprocessing

FILENAME = 'bruh.txt'

def calculate_room_area(width, length, height):
    # Вычисление площади стен
    wall_area = str(2 * height * (width + length))
    
    # Запись площади стен в файл
    with open(FILENAME, 'w') as file:
        file.write(wall_area)

def calculate_paint_usage():
    # Чтение площади стен из файла
    with open(FILENAME, 'r') as file:
        wall_area = file.readline()
        wall_area = int(wall_area)
        print(wall_area)
    
    # Вычисление расхода краски
    paint_usage = wall_area * 5
    
    # Запись расхода краски в файл
    with open(FILENAME, 'a') as file:
        file.write('\nРасход краски: {0} л.\n'.format(paint_usage))

if __name__ == '__main__':
    
    # Создание процессов
    p1 = multiprocessing.Process(target=calculate_room_area, args=(5, 5, 5))
    p2 = multiprocessing.Process(target=calculate_paint_usage, args=())
    
    # Запуск процессов
    p1.start()
    p2.start()
    
    # Ожидание завершения процессов
    p1.join()
    p2.join()