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

from orm.db.models import Club
from function.fetch_content import fetch_content


# Function to update the fields of a Club instance
def update_club_instance(club_instance, **fields):
    for field, value in fields.items():
        setattr(club_instance, field, value)
    club_instance.save()


# Main parsing logic
def club_parse(competition_id):
    clubs = Club.objects.filter(competition_id=competition_id)
    if not clubs.exists():
        print(f"No clubs found for competition ID {competition_id}.")
        return

    for club in clubs:
        club_link = club.club_link
        if not club_link:
            print(f"No club link found for club '{club.name}'. Skipping.")
            continue

        response_content = fetch_content(club_link)
        if response_content is None:
            print(f"Failed to fetch content for {club_link} after retries.")
            continue

        soup = BeautifulSoup(response_content, 'html.parser')


        # Find the club name in the <h1> tag
        name_tag = soup.find('h1')
        if not name_tag:
            print("Club name not found in the expected <h1> tag.")
            return None, None

        # Extract and translate the name
        name_ru = name_tag.text.strip()
        name_en = GoogleTranslator(source='auto', target='en').translate(name_ru)

        # Fetch club details
        descr_tag = soup.find('div', class_="descr")
        descr = descr_tag.text if descr_tag else ""

        region_tag = soup.find('th', string='Страна')
        country_ru = region_tag.find_next_sibling('td').get_text(strip=True) if region_tag else "N/A"
        country_en = GoogleTranslator(source='auto', target='en').translate(country_ru)

        trener_tag = soup.find('th', string='Тренер')
        trener_ru = trener_tag.find_next_sibling('td').get_text(strip=True) if trener_tag else "N/A"
        trener_en = GoogleTranslator(source='auto', target='en').translate(trener_ru)

        # Handle club logo
        club_logo_box = soup.find('div', class_="img-box")
        logo_path, form_img = "", ""
        if club_logo_box:
            club_logo = club_logo_box.find('img')['src']
            file_type = club_logo.split('.')[-1]
            logo_response = fetch_content(club_logo)

            # Save logo image
            base_path = os.getenv('base_path_club')
            club_path = os.path.join(base_path, club.slug)
            os.makedirs(club_path, exist_ok=True)
            file_name = f'logo.{file_type}'
            file_path = os.path.join(club_path, file_name)

            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(logo_response)
                print(f'Image for {club.name} saved in {file_path}')
            else:
                print(f'Image for {club.name} already exists in {file_path}')

            logo_path = f'club\\{club.slug}\\logo.{file_type}'
            form_img = f'club\\{club.slug}\\app.png'

        # Update Club instance with specific fields
        update_club_instance(
            club,
            name=name_en,
            competition_name=club.competition_name,
            logo_img=logo_path,
            country_id=club.country_id,
            name_ru=name_ru,
            club_link=club_link,
            slug=club.slug,
            native=descr,
            region=country_en,
            trainer=trener_en,
            competition_id=club.competition_id,
            form_img=form_img,
            created_at=timezone.now(),
            updated_at=timezone.now(),
        )
        print(f"Updated club {club.name} with ID {club.id} from link: {club_link}")


# Run the parsing function for a specific competition ID
club_parse(competition_id=2)  # Replace with the desired competition ID