"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""
class Man:

    def krya(self):
        print('Имитирую кряканье')

    def wear_clothes(self):
        print('Я одет')


class Duck:

    def krya(self):
        print('КРЯ-КРЯ-КРЯ!!!')

    def wear_clothes(self):
        print('Я не кот в сапогах, Я утка в очках! КРЯ')


def main():
    my_list = [Person(), Duck()]
    for i in my_list:
        i.krya_krya()
        i.wear_clothes()


main()