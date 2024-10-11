import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
from dotenv import load_dotenv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django
django.setup()
load_dotenv()

# Define the base path for saving HTML files
base_path_html = os.getenv('base_path_html', 'd:/Python projects/sports images/Competition_HTML/')  # HTML saqlash joyi

# Create the directory if it doesn't exist
if not os.path.exists(base_path_html):
    os.makedirs(base_path_html)

from orm.db.models import Competition
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import subprocess

# Olish uchun URL
url = 'https://www.sports.ru/football/tournament/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Musobaqalar jadvalini topish
table = soup.find('table', class_='ratings-table tags-rating js-active')
table_body = table.find('tbody')
table_row = table_body.find_all('tr')

i = 0
for row in table_row:
    name_tag = row.find('a', class_="name")
    if not name_tag:
        continue

    # Musobaqa ma'lumotlarini olish
    name_ru = name_tag.text.strip()
    name_en = GoogleTranslator(source='auto', target='en').translate(name_ru)
    competition_link = name_tag['href']
    slug = competition_link.split('/')[-2]

    # Monolith yordamida HTML ni saqlash
    html_file_path = os.path.join(base_path_html, f"{slug}.html")
    try:
        subprocess.run(["monolith", competition_link, "-o", html_file_path], check=True)
        print(f"HTML saved for {name_en}: {html_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while downloading HTML for {name_en}: {e}")
        continue

    # Ma'lumotlar bazasiga yozish
    try:
        Competition.objects.get(name=name_en)
        print('Already Exists: ', name_en)
    except Competition.DoesNotExist:
        Competition.objects.create(
            name=name_en,
            title=name_en,
            competition_link=competition_link,
            slug=slug,
        )
        i += 1
        print(i, 'created: ', name_en)