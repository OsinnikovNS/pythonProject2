import requests
from bs4 import BeautifulSoup as Bs

url = "https://en.soccerwiki.org/league-php?leagueid=28"

html = requests.get(url).text
soup = Bs(html, 'html.parser')

div = soup.find('div', "col-lg-8 col-12")  # row mt-3 mb-3
table = div.find('table', attrs={'class': ['table-custom', 'table-roster']})
# print(table)
tds = table.select('td:nth-of-type(2) a')

print('*****-CLUB-*****')
for td in tds:
    print(td.text)
print('-*' * 10)
