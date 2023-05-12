def best(name):
    l1 = 'АЯГМ'
    l2 = 'ОЬЛН'
    case = [(lambda x: print(x, "Гений")), (lambda x: print(x, "Сверхразум")), (lambda x: print('Просто', x))]
    if name[-1].lower() in l1.lower():
        case[0](name)
    elif name[-1] in l2.lower():
        case[1](name)
    else:
        case[2](name)


best(input())