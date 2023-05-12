"""
Напишите скрипт который в качестве параметра из командной строки принимает имя файла. Читает команды в этом файле и выполняет их
Протестируйте скрипт на файле comands.txt
"""

import os
import sys
with open(str(sys.argv[1]), "r") as file:
    for line in file:
        os.system(line)