class Hero():
    def __int__(self, name, health, armor):
        self.name = name
        self.health = health
        self. armor = armor
    def print_info(self):
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)

class Magician(Hero):
    def __init__(self, health, power):
        super().__init__(health, power)

    def hello(self):
        print('Салам!')

    def attack(self, another_gamer):
        another_gamer.health -= self.power * 2
        self.power -= 2
        print('Хук справа')


def check():
    hero = Hero(300, 20)
    mag = Magician(200, 20)
    mag.hello()
    mag.attack(hero)
    print(f'Сила мага: {mag.power}')
    print(f'Здоровье героя: {hero.health}')


check()