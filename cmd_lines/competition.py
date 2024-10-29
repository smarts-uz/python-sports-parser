import os
import click
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import django
import  time

from deep_translator import GoogleTranslator
from django.utils import timezone  # timezone ni import qiling
from monolithh.monolith_htmls import html_downloader

# .env faylidan yuklang
load_dotenv()

# Django maxsus sozlamalari
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
django.setup()

from orm.db.models import Competition,Club  # Club modelini import qildik

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

            # Har bir klub uchun HTMLni saqlash va bazaga kiritish
            for club in clubs:
                link_tag = club.find('a')

                if link_tag:
                    club_name = link_tag.text.strip()
                    print(club_name)# Klub nomini olish
                    club_slug = link_tag['href'].split('/')[-2]  # Klub slugini olish
                    club_link = link_tag['href']


                    # Klub havolasini olish

                    # Klub nomini ingliz tiliga tarjima qilish
                    club_name_en = GoogleTranslator(source='auto', target='en').translate(club_name)

                    club = Club.objects.filter(slug=club_slug, competition_id=competition_id).first()
                    if club:
                        # Update club if it exists
                        club.name = club_name_en
                        club.name_ru = club_name
                        # club.club_link = club_link
                        club.updated_at = timezone.now()
                        club.save()
                        print(f"Updated existing Club: {club.name} with ID {club.id} - link {club_link}")
                    else:
                        # Create a new club if not found
                        club = Club.objects.create(
                            name=club_name_en,
                            competition_name=competition.name,
                            slug=club_slug,
                            competition_id=competition_id,
                            name_ru=club_name,
                            club_link=club_link,
                            created_at=timezone.now(),
                        )
                        print(f"Created new Club: {club.name} - link {club_link}")

                    # Klub HTMLsini saqlash
                    club_folder_path = os.path.join(base_path_html, club_slug)
                    os.makedirs(club_folder_path, exist_ok=True)

                    html_file_path = os.path.join(club_folder_path,'app.html')  # Tarjima qilingan nomi bilan saqlash
                    # htmls downloader functions
                    # print(club.club_link)
                    # html_downloader(club_name_en,club.club_link,html_file_path)  #for the competition_id 2
                    html_downloader(club_name_en,club_link, html_file_path)
        else:
            print("Competition page could not be retrieved.")

    except Competition.DoesNotExist:
        print(f"Competition with id {competition_id} does not exist.")
    except Exception as e:

        print(f"An error occurred: {e}")
    time.sleep(1)


