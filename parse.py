import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

url_5 = 'https://m.vk.com/myserianet?act=links'
r = requests.get(url_5).text
new_list = []
soup = BeautifulSoup(r, 'lxml')
page = soup.find_all('a')

for item in page:
    new_list.append(item.get('href'))
print(new_list)
new_list.pop(0)
new_list.pop(0)
new_list.pop(0)
new_list.pop(1)

link = (" ".join(new_list))

urlss = 'https://m.vk.com/'

url_2 = urlss+link
r = requests.get(url_2).text
new_list = []
soup = BeautifulSoup(r, 'lxml')
page = soup.find_all('a')


r = requests.get(url_2).text
url='https://serialfan.net/series/'
page = requests.get(url)
filteredSeries = []
name_series = []
serios_seasons = []
serios_seasons_taked = []
soup = BeautifulSoup(page.text, "html.parser")
name_series = soup.findAll('div', class_='field-title')
serios_seasons = soup.findAll('div', class_='field-description')

for data in name_series:
    if data.find('a') is not None:
        filteredSeries.append(data.text)
    MyFile=open('serials.txt', 'w')
    for data in filteredSeries:
        MyFile.write(data)
        MyFile.write('\n')

for data in serios_seasons:
    if data.find('a') is not None:
        serios_seasons_taked.append(data.text)
    MyFile=open('series.txt', 'w')
    for data in serios_seasons_taked:
        MyFile.write(data)
        MyFile.write('\n')


MyFile=open('serials.txt', 'r')
serials = MyFile.readlines()
serials = [line.rstrip('\n') for line in serials]
MyFile.close()


MyFile=open('series.txt', 'r')
series = MyFile.readlines()
series = [line.rstrip('\n') for line in series]
MyFile.close()


data = dict(Сериал=serials, Серия=series)
df = pd.DataFrame(data)
df.to_csv('data.csv', sep=';', index=False)
print(url_2)
