"""
Напишите скрипт который получает системный ввод от пользователя и выводит надпись "команда принята" если ввод начинается
с sys.in.
"""

import sys

# user_input = input("Введите строку: ")
# if user_input.startswith("sys.in"):
#     print("команда принята")
# else:
#     print('дядя, я такого не знаю')


user_input = sys.stdin.readline()

if user_input.startswith("sys.in"):
    print("команда принята")
else:
    print('дядя, я такого не знаю')