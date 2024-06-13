"""Нельзя слишком часто отправлять запросы, сайт блокирует"""
import requests
from bs4 import BeautifulSoup

url = 'https://yandex.com.am/weather/yekaterinburg?lat=56.838011&lon=60.597465'
response = requests.get(url)
print(response)
bs = BeautifulSoup(response.text, "lxml")
# print(bs)
time_fact = bs.find('time', 'time fact__time')
temp = bs.find('div', 'temp fact__temp fact__temp_size_s')
temp1 = bs.find('div', 'link__condition day-anchor i-bem')
temp2 = bs.find('div', 'term term_orient_h fact__feels-like')
temp3 = bs.find('span', 'a11y-hidden')

print(f'******-Погода в Екатеринбурге-******')
print(f'{time_fact.text}')
print(f'Температура : {temp.text}')
print(f'{temp1.text}')
print(f'{temp2.text}')
print(f'{temp3.text}')
