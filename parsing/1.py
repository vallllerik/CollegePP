import requests
import json
from bs4 import BeautifulSoup

url = "https://music.yandex.ru/chart/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

chart_items = soup.find_all("div", class_='d-track__overflowable-column')
print(chart_items)
data = {}

for item in chart_items:
    place = item.find("div", {"class": "chart__position"}).text
    artist = item.find("div", {"class": "chart__item-title"}).text
    track = item.find("div", {"class": "chart__item-artist"}).text
    print(place, artist, track)
    data[place] = (artist, track)

with open("yandex_music_chart.json", "w", encoding="utf-8") as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)