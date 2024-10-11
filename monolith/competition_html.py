import sys
import os
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import subprocess
from dotenv import load_dotenv

sys.dont_write_bytecode = True

# Django specific settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django
django.setup()

# .env faylidan yuklang
load_dotenv()

# HTML fayllarini saqlash uchun asosiy yo'l
base_path_html = os.getenv('base_path_html', 'd:/Python projects/sports images/Competition_HTML/')  # HTML saqlash joyi

# Agar katalog mavjud bo'lmasa, uni yaratamiz
if not os.path.exists(base_path_html):
    os.makedirs(base_path_html)

# Olish uchun URL
url = 'https://www.sports.ru/football/tournament/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Musobaqalar jadvalini topish
table = soup.find('table', class_='ratings-table tags-rating js-active')
table_body = table.find('tbody')
table_row = table_body.find_all('tr')

for row in table_row:
    name_tag = row.find('a', class_="name")
    if not name_tag:
        continue

    # Musobaqa ma'lumotlarini olish
    name_ru = name_tag.text.strip()  # Ruscha nom
    name_en = GoogleTranslator(source='auto', target='en').translate(name_ru)  # Inglizcha nom
    competition_link = name_tag['href']
    slug = competition_link.split('/')[-2]

    # Musobaqa nomi bo'yicha katalog yaratamiz
    competition_folder = os.path.join(base_path_html, name_en)
    if not os.path.exists(competition_folder):
        os.makedirs(competition_folder)

    # Monolith yordamida HTML ni saqlash
    html_file_path = os.path.join(competition_folder, f"{slug}.html")
    try:
        subprocess.run(["monolith", competition_link, "-o", html_file_path], check=True)
        print(f"HTML saved for {name_en}: {html_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while downloading HTML for {name_en}: {e}")