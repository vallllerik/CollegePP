"""
Создайте класс Person у которого будут свойства name и age.
Добавьте метод экземпляра который выводит информацию о человеке.
Создайте метод класса который генерирует новый объект класса
который ставить возраст человека: сегодняшний год - год который передают в метод.
(подсказка: тут можно использовать метод today().year класса date из модуля datetime)
Создайте статический метод который проверяет является ли совершеннолетним человек возраст которого передается в метод.
"""

from datetime import *


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'

    def print_info(self):
        print(f'Имя: {self.name}\n'
              f'Возраст: {self.age}')

    @classmethod
    def generate_person(cls, name, year):
        now = datetime.now()
        age = now.year - year
        return cls(name, age)

    @staticmethod
    def check_adult(person):
        if person.age >= 18:
            return True
        else:
            return False


def main():
    kek = Person('Kek', 15)
    kek.print_info()

    lol = Person.generate_person('Lol', 1999)
    print(lol)

    print(Person.check_adult(lol))
    print(Person.check_adult(kek))


main()