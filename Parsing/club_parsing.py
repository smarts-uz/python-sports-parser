import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django
django.setup()

# Import your models for use in your script
from orm.db.models import Club

import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
url = 'https://www.sports.ru/football/tournament/la-liga/table/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('div',class_='stat mB6')
table_body = table.find('tbody')
table_row = table_body.find_all('tr')
i= 0
for row in table_row:
    name = row.find('a',class_="name")['title']
    name = GoogleTranslator(source='auto', target='en').translate(name)
    club_link = row.find('a',class_="name")['href']
    print(name," ",club_link)
    club_response = requests.get(club_link)
    club_soup = BeautifulSoup(club_response.content, 'html.parser')
    club_logo_box = club_soup.find('div',class_="img-box")
    club_logo = club_logo_box.find('img')['src']
    type = club_logo.split('.')[-1]
    logo_response = requests.get(club_logo).content
    print(f'{name}.{type}')
    with open(f'D:/Test/Sports parser/Club/{name}.{type}', 'wb') as f:
        f.write(logo_response)
    print(f'{name} Saved photo! ')

    try:
        Club.objects.get(name=name)
        print('Already Exists: ',name)
    except Club.DoesNotExist as e:
        Club.objects.create(name=name,flag_url=club_logo)
        i+=1
        print(i,'created: ',name)




