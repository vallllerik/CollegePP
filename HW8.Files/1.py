with open('TXT.txt', 'w+') as file:
    file.write('Я гений и стараюсь учить питон')
    file.seek(0)
    read = file.read(7)
print(read)