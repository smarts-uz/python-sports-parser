import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django
django.setup()
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

from orm.db.models import Player
from orm.db.models import Club

a = Club.objects.all()
for club in a:
    url = f'https://www.sports.ru/football/club/{club.name}/team/'
    b = club.id
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('div',class_='stat mB15')
    table_body = table.find('tbody')
    table_row = table_body.find_all('tr')




    def get_position_code(player_position):
        switcher = {
            'вратарь': 'GOA',
            'защитник': 'DEF',
            'полузащитник': 'MID',
            'нападающий': 'STR'
        }
        return switcher.get(player_position, 'Unknown')


    i=0
    for row in table_row:
        # table_elements = row.find_all('td')
        name = row.find('a').get_text()
        number = row.find('td').get_text(strip=True)
        if not number:
            number = '0'
        name = GoogleTranslator(source='auto', target='en').translate(name)
        player_position = row.find_all('td')[-1]["title"]
        club_link = row.find('a')['href']
        club_response = requests.get(club_link)
        club_soup = BeautifulSoup(club_response.content, 'html.parser')
        club_logo_box = club_soup.find('div', class_="img-box")
        club_logo = club_logo_box.find('img')['src']
        # print(name," ",club_link," ",number," ",club_logo)
        type = club_logo.split('.')[-1]
        logo_response = requests.get(club_logo).content
        print(f'{name}.{type}')
        with open(f'D:/Test/Sports parser/Player/{name}.{type}', 'wb') as f:
            f.write(logo_response)
        print(f'{name} Saved photo! ')
        position_code = get_position_code(player_position)
        try:
            Player.objects.get(name=name)
            print('Already Exists: ', name)
        except Player.DoesNotExist as e:
            Player.objects.create(name=name,shirt_number=number,club_id=b,position=position_code)
            i += 1
            print(i, 'created: ', name)

    print("      ")
    print(club.name, " Player finished")
    print("     ")




