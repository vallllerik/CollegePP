def avtootvetchik(req):
    if "расп" in req:
        schedule()
    if "трен" in req:
        trener()
    if "сколько" in req:
        prise()
    if "адрес" in req:
        adress()
    if "время" in req:
        time()

def schedule():
    print("Расписание занятий: Пн, Ср, Пт")
def trener():
    print('Игнат')
def prise():
    print('5000 рублей')
def adress():
    print('Воскресенская 12')
def time():
    print("19:00")




