cash = int(input('Введите цену - '))
while cash != 0:
    sale = int(input('Введите скидку в процентах - '))
    price = cash - (cash / 100 * sale)
    print('Стоимость товара со скидкой =', price)
    cash = int(input('Введите цену - '))
print('Cпасибо за покупки')