import csv
import requests
from bs4 import BeautifulSoup

# Создаем пустые списки для каждой колонки
names = []
prices = []
locations = []
descriptions = []

# Читаем страницу и парсим данные
url = 'https://businessesforsale.ru/krasnodarskiy-kray-kupit-gostinicu/'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

# Добавляем данные в списки
names += [x.text.strip() for x in soup.find_all('a', class_='title visible-desktop visible-tablet')]
prices += [x.text for x in soup.find_all('span', class_='price')]
locations += [x.text for x in soup.find_all('a', class_='info_location')]
descriptions += [x.text for x in soup.find_all('p', class_='desc')]

# Записываем данные в CSV-файл
with open('table.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Цена', 'Локация', 'Описание'])
    for _ in zip(names, prices, locations, descriptions):
        writer.writerow(_)

print('Файл table.csv создан')
