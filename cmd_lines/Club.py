import os
import django
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from deep_translator import GoogleTranslator
from django.utils import timezone


# Load environment variables
load_dotenv()

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
django.setup()

# Function to fetch content with retries
from orm.db.models import Club, Competition
from function.fetch_content import fetch_content
# Function to update or create a Club instance
def update_or_create_club(name,slug,competition_id, **fields):
    clubs = Club.objects.filter(name=name,slug=slug,competition_id=competition_id)
    if clubs.count() > 1:
        print(f"Multiple clubs found with name '{name}'. Manual review needed.")
        return

    if clubs.exists():
        club = clubs.first()
        for field, value in fields.items():
            setattr(club, field, value)
        club.save()
        created = False
    else:
        club = Club.objects.create(name=name,slug=slug,competition_id=competition_id)
        created = True

    return club, created

# Main logic
def club_parse(competition_id):
    competition = Competition.objects.filter(id=competition_id).first()
    if not competition:
        print(f"Competition with ID {competition_id} not found.")
        return

    url = f'https://www.sports.ru/football/tournament/{competition.slug}/table/'
    response_content = fetch_content(url)
    if response_content is None:
        print(f"Failed to fetch {url} after retries.")
        return

    soup = BeautifulSoup(response_content, 'html.parser')
    table = soup.find('div', class_='stat mB6')
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
        club_response = requests.get(club_link)
        club_soup = BeautifulSoup(club_response.content, 'html.parser')

        descr_tag = club_soup.find('div', class_="descr")
        descr = descr_tag.text if descr_tag else ""

        region_tag = club_soup.find('th', string='Страна')
        country_ru = region_tag.find_next_sibling('td').get_text(strip=True) if region_tag else "N/A"
        country_en = GoogleTranslator(source='auto', target='en').translate(country_ru)

        trener_tag = club_soup.find('th', string='Тренер')
        trener_ru = trener_tag.find_next_sibling('td').get_text(strip=True) if trener_tag else "N/A"
        trener_en = GoogleTranslator(source='auto', target='en').translate(trener_ru)

        club_logo_box = club_soup.find('div', class_="img-box")
        if club_logo_box:
            club_logo = club_logo_box.find('img')['src']
            file_type = club_logo.split('.')[-1]
            logo_response = fetch_content(club_logo)

            # Save logo image
            base_path = os.getenv('base_path_club')
            club_path = os.path.join(base_path, slug)
            os.makedirs(club_path, exist_ok=True)
            file_name = f'logo.{file_type}'
            file_path = os.path.join(club_path, file_name)
            if os.path.exists(file_path):
                print(f'Image for {name_en} already exists in relative_path:{file_path}')
            else:
                with open(file_path, 'wb') as f:
                    f.write(logo_response)
                print(f'Image for {name_en} saved in {file_path}')


            logo_path = os.path.join( f'club\\{slug}\\logo.{file_type}')
            print(logo_path)

            form_img = os.path.join(f'club\\{slug}\\app.png')

            print(form_img)



        # Update or create Club instance
        club, created = update_or_create_club(
            name=name_en,
            competition_name=competition.name,
            logo_img=logo_path,
            country_id=competition.country_id,
            name_ru=name_ru,
            club_link=club_link,
            slug=slug,
            native=descr,
            region=country_en,
            trainer=trener_en,
            competition_id=competition.id,
            form_img=form_img,
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )

        if created:
            print(f'{name_en} created successfully with id-{club.id}-club_link {club_link}')
        else:
            print(f'{name_en} updated successfully with id-{club.id}-club_link {club_link}')
