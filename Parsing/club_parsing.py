import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from deep_translator import GoogleTranslator
import os
import django

# Load environment variables from .env file
load_dotenv()

# Set the Django settings module environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')

# Initialize Django
django.setup()

# Now you can import Django models
from orm.db.models import Club, Competition

# Function to fetch content with retries
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

# Function to update or create a Club instance
def update_or_create_club(name, **fields):
    clubs = Club.objects.filter(name=name)
    if clubs.count() > 1:
        print(f"Multiple clubs found with name '{name}'. Manual review needed.")
        return None, None

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

# Main logic for parsing clubs
def parse_clubs_for_competition(competition):
    url = f'https://www.sports.ru/football/tournament/{competition.slug}/table/'
    response_content = fetch_content(url)
    if response_content is None:
        print(f"Failed to fetch {url} after retries.")
        return

    soup = BeautifulSoup(response_content, 'html.parser')
    table = soup.find('div', class_='stat mB6')
    if not table:
        print(f"No table found for competition {competition.slug}.")
        return

    table_body = table.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        name_tag = row.find('a', class_="name")
        if not name_tag:
            continue

        name_ru = name_tag['title']
        name_en = GoogleTranslator(source='auto', target='en').translate(name_ru)
        club_link = name_tag['href']
        slug = club_link.split('/')[-2]

        # Fetch and process club details
        club_response = fetch_content(club_link)
        if club_response is None:
            print(f"Failed to fetch {club_link} after retries.")
            continue

        club_soup = BeautifulSoup(club_response, 'html.parser')
        descr_tag = club_soup.find('div', class_="descr")
        descr = descr_tag.text if descr_tag else ""

        region_tag = club_soup.find('th', string='Страна')
        country_ru = region_tag.find_next_sibling('td').get_text(strip=True) if region_tag else "N/A"
        country_en = GoogleTranslator(source='auto', target='en').translate(country_ru)

        trener_tag = club_soup.find('th', string='Тренер')
        trener_ru = trener_tag.find_next_sibling('td').get_text(strip=True) if trener_tag else "N/A"
        trener_en = GoogleTranslator(source='auto', target='en').translate(trener_ru)

        club_logo_box = club_soup.find('div', class_="img-box")
        club_logo = club_logo_box.find('img')['src']
        file_type = club_logo.split('.')[-1]
        logo_response = fetch_content(club_logo)
        if logo_response is None:
            print(f"Failed to fetch logo for {name_en} after retries.")
            continue

        # Save logo image
        base_path = os.getenv('base_path_club')
        club_path = os.path.join(base_path, slug)
        os.makedirs(club_path, exist_ok=True)
        logo_path = os.path.join(club_path, f'{name_en}.{file_type}')
        relative_logo_path = logo_path.replace(os.getenv('base_path_club'), '').replace('\\', '/')

        with open(logo_path, 'wb') as f:
            f.write(logo_response)

        # Update or create Club instance
        club, created = update_or_create_club(
            name=name_en,
            flag_url=relative_logo_path,
            country_id=competition.country_id,
            name_ru=name_ru,
            club_link=club_link,
            slug=slug,
            native=descr,
            region=country_en,
            trainer=trener_en,
            competition_id=competition.id
        )

        if club:  # Check if club instance was created or updated
            if created:
                print(f'{name_en} created successfully. Club ID: {club.id}, Club Link: {club_link}')
            else:
                print(f'{name_en} updated successfully. Club ID: {club.id}, Club Link: {club_link}')

# Main function to loop through competitions
def main():
    competitions = Competition.objects.all()
    for competition in competitions:
        parse_clubs_for_competition(competition)

if __name__ == "__main__":
    main()