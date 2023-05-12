"""
Изучите API сервиса https://randomuser.me/
Выведите цитату "Hi, im #NAME, im from #COUNTRY, my phone number is #PHONE"
"""
import requests
r=requests.get('https://randomuser.me/api/').json()
print('Hello', r["results"][0]['name']['first'], 'im from', r['results'][0]['location']['country'], 'my phone', r['results'][0]['phone'])