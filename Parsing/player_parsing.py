import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django

django.setup()
import requests

load_dotenv()
base_path = os.getenv('base_path_player')
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from orm.db.models import Player
from orm.db.models import Club

def get_position_code(player_position):
    switcher = {
        'вратарь': 'GOA',
        'защитник': 'DEF',
        'полузащитник': 'MID',
        'нападающий': 'STR',
        None: None
    }
    return switcher.get(player_position, 'None')

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

def sanitize_filename(filename):
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

# O'yinchilarni olish
clubs = Club.objects.all()
for club in clubs:
    url = f'https://www.sports.ru/football/club/{club.slug}/team/'
    response_content = fetch_content(url)
    if response_content is None:
        print(f"Failed to fetch {url} after retries.")
        continue

    soup = BeautifulSoup(response_content, 'html.parser')
    table = soup.find('div', class_='stat mB15')
    if table is None:
        print(f"No table found for {club.name}")
        continue

    table_body = table.find('tbody')
    if table_body is None:
        print(f"No tbody found for {club.name}")
        continue

    table_rows = table_body.find_all('tr')
    if not table_rows:
        print(f"No table rows found for {club.name}")
        continue

    for row in table_rows:
        name = row.find('a').get_text()
        player_link = row.find('a')['href']
        slug = player_link.split('/')[-2]
        name_ru = row.find('a').get_text()
        number = row.find('td').get_text(strip=True) or '0'
        name = GoogleTranslator(source='auto', target='en').translate(name)
        player_position = row.find_all('td')[-1].get_text(strip=True)
        position_code = get_position_code(player_position)

        # O'yinchining rasm URL manzilini olish
        player_image_tag = row.find('img')
        player_image_url = player_image_tag['src'] if player_image_tag else None

        # O'yinchi borligini tekshirish (slug va club bo'yicha)
        try:
            Player.objects.get(slug=slug, club=club)  # Agar o'yinchi mavjud bo'lsa, davomini o'tkazish
            print(f'Already Exists: {name} | Club ID: {club.id} | Player Link: {player_link}')
            continue  # O'yinchi mavjud bo'lsa, uni e'tiborsiz qoldirish
        except Player.DoesNotExist:
            # Agar o'yinchi yo'q bo'lsa, yangi o'yinchi yaratish
            player_image_path = None
            if player_image_url:
                player_image_response = fetch_content(player_image_url)
                if player_image_response is None:
                    print(f'Failed to fetch image for {name} | Club ID: {club.id}')
                    continue

                # Fayl nomini sanitizatsiya qilish
                sanitized_name = sanitize_filename(name)
                player_image_path = os.path.join(base_path, club.slug, f'{sanitized_name}.jpg')  # Rasm uchun yo'l

                # Rasmni saqlash
                os.makedirs(os.path.dirname(player_image_path), exist_ok=True)
                with open(player_image_path, 'wb') as f:
                    f.write(player_image_response)
                print(f'Saved image for {name} | Club ID: {club.id} ')  # Rasm yo'lini konsolda chiqarish

            # Yangi o'yinchini bazaga qo'shish
            Player.objects.create(
                name=name,
                slug=slug,
                shirt_number=number,
                club=club,
                position=position_code,
                name_ru=name_ru,
                player_link=player_link,
                image=player_image_path if player_image_url else None,
            )
            print(f'Created: {name} | Club ID: {club.id} | Player Link: {player_link} | Image Path: {player_image_path}')  # Yangi yaratilgan o'yinchi haqidagi ma'lumotlar

    # O'yinchilarni tekshirish
    existing_players_count = Player.objects.filter(club=club).count()
    required_players_count = len(table_rows)

    if existing_players_count < required_players_count:
        print(f'Club {club.name} has {required_players_count} players listed, but only {existing_players_count} exist in the database.')
    elif existing_players_count > required_players_count:
        print(f'Warning: Club {club.name} has more players in the database ({existing_players_count}) than listed ({required_players_count}).')

    print(f"\n{club.name} Players parsing finished\n")