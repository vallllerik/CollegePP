"""
Напишите скрипт который принимает 2 аргумента - путь и имя папки. И создаем папку по указанному пути.
"""

import sys
import os

if len(sys.argv) != 3:
    print("Используй конструкцию: python3 4.py <way to heaven> <directory name>")
else:
    way = sys.argv[1]
    directory = sys.argv[2]
    os.system("mkdir {0}/{1}".format(way, directory))
