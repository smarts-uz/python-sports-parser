import requests
from bs4 import BeautifulSoup


url = 'https://www.sports.ru/football/tournament/la-liga/table/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('div',class_='stat mB6')
table_body = table.find('tbody')
table_row = table_body.find_all('tr')

for row in table_row:
    title = row.find('a',class_="name")['href']
    print(title)