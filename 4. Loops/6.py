cash = int(input('Цена товара - '))
counter = 0
while cash % 2 == 0:
    cash = cash / 2
    counter += 1
if counter > 0:
    print('К оплате -', cash)
else:
    print('К оплате -', cash * 0.75)
print('Спасибо за покупку!')