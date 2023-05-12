def imt():
    ves = int(input('Введите вес - '))
    rost = int(input('Введите рост'))
    imt = rost / (ves *ves)
    return imt


def vse():
    imt = imt()
    if imt < 18.5:
        return print('Недостаточный вес')
    elif imt <= 18.5 and imt <25:
        return print('Норма')
    else:
        return print('Большой вес')


vse()