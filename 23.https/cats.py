"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""

import requests

def save_random_cat_images():
    for i in range(2000):
        response = requests.get('https://cataas.com/cat', stream=True)
        with open(f'random_cat{i}.jpg', 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

def save_original_images():
    params = {'size': 'full'}
    for i in range(255):
        response = requests.get('https://cataas.com/cat', params=params, stream=True)
        with open(f'original_cat{i}.jpg', 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

def save_pixelated_images():
    params = {'filter': 'pixel'}
    for i in range(2555):
        response = requests.get('https://cataas.com/cat', params=params, stream=True)
        with open(f'pixelated_cat{i}.jpg', 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

save_random_cat_images()
save_original_images()
save_pixelated_images()