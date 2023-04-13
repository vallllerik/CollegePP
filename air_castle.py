class AirCastle:
    def __init__(self, height, clouds, colour):
        self.height = height
        self.clouds = clouds
        self.colour = colour

    def new_height(self, val):
        if self.height + val  <= 0:
            self.height = 0
            print('Мы на земле')
        else:
            self.height += val

    def mega_channge(self, count):
        self.clouds += count
        self.height += count //5

    def __str__(self):
        return f'Магический замок на высоте: {self.height}\n' \
               f'Количество облаков: {self.clouds}'
    def __lt__(self, other):
        return self.clouds < other.clouds or other.height < self.height

    def __lt__(self, other):
        return self.clouds > other.clouds or other.height > self.height


castle1 = AirCastle(10, 2, "красный")
castle2 = AirCastle(1203, 322, "зеленый")
print(castle1)
castle1.new_height(-123123123)
print(castle1)
castle1.mega_channge(-234234234)
print(castle1 > castle2)

