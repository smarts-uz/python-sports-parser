import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
from dotenv import load_dotenv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django
django.setup()
load_dotenv()

# Define the base path for saving logos
base_path = os.getenv('base_path_club')

from orm.db.models import Competition
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

url = 'https://www.sports.ru/football/tournament/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', class_='ratings-table tags-rating js-active')
table_body = table.find('tbody')
table_row = table_body.find_all('tr')

i = 0
for row in table_row:
    name_tag = row.find('a', class_="name")
    print(name_tag)

    if not name_tag:
        continue

    name_ru = name_tag.text.strip()
    name_en = GoogleTranslator(source='auto', target='en').translate(name_ru)
    competition_link = name_tag['href']
    slug = competition_link.split('/')[-2]
    print(name_ru, " ", name_en, " ", competition_link, " ", slug)

    club_response = requests.get(competition_link)
    club_soup = BeautifulSoup(club_response.content, 'html.parser')

    club_logo_box = club_soup.find('div', class_="img-box")
    if club_logo_box:
        club_logo = club_logo_box.find('img')['src']
        file_type = club_logo.split('.')[-1]
        logo_response = requests.get(club_logo).content
        print(club_logo)

    # Create or update the competition entry in the database
    try:
        Competition.objects.get(name=name_en)
        print('Already Exists: ', name_en)
    except Competition.DoesNotExist:
        Competition.objects.create(
            title=name_en,
            flag=club_logo,  # Use the relative path for the flag field
            name_ru=name_ru,
            competition_link=competition_link,
            slug=slug,
        )
        i += 1
        print(i, 'created: ', name_en)
