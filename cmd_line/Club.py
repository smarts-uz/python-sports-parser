import os
import requests
import subprocess
import time
from bs4 import BeautifulSoup
from googletrans import Translator
from dotenv import load_dotenv
import click
import django
# from django.conf import settings

# Load environment variables from .env file
load_dotenv()

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')  # Adjust to your settings module
django.setup()  # Initialize Django

from orm.db.models import Club, Competition  # Model import

# Translator instance
translator = Translator()

# Function to update or create a Club instance
def update_or_create_club(name, **fields):
    clubs = Club.objects.filter(name=name)
    if clubs.count() > 1:
        print(f"Multiple clubs found with name '{name}'. Manual review needed.")
        return None, False

    if clubs.exists():
        club = clubs.first()
        for field, value in fields.items():
            setattr(club, field, value)
        club.save()
        created = False
    else:
        club = Club.objects.create(name=name, **fields)
        created = True

    return club, created

# Function to save HTML and logo
def save_html_and_logo(club_link, club_name_en, slug):
    # HTML file path
    html_file_path = os.path.join(os.getenv('base_path_club'), slug, f'{club_name_en}.html')

    # Check if HTML file already exists
    if os.path.exists(html_file_path):
        print(f'HTML already exists for {club_name_en}. Parsing the existing file...')
        with open(html_file_path, 'r', encoding='utf-8') as file:
            response_content = file.read()
            soup = BeautifulSoup(response_content, 'html.parser')
    else:
        # Save HTML using Monolith
        print(f"Saving HTML for {club_name_en}...")
        subprocess.run(["monolith", club_link, "-o", html_file_path], check=True)
        print(f"HTML saved for {club_name_en}: {html_file_path}")
        with open(html_file_path, 'r', encoding='utf-8') as file:
            response_content = file.read()
            soup = BeautifulSoup(response_content, 'html.parser')

    # Extract club details
    table = soup.find('div', class_='stat mB6')
    if table:
        table_body = table.find('tbody')
        table_rows = table_body.find_all('tr')

        for row in table_rows:
            name_tag = row.find('a', class_="name")
            if not name_tag:
                continue

            name_ru = name_tag['title']
            name_en = translator.translate(name_ru, dest='en').text  # Translate to English
            club_link = name_tag['href']
            slug = club_link.split('/')[-2]

            # Fetch and process club details
            try:
                club_soup = BeautifulSoup(requests.get(club_link).content, 'html.parser')
                time.sleep(1)  # Pause for 1 second

                descr_tag = club_soup.find('div', class_="descr")
                descr = descr_tag.text if descr_tag else ""

                region_tag = club_soup.find('th', string='Страна')
                country_ru = region_tag.find_next_sibling('td').get_text(strip=True) if region_tag else "N/A"
                country_en = translator.translate(country_ru, dest='en').text

                trener_tag = club_soup.find('th', string='Тренер')
                trener_ru = trener_tag.find_next_sibling('td').get_text(strip=True) if trener_tag else "N/A"
                trener_en = translator.translate(trener_ru, dest='en').text

                # Handle club logo
                club_logo_box = club_soup.find('div', class_="img-box")
                if club_logo_box and club_logo_box.find('img'):
                    club_logo = club_logo_box.find('img')['src']
                    file_type = club_logo.split('.')[-1]
                    logo_response = requests.get(club_logo)
                    logo_response.raise_for_status()  # Raises error for 4xx/5xx responses

                    # Save logo image
                    base_path = os.getenv('base_path_club')
                    club_path = os.path.join(base_path, slug)
                    os.makedirs(club_path, exist_ok=True)
                    logo_path = os.path.join(club_path, f'{name_en}.{file_type}')
                    relative_logo_path = logo_path.split(os.getenv('base_path_club'))[-1].replace('\\', '/')

                    with open(logo_path, 'wb') as f:
                        f.write(logo_response.content)

                    # Update or create Club instance with transaction
                    club, created = update_or_create_club(
                        name=name_en,
                        flag_url=relative_logo_path,
                        name_ru=name_ru,
                        club_link=club_link,
                        slug=slug,
                        native=descr,
                        region=country_en,
                        trainer=trener_en,
                        competition_id=Competition.id
                    )

                    if created:
                        print(f'{name_en} created successfully.')
                    else:
                        print(f'{name_en} updated successfully.')

            except requests.RequestException as e:
                print(f"Error fetching club details for {name_en}: {e}")
                continue  # Skip to the next club if there is an error

    return response_content

@click.command()
@click.argument('competition_id', type=int)
def main(competition_id):
    # Select the competition with the given competition_id
    competition = Competition.objects.filter(id=competition_id).first()
    if not competition:
        print(f"Competition with ID {competition_id} not found.")
        return

    url = f'https://www.sports.ru/football/tournament/{competition.slug}/table/'
    response_content = save_html_and_logo(url, competition.name_en, competition.slug)
    if response_content is None:
        print(f"Failed to fetch {url}.")
        return

if __name__ == '__main__':
    main()