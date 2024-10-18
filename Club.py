import os
import click
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import django
import subprocess
from deep_translator import GoogleTranslator

# .env faylidan yuklang
load_dotenv()

# Django maxsus sozlamalari
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
django.setup()

from orm.db.models import Competition, Club  # Club modelini import qildik

def download_and_save_club_htmls(competition_id):
    try:
        # Musobaqani olish
        competition = Competition.objects.get(id=competition_id)
        competition_link = competition.competition_link + "table/"
        print(f"Found competition: {competition.name} with link: {competition_link}")

        # Musobaqa sahifasini ochish
        response = requests.get(competition_link)

        if response.ok:
            soup = BeautifulSoup(response.content, 'html.parser')
            clubs = soup.find_all('tr')  # Barcha jadvallardagi satrlar

            base_path_html = os.getenv('base_path_club')

            for club in clubs:
                link_tag = club.find('a')
                if link_tag:
                    club_name = link_tag.text.strip()
                    club_slug = link_tag['href'].split('/')[-2]
                    club_link = link_tag['href']

                    try:
                        club_name_en = GoogleTranslator(source='auto', target='en').translate(club_name)
                    except Exception as e:
                        print(f"Error translating club name '{club_name}': {e}")
                        club_name_en = club_name

                    club_folder_path = os.path.join(base_path_html, club_slug)
                    os.makedirs(club_folder_path, exist_ok=True)
                    html_file_path = os.path.join(club_folder_path, f"{club_name_en}.html")

                    if os.path.exists(html_file_path):
                        print(f"HTML for {club_name_en} already exists: {html_file_path} skip...")
                    else:
                        print(f"Saving HTML for {club_name_en}...")
                        try:
                            subprocess.run(["monolith", club_link, "-o", html_file_path], check=True)
                            print(f"HTML saved for {club_name_en}: {html_file_path}")
                        except subprocess.CalledProcessError as e:
                            print(f"Failed to save HTML for {club_name_en}: {e}")

                    # Klub HTML faylini parsing qilish
                    with open(html_file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        parse_club_html(content, competition_id)  # 2 ta argument berilishi kerak

        else:
            print("Competition page could not be retrieved.")

    except Competition.DoesNotExist:
        print(f"Competition with id {competition_id} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def parse_club_html(response_content, competition_id):
    """Klub HTML faylini parsing qilish va ma'lumotlarni bazaga saqlash"""
    try:
        soup = BeautifulSoup(response_content, 'html.parser')
        table = soup.find('div', class_='stat mB6')

        if table is None:
            print("Statistics section not found. Check HTML structure.")
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
            club_response = requests.get(club_link)
            if not club_response.ok:
                print(f"Failed to retrieve club details from {club_link}.")
                continue

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
            club_logo = club_logo_box.find('img')['src'] if club_logo_box else None

            if club_logo:
                logo_response = requests.get(club_logo).content
                base_path = os.getenv('base_path_club')
                club_path = os.path.join(base_path, slug)
                os.makedirs(club_path, exist_ok=True)
                file_type = club_logo.split('.')[-1]
                logo_path = os.path.join(club_path, f'{name_en}.{file_type}')

                if logo_response:
                    with open(logo_path, 'wb') as f:
                        f.write(logo_response)
                else:
                    print(f"Failed to retrieve logo for {name_en}.")

            # Klubni bazaga qo'shish
            if not Club.objects.filter(slug=slug, competition_id=competition_id).exists():
                Club.objects.create(
                    name=name_en,
                    name_ru=name_ru,
                    club_link=club_link,
                    country_id=country_en,
                    slug=slug,
                    region=country_en,
                    trainer=trener_en,
                    flag_url=club_logo,
                    html_paths=logo_path,  # Olingan HTML fayl yo'lini saqlash
                )
                print(f"Club {name_en} added to the database.")
            else:
                print(f"Club {name_en} already exists in the database.")

    except Exception as e:
        print(f"An error occurred while parsing the club HTML: {e}")

@click.command()
@click.argument('competition_id', type=int)
def competition(competition_id):
    download_and_save_club_htmls(competition_id)

if __name__ == '__main__':
    competition()