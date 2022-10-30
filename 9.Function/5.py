def subject():
    name = input('Enter name: ')
    number = int(input('Enter number of subjects: '))
    while name != "стоп" or number != "стоп":
        _sum = 0
        for i in range(0, number):
            _sum += int(input('Enter score: '))
        if _sum > 80:
            print('Наградить дипломом.')
        elif 50 > _sum >= 80:
            print('Наградить похвальной грамотой.')
        elif _sum <= 50:
            print('Выдать грамоту об участии.')
        name = input('Enter name: ')
        number = int(input('Enter number of subjects: '))


subject()