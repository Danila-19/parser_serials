import requests
from bs4 import BeautifulSoup

url_2 = 'https://m.vk.com/myserianet?act=links'
r = requests.get(url_2).text
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
