"""
Создайте класс который будет устанавливать свойство name и иметь метод
который к имени прибавляет надпись "гений". Создайте еще 1 класс, унаследуйте предыдущий.
Во втором классе вызовите метод класса родителя и добавьте к выводу надпись "но его отчислят если он не будет учить ООП".
Создайте экземпляр второго класса с вашим именем и вызовите метод печатающий всю надпись.
"""

class Genius:

    def __init__(self, name):
        self.name = name

    def write_genius(self):
        return f'{self.name} гений'


class secondclass(Genius):

    def __init__(self, name):
        super().__init__(name)

    def make_object(self):
        one = Genius(self.name)
        return one

    def complete(self):
        print(f'{self.make_object().write_genius()}, но его отчислят если он не будет учить ООП')


def check():
    test = secondclass('Valerius')
    test.complete()


check()