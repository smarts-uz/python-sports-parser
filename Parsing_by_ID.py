import os
from dotenv import load_dotenv
import django
import click
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# Load environment variables from .env file
load_dotenv()

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')

# Setup Django
django.setup()

# Import Django models after setup
from orm.db.models import Club, Player

# Get base path for saving club images from environment variables
base_path = os.getenv('base_path_club')


def fetch_content(url, retries=3, timeout=10):
    """Fetch content from a given URL with retries on failure."""
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


def parse_club(club):
    """Parse club information from the club's web page."""
    club_id = club.id
    club_link = club.club_link
    response_content = fetch_content(club_link)
    if response_content is None:
        print(f"Failed to fetch {club_link} after retries.")
        return

    soup = BeautifulSoup(response_content, 'html.parser')

    # Get club description
    descr_tag = soup.find('div', class_="descr")
    descr = descr_tag.text if descr_tag else ""

    # Get country information
    region_tag = soup.find('th', string='Страна')
    if region_tag:
        region_td = region_tag.find_next_sibling('td')
        country_ru = region_td.get_text(strip=True) if region_td else ""
        country_en = GoogleTranslator(source='auto', target='en').translate(country_ru)
    else:
        country_en = "N/A"

    # Get trainer information
    trener_tag = soup.find('th', string='Тренер')
    if trener_tag:
        trener_td = trener_tag.find_next_sibling('td')
        trener_ru = trener_td.get_text(strip=True) if trener_td else ""
        trener_en = GoogleTranslator(source='auto', target='en').translate(trener_ru)
    else:
        trener_en = "N/A"

    print(club.name, club.name_ru, club_link)

    # Fetch club logo
    club_logo_box = soup.find('div', class_="img-box")
    if club_logo_box:
        club_logo = club_logo_box.find('img')['src']
        file_type = club_logo.split('.')[-1]
        logo_response = fetch_content(club_logo)
        if logo_response is None:
            print(f"Failed to fetch logo for {club.name}")
            return

        print(f'{club.name}.{file_type}')

        # Save logo image
        club_path = os.path.join(base_path, club.slug)
        os.makedirs(club_path, exist_ok=True)
        logo_path = os.path.join(club_path, f'{club.name}.{file_type}')
        relative_logo_path = logo_path.replace(base_path, '').replace('\\', '/')
        print(relative_logo_path)

        form_img = os.path.join(os.path.dirname(relative_logo_path), 'App.png').replace('\\', '/')
        print(form_img)

        with open(logo_path, 'wb') as f:
            f.write(logo_response)
        print(f'{club.name} Saved photo! ')

        # Update club information in the database
        club.native = descr
        club.region = country_en
        club.trainer = trener_en
        club.flag_url = relative_logo_path
        club.form_img = form_img
        club.save()
        print(f'Updated: {club.name}')

        # Parse club players
        parse_club_players(club=club)


def get_position_code(player_position):
    """Get position code based on player position name."""
    switcher = {
        'вратарь': 'GOA',
        'защитник': 'DEF',
        'полузащитник': 'MID',
        'нападающий': 'STR',
        None: None
    }
    return switcher.get(player_position, 'None')


def sanitize_filename(filename):
    """Sanitize the filename by replacing invalid characters."""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename


def parse_club_players(club):
    """Parse players from the club's team page."""
    url = f'https://www.sports.ru/football/club/{club.slug}/team/'
    response_content = fetch_content(url)
    if response_content is None:
        print(f"Failed to fetch {url} after retries.")
        return

    soup = BeautifulSoup(response_content, 'html.parser')
    table = soup.find('div', class_='stat mB15')
    if table is None:
        print(f"No table found for {club.name}")
        return

    table_body = table.find('tbody')
    if table_body is None:
        print(f"No tbody found for {club.name}")
        return

    table_row = table_body.find_all('tr')
    if not table_row:
        print(f"No table rows found for {club.name}")
        return

    i = 0
    for row in table_row:
        name_ru = row.find('a').get_text()
        player_link = row.find('a')['href']
        slug = player_link.split('/')[-2]

        name = GoogleTranslator(source='auto', target='en').translate(name_ru)
        number = row.find('td').get_text(strip=True) or '0'
        player_position = row.find_all('td')[-1].get_text(strip=True)
        position_code = get_position_code(player_position)

        # Fetch player details
        club_response_content = fetch_content(player_link)
        if club_response_content is None:
            print(f"Failed to fetch {player_link} after retries.")
            continue

        club_soup = BeautifulSoup(club_response_content, 'html.parser')
        descr = club_soup.find('div', class_="descr").text

        # Fetch player logo
        club_logo_box = club_soup.find('div', class_="img-box")
        if club_logo_box is None:
            print(f"No logo box found for {name}")
            continue

        club_logo = club_logo_box.find('img')['src']
        if not club_logo:
            print(f"No logo found for {name}")
            continue

        logo_response_content = fetch_content(club_logo)
        if logo_response_content is None:
            print(f"Failed to fetch logo for {name}")
            continue

        file_type = club_logo.split('.')[-1]
        sanitized_name = sanitize_filename(name)
        club_path = os.path.join(base_path, slug)
        os.makedirs(club_path, exist_ok=True)

        logo_path = os.path.join(club_path, f'{sanitized_name}.{file_type}')
        relative_logo_path = logo_path.replace(base_path, '').replace('\\', '/')

        # Save player logo image
        with open(logo_path, 'wb') as f:
            f.write(logo_response_content)
        print(f'{name} Saved photo! ')

        # Save player data to the database
        try:
            Player.objects.get(name=name)
            print(f'Already Exists: {name} with Player_link: {player_link}')
        except Player.DoesNotExist:
            Player.objects.create(
                name=name,
                slug=slug,
                shirt_number=number,
                image=relative_logo_path,
                club_id=club.id,
                position=position_code,
                name_ru=name_ru,
                player_link=player_link,
                native=descr,
                competition_id=club.competition_id
            )
            i += 1
            print(i, 'created: ', name)

    print(f"\n{club.name} with Player_link: {player_link} Players parsing finished ")


@click.command()
@click.argument('club_id')
def main(club_id):
    """Main function to parse club information and players."""
    try:
        club = Club.objects.get(id=club_id)
        parse_club(club)
    except Club.DoesNotExist:
        print(f"Club with id {club_id} does not exist.")


if __name__ == "__main__":
    main()