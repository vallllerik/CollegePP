a = input().split(', ')
n = ['5','3','4', '5', '5', '2', '3', '3']
usp = 0
for elem in n:
	usp += a.count(elem)
print(a, len(a), usp / len(a) * 100)

