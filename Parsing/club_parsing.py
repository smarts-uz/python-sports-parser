import sys


sys.dont_write_bytecode = True

# Django specific settings
import os
from dotenv import load_dotenv
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django

django.setup()
load_dotenv()
base_path = os.getenv('base_path_club')
# Import your models for use in your script
from orm.db.models import Club
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from orm.db.models import Competition

def fetch_content(url, retries=3, timeout=10):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            if attempt < retries - 1:
                print(f"Retrying ({attempt + 1}/{retries})...")
    return None


a = Competition.objects.all()
for club in a:

    url = f'https://www.sports.ru/football/tournament/{club.slug}/table/'

    response_content = fetch_content(url)
    if response_content is None:
        print(f"Failed to fetch {url} after retries.")
        continue

    country_id = club.country_id
    competition_id = club.id

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('div', class_='stat mB6')
    table_body = table.find('tbody')
    table_row = table_body.find_all('tr')

    i = 0
    for row in table_row:
        name_tag = row.find('a', class_="name")
        if not name_tag:
            continue

        name_ru = name_tag['title']
        name_en = GoogleTranslator(source='auto', target='en').translate(name_ru)
        club_link = name_tag['href']
        slug = club_link.split('/')[-2]

        club_response = requests.get(club_link)
        club_soup = BeautifulSoup(club_response.content, 'html.parser')

        descr_tag = club_soup.find('div', class_="descr")
        descr = descr_tag.text if descr_tag else ""

        region_tag = club_soup.find('th', string='Страна')
        if region_tag:
            region_td = region_tag.find_next_sibling('td')
            country_ru = region_td.get_text(strip=True) if region_td else ""
            country_en = GoogleTranslator(source='auto', target='en').translate(country_ru)
        else:
            country_en = "N/A"

        trener_tag = club_soup.find('th', string='Тренер')
        if trener_tag:
            trener_td = trener_tag.find_next_sibling('td')
            trener_ru = trener_td.get_text(strip=True) if trener_td else ""
            trener_en = GoogleTranslator(source='auto', target='en').translate(trener_ru)
        else:
            trener_en = "N/A"

        print(name_en, name_ru, club_link)

        club_logo_box = club_soup.find('div', class_="img-box")
        club_logo = club_logo_box.find('img')['src']
        file_type = club_logo.split('.')[-1]
        logo_response = requests.get(club_logo).content
        print(f'{name_en}.{file_type}')

        club_path = os.path.join(base_path, slug)
        os.makedirs(club_path, exist_ok=True)
        logo_path = os.path.join(club_path, f'{name_en}.{file_type}')
        relative_logo_path = logo_path.split('C:/Users/user/Desktop/Parser/Proliga')[-1].replace('\\', '/')
        print(relative_logo_path)

        form_img = os.path.join(os.path.dirname(relative_logo_path), 'App.png').replace('\\', '/')
        print(form_img)

        with open(logo_path, 'wb') as f:
            f.write(logo_response)
        print(f'{name_en} Saved photo! ')

        try:
            Club.objects.get(name="lala")
            print('Already Exists: ', name_en)
        except Club.DoesNotExist:
            Club.objects.create(
                name=name_en,
                flag_url=relative_logo_path,
                country_id=country_id,
                name_ru=name_ru,
                club_link=club_link,
                slug=slug,
                native=descr,
                region=country_en,
                trainer=trener_en,
                competition_id=competition_id,
                form_img=form_img
            )
            i += 1
            print(i, 'created: ', name_en)
