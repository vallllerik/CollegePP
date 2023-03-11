"""
Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл где имя файла второй аргумент.
"""

import sys
import os

if len(sys.argv) != 3:
    print("Используй конструкцию: python3 3.py <text> <filename>")
else:
    text = sys.argv[1]
    filename = sys.argv[2]
    os.mkdir('answer')
    os.system("echo {0} > answer/{1}.txt".format(text, filename))
