with open('TXT.txt', 'a') as file:
    file.write(' Но у меня не получается')

with open('TXT.txt', 'r') as file_1:
    read = file_1.read()
print(read)