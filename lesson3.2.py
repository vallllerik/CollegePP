cash = int(input('Сумма к оплате:'))
time = int(input('Время оплаты:'))
if time >= 10 and time <= 12:
    cash = cash//2
    print(cash)
elif time >= 20 and time <= 22:
    cash = cash//4
    print(cash)
else:
    print(cash)