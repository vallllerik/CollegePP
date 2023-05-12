def prise():
    ball = int(input('Кол-во баллов - '))
    if ball in range(1, 50):
        return print('Скидка 10%')
    elif ball in range(50, 100):
        return print('Скидка 15%')
    else:
        return print('Скидка 20%')
prise()