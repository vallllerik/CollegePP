from time import *


def game():
   start = time()
   while time() - start < 18000:
       step = input('Введите ход: ')
       if step.lower() == 'off':
           break
       else:
           print(f'Вы потратили на ход: {round(time() - start, 2)} секунд')
       print(f'Оставшееся время: {30 -  round((time() - start) / 60, 2)} минут')


game()