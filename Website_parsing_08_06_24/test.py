import requests
from bs4 import BeautifulSoup as Bs

url = "https://en.soccerwiki.org/league-php?leagueid=28"

html = requests.get(url).text
soup = Bs(html, 'html.parser')

div = soup.find('div', class_="col-lg-8 col-12")
table = div.find('table', attrs={'class': ['table-custom', 'table-roster']})
print(table)
tds = table.select('td:nth-of-type(2) a')

print('-*'*10)
for td in tds:
    print(td.text)