def match():
    while True:
        delete = int(input('Удалить с поля? 1. Да 2. Нет'))
        if delete == 1:
            time_input = int(input('На сколько минут?'))
            print('Вы удалена с поля на', time_input, 'минут(-ы)')
            sleep(time_input)
            print('Возвращайтесь на поле!')
        else:
            pass


match()