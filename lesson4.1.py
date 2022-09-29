food = input()
food = food.lower()
if (food == 'завтрак'):
    print('Каша')
elif (food != 'завтрак'):
    print('Ты хочешь плотно поесть?')
    meal = input()
    meal = meal.lower()
    if (meal == 'да'):
        print('Плов')
    else:
        print('Котлета с пюре')