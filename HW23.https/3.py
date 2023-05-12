"""
Изучите API сервиса https://rickandmortyapi.com/
Получите имя, родную планету и список эпизодов  всех персонажах начиная с вашего номера в журнале и заканчивая ваш номер*5
Сохраните в .json файл.
"""

import requests
r=requests.get('https://rickandmortyapi.com/api/character').json()

ids=r['results'][0]['id']
ids_last=r['results'][ids*5]['id']

for i in range(ids, ids_last):
    if ids==ids_last:
        print('Имя', r['results'][ids_last]['name'], 'планета', r['results'][ids_last]['location']['name'], r['results'][ids_last]['episode'])
    print('Имя', r['results'][ids]['name'], 'планета', r['results'][ids]['location']['name'], r['results'][ids]['episode'])
    ids+=1