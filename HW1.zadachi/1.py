print("Введите первое число")
a=int(input())
print('введите второе число')
b=int(input())
sum = 0
for i in range(a,b+1):
    sum += i
print(sum)