import os
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from django.utils import timezone

# Django specific settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django
django.setup()
from function.fetch_content import fetch_content,get_position_code
from function.player_image_cheker import create_player_image
from orm.db.models import Player, Club


def update_or_create_player(name, slug, club_id, player_link, **fields):
    """O'yinchini name, slug va club_id bo'yicha yangilash yoki yaratish."""
    try:
        # Klubni bazadan olamiz
        club = Club.objects.get(id=club_id)

        # O'yinchini club_id, name va slug bo'yicha qidiramiz
        players = Player.objects.filter(name=name, slug=slug, club=club)

        if players.count() > 1:
            print(f"Multiple players found for {name} in club {club_id}. Please check the data.")
            return None, False

        if players.exists():
            player = players.first()
            # Yangilanishi kerak bo'lgan maydonlarni tekshiramiz
            for field, value in fields.items():
                setattr(player, field, value)

            player.updated_at = timezone.now()  # Yangilash vaqtini yangilaymiz
            player.save()
            created = False
        else:
            # Yangi o'yinchini yaratamiz
            player = Player.objects.create(name=name, slug=slug, club=club, player_link=player_link, **fields)
            created = True

        return player, created

    except Club.DoesNotExist:
        print(f"Club with ID {club_id} does not exist.")
        return None, False
    except Exception as e:
        print(f"An error occurred while updating or creating player: {e}")
        return None, False
def parse_player_all(competition_id):
    """Berilgan competition_id asosida barcha o'yinchilarni parslaydi."""
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
            player_response_content = fetch_content(player_link)
            if player_response_content is None:
                print(f"Failed to fetch {player_link} after retries.")
                return

            player_soup = BeautifulSoup(player_response_content, 'html.parser')
            descr = player_soup.find('div', class_="descr").text


            # Futbolchini yangilash yoki yaratish
            player, created = update_or_create_player(
                name=name_en,
                slug=slug,
                shirt_number=number,
                club_id=club.id,
                position=position_code,
                name_ru=name,
                native=descr,
                player_link=player_link,
                competition_id=competition_id,
                updated_at=timezone.now(),
                created_at=timezone.now(),
            )

            if created:
                print(f'Created: {name_en}, Club ID: {club.id}, Link: {player_link}')

            else:
                print(f'Updated: {name_en}, Slug: {slug}, Club ID: {club.id}, Link: {player_link}')

            create_player_image(player)
