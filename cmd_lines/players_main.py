import os
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
from function.fetch_content import fetch_content
# Import Django models after setting up Django
from orm.db.models import Player, Club

# Base paths for saving player and club HTML files
base_path_player = os.getenv('base_path_player')

# def update_or_create_player(name, slug, **fields):
#     """O'yinchini yangilash yoki yaratish."""
#     players = Player.objects.filter(name=name, slug=slug)
#
#     if players.count() > 1:
#         print(f"Multiple players found for {name}. Please check the data.")
#         return None, False
#
#     if players.exists():
#         player = players.first()
#         for field, value in fields.items():
#             setattr(player, field, value)
#         player.save()
#         print(f"Updated player: {name} (Slug: {slug})")
#         created = False
#     else:
#         player = Player.objects.create(name=name, slug=slug, **fields)
#         print(f"Created new player: {name} (Slug: {slug})")
#         created = True
#
#     return player, created

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

            player=Player.objects.filter(slug=slug,competition_id=competition_id)
            if player:
                # Updating the players main data
                player.name=name_en
                player.shirt_number=number
                player.club_id=club.id
                player.name_ru=name
                player.player_link=player_link
                player.slug=slug
                player.competition_id=competition_id
                player.updated_at=timezone.now()
                player.save()
                print(f"Updated existings Player:{player.name} id:{player.id} with link:{player_link}")
            else:
                # Creating new found playerss
                player=Player.objects.create(
                    name=name_en,
                    shirt_number=number,
                    club_id=club.id,
                    name_ru=name,
                    player_link=player_link,
                    slug=slug,
                    competition_id=competition_id,
                    created_at=timezone.now(),
                )
                print(f"Created new Player:{player.name} id:{player.id} with link:{player_link}")

            player_foldr_path=os.path.join(base_path_player,slug)
            os.makedirs(player_foldr_path, exist_ok=True)
            html_file_path = os.path.join(player_foldr_path,f"{name_en}.html")
            html_downloader(name_en,player_link,html_file_path)
