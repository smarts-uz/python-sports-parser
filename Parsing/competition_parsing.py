import sys
import os
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from dotenv import load_dotenv

sys.dont_write_bytecode = True

# Django specific settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django
django.setup()

# .env faylidan yuklang
load_dotenv()

# HTML fayllarini va logolarni saqlash uchun asosiy yo'l
base_path_html = os.getenv('base_path_competition')  # HTML va logolar saqlash joyi

# Agar HTML katalog mavjud bo'lmasa, uni yaratamiz
if not os.path.exists(base_path_html):
    os.makedirs(base_path_html)

from orm.db.models import Competition

url = os.getenv('competitions_url')
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', class_='ratings-table tags-rating js-active')
table_body = table.find('tbody')
table_row = table_body.find_all('tr')

i = 0
for row in table_row:
    name_tag = row.find('a', class_="name")
    if not name_tag:
        continue

    name_ru = name_tag.text.strip()
    name_en = GoogleTranslator(source='auto', target='en').translate(name_ru)
    competition_link = name_tag['href']
    slug = competition_link.split('/')[-2]

    # Musobaqa ma'lumotlarini olish va HTML faylini saqlash
    competition_folder = os.path.join(base_path_html, name_en)
    if not os.path.exists(competition_folder):
        os.makedirs(competition_folder)

    # HTML faylini saqlash
    html_file_path = os.path.join(competition_folder, f"{slug}.html")
    html_response = requests.get(competition_link)
    with open(html_file_path, 'wb') as html_file:
        html_file.write(html_response.content)
        print(f"HTML saved for {name_en}: {html_file_path}")

    # Logo olish
    logo_url = None
    club_logo_box = BeautifulSoup(html_response.content, 'html.parser').find('div', class_="img-box")
    if club_logo_box:
        club_logo = club_logo_box.find('img')['src']
        logo_url = club_logo

        # Logo saqlash
        logo_response = requests.get(logo_url)
        logo_file_path = os.path.join(competition_folder, f"{slug}_logo.{logo_url.split('.')[-1]}")
        with open(logo_file_path, 'wb') as logo_file:
            logo_file.write(logo_response.content)
            print(f"Logo saved for {name_en}: {logo_file_path}")

    # Ma'lumotlar bazasiga musobaqani yaratish yoki yangilash
    try:
        Competition.objects.get(name=name_en)
        print('Already Exists: ', name_en)
    except Competition.DoesNotExist:
        Competition.objects.create(
            name=name_en,
            title=name_en,
            name_ru=name_ru,
            competition_link=competition_link,
            slug=slug,
        )
        i += 1
        print(i, 'created: ', name_en)