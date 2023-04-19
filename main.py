import csv
import requests
from bs4 import BeautifulSoup

with open('table.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Цена', 'Локация', 'Описание'])
url = 'https://businessesforsale.ru/krasnodarskiy-kray-kupit-gostinicu/'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
name = [x.text.strip() for x in soup.find_all('a', class_='title visible-desktop visible-tablet')]
price = [x.text for x in soup.find_all('span', class_='price')]
location = [x.text for x in soup.find_all('a', class_='info_location')]
description = [x.text for x in soup.find_all('p', class_='desc')]
for name, price, location, description in zip(name, price, location, description):
    file = open('table.csv', 'a', encoding='utf-8-sig', newline='')
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        name, price, location, description])
file.close()
print('Файл table.csv создан')
