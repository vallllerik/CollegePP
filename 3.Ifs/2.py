amount = int(input())
time = int(input())
if (time >= 10) and (time <= 12):
    print(amount/2)
elif (time >= 20) and (time <= 22):
    print(amount/4)
elif ((time >= 8) and (time < 10)) or ((time > 12) and (time < 20)):
    print(amount)
else:
    print('Закрыто')