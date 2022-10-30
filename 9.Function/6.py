list = []


def vse():
    pisem()
    Proverka()


def pisem():
    for x in range(3):
        x = input()
        list.append(x)


def Proverka():
    for i in list:
        if i != 'None':
            print(i)


vse()
