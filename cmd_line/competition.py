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

from orm.db.models import Competition


def save_club_htmls_by_competition_id(competition_id):
    try:
        # Musobaqani olish
        competition = Competition.objects.get(id=competition_id)
        competition_link = competition.competition_link + "table/"  # Musobaqa havolasini qo'shish
        print(f"Found competition: {competition.name} with link: {competition_link}")

        # Musobaqa sahifasini ochish
        response = requests.get(competition_link)

        # Agar sahifa muvaffaqiyatli ochilgan bo'lsa
        if response.ok:
            # HTML ni olish
            soup = BeautifulSoup(response.content, 'html.parser')

            # Klub ma'lumotlarini olish
            clubs = soup.find_all('tr')  # Barcha jadvallardagi satrlar

            # HTML saqlash uchun bazaviy yo'l
            base_path_html = os.getenv('base_path_club')

            # Har bir klub uchun HTMLni saqlash
            for club in clubs:
                link_tag = club.find('a')
                if link_tag:
                    club_name = link_tag.text.strip()  # Klub nomini olish
                    club_slug = link_tag['href'].split('/')[-2]  # Klub slugini olish
                    club_link = link_tag['href']  # Klub havolasini olish

                    # Klub nomini ingliz tiliga tarjima qilish
                    club_name_en = GoogleTranslator(source='auto', target='en').translate(club_name)


                    # Klub uchun slug bo'yicha papka yaratish
                    club_folder_path = os.path.join(base_path_html, club_slug)
                    os.makedirs(club_folder_path, exist_ok=True)

                    # Klub HTMLsini saqlash
                    html_file_path = os.path.join(club_folder_path,
                                                  f"{club_name_en}.html")  # Tarjima qilingan nomi bilan saqlash

                    if os.path.exists(html_file_path):
                        print(f"HTML for {club_name_en} already exists: {html_file_path} skip...")
                    else:
                        # Monolith yordamida HTML saqlash
                        print(f"Saving HTML for {club_name_en}...")
                        subprocess.run(["monolith", club_link, "-o", html_file_path], check=True)
                        print(f"HTML saved for {club_name_en}: {html_file_path}")

        else:
            print("Competition page could not be retrieved.")

    except Competition.DoesNotExist:
        print(f"Competition with id {competition_id} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

@click.command()
@click.argument('competition_id',type=int)
def competition(competition_id):
    save_club_htmls_by_competition_id(competition_id)

if __name__ == '__main__':
    competition()

