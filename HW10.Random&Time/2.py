import random

sport = int(input('Количество спорцменов первой команды- '))
sport1 = int(input('Количество спорцменнов второй команды - '))
sport_1 = random.randint(1, sport)
sport_2 = random.randint(1, sport1)
print('Пловец первой команды под номером -', sport_1, '-', 'Пловец второй команды под номером -', sport_2)