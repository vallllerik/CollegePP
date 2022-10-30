a = int(input('Товар 1 - '))
b = int(input('Товар 2 - '))
c = int(input('Товар 3 - '))
cash = 0
if a < b < c:
    cash = (a + b + c)/2
    print('Акция - ', cash)
elif a > b > c:
    cash = (a + b + c) / 3
    print('Акция - ', cash)
else:
    cash = (a + b + c)
    print('К оплате - ',
          cash)