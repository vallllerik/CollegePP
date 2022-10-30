game = input('Введите настольную игру: ')
gameList = []
while (game != '0'):
    if (game not in gameList):
        gameList.append(game)
    else:
        print('Игра уже была записана')
    game = input('Введите настольную игру: ')
gameList.sort()
print(gameList)