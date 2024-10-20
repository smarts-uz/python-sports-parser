import sys
import os
from dotenv import load_dotenv
import click
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from function.fetch_content import fetch_content
from function.player_image_cheker import create_player_image
from django.utils import timezone
# Django specific settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django
django.setup()
from orm.db.models import Player, Club

def get_position_code(player_position):
    switcher = {
        'вратарь': 'GOA',
        'защитник': 'DEF',
        'полузащитник': 'MID',
        'нападающий': 'STR',
        None: None
    }
    return switcher.get(player_position, 'None')

def sanitize_filename(filename):
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

@click.command()
@click.option('--competition_id', type=int, required=True, help='ID of the competition to parse players from.')
def parse_players(competition_id):
    clubs = Club.objects.filter(competition_id=competition_id)
    if not clubs.exists():
        print(f"No clubs found for competition ID: {competition_id}")
        return

    for club in clubs:
        print(f"Parsing players for club: {club.name} in ID:{club.id}")
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

            # Fetch players with the same slug and competition_id
            existing_players = Player.objects.filter(slug=slug, competition_id=competition_id)

            if existing_players.exists():
                for player in existing_players:
                    print(f'Already Exists: {player.name} (Slug: {slug}), ID: {player.id}, Link: {player_link}')
                # Optionally, you can choose to skip creating new players here
                continue  # Skip to the next player if one already exists

            else:
                # Create new player record
                player = Player.objects.create(
                    name=name_en,
                    slug=slug,
                    shirt_number=number,
                    club=club,
                    position=position_code,
                    name_ru=name,
                    player_link=player_link,
                    competition_id=competition_id,
                    created_at=timezone.now(),
                )
                print(f'Created: {player.name} (ID: {player.id}), Club ID: {club.id}, Link: {player.player_link}')

                # Create player image
                create_player_image(player)

if __name__ == '__main__':
    parse_players()