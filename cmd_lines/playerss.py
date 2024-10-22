import os
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from django.utils import timezone
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the Django settings module environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')

# Initialize Django
import django
django.setup()

from monolithh.monolith_htmls import html_downloader
from function.fetch_content import fetch_content,get_position_code
# Import Django models after setting up Django
from orm.db.models import Player, Club

# Base paths for saving player and club HTML files
base_path_player = os.getenv('base_path_player')
# base_path_club = os.getenv('base_path_club')


def update_or_create_player(name, slug, **fields):
    """O'yinchini yangilash yoki yaratish."""
    players = Player.objects.filter(name=name, slug=slug)

    if players.count() > 1:
        print(f"Multiple players found for {name}. Please check the data.")
        return None, False

    if players.exists():
        player = players.first()
        for field, value in fields.items():
            setattr(player, field, value)
        player.save()
        print(f"Updated player: {name} (Slug: {slug})")
        created = False
    else:
        player = Player.objects.create(name=name, slug=slug, **fields)
        print(f"Created new player: {name} (Slug: {slug})")
        created = True

    return player, created

def parse_players(competition_id):
    """Berilgan competition_id orqali o'yinchilarni parslash."""
    clubs = Club.objects.filter(competition_id=competition_id)
    if not clubs.exists():
        print(f"No clubs found for competition ID: {competition_id}")
        return

    for club in clubs:
        print(f"Parsing players for club: {club.name} (ID: {club.id})")
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

        for row in table_rows:
            name = row.find('a').get_text()
            player_link = row.find('a')['href']
            slug = player_link.split('/')[-2]
            name_en = GoogleTranslator(source='auto', target='en').translate(name)
            number = row.find('td').get_text(strip=True) or '0'
            player_position = row.find_all('td')[-1].get_text(strip=True)
            position_code = get_position_code(player_position)

            player, created = update_or_create_player(
                name=name_en,
                slug=slug,
                shirt_number=number,
                club=club,
                position=position_code,
                name_ru=name,
                player_link=player_link,
                competition_id=competition_id,
                updated_at=timezone.now(),
                created_at=timezone.now(),
            )

            if created:
                print(f'Created: {name_en}, Club ID: {club.id}, Link: {player_link}')
            else:
                print(f'Already Exists: {name_en}, Slug: {slug}, Club ID: {club.id}, Link: {player_link}')

            player_foldr_path=os.path.join(base_path_player,slug)
            os.makedirs(player_foldr_path, exist_ok=True)
            html_file_path = os.path.join(player_foldr_path,f"{name_en}.html")
            html_downloader(name_en,player_link,html_file_path)

# Competition ID'ni kiriting
competition_id = 1  # O'zingizga kerakli competition_id ni kiriting
parse_players(competition_id)