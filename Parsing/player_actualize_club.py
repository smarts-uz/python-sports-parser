import os
import django
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# .env fayldan ma'lumotlarni yuklash
load_dotenv()

# Django sozlamalarini yuklash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
django.setup()

from orm.db.models import Player, Club  # Import after setup
#
# # Kontent olish va qayta urinib ko'rish funksiyasi
# def fetch_content(url, retries=3, timeout=10):
#     for attempt in range(retries):
#         try:
#             response = requests.get(url, timeout=timeout)
#             response.raise_for_status()  # HTTP xatolarini ko'rsatadi
#             return response.content
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching {url}: {e}")
#             if attempt < retries - 1:
#                 print(f"Retrying ({attempt + 1}/{retries})...")
#     return None
#
# # Club ma'lumotini tekshirish funksiyasi
# def get_club_id_from_link(club_link):
#     try:
#         club = Club.objects.get(club_link=club_link)
#         return club.id
#     except Club.DoesNotExist:
#         print(f"No club found for link: {club_link}")
#         return None
#
# # Ma'lumotlarni olish va saqlash jarayoni
# clubs = Club.objects.all()
# for club in clubs:
#     print(f"Processing club: {club.name}")
#     url = f'https://www.sports.ru/football/club/{club.slug}/team/'
#     response_content = fetch_content(url)
#     if not response_content:
#         print(f"Failed to fetch {url} after retries.")
#         continue
#
#     soup = BeautifulSoup(response_content, 'html.parser')
#
#     # O'yinchilar ro'yxatini olish
#     rows = soup.find_all('div', class_='player-row')  # O'yinchilarni belgilovchi div'larni toping
#
#     if not rows:
#         print(f"No players found for club: {club.name}")
#         continue
#
#     # O'yinchilarni yangilash va klub HTML kodini saqlash
#     for row in rows:
#         name_tag = row.find('a')
#         if not name_tag:
#             continue
#
#         player_link = name_tag['href']
#         player_name = name_tag.get_text(strip=True)
#
#         # O'yinchining profili sahifasini yuklab olish
#         player_response_content = fetch_content(player_link)
#         if not player_response_content:
#             print(f"Failed to fetch player profile: {player_link}")
#             continue
#
#         player_soup = BeautifulSoup(player_response_content, 'html.parser')
#
#         # Klub haqidagi ma'lumotlarni olish
#         club_row = player_soup.find('table', class_='profile-table').find_all('tr')[2]  # 3-qatorda klub bor
#         club_data = club_row.find('td')
#         club_link_tag = club_data.find('a')
#
#         if club_link_tag:
#             club_link = club_link_tag['href']  # Klubning havolasini olish
#             club_name = club_link_tag.get_text(strip=True)  # Klub nomini olish
#         else:
#             club_link = None
#
#         # Club ID ni olish
#         club_id_value = None
#         if club_link:
#             club_id_value = get_club_id_from_link(club_link)
#
#         # O'yinchining club_id va is_actualized ni yangilash
#         if player_link:
#             try:
#                 player = Player.objects.get(player_link=player_link)
#                 player.club_id = club_id_value  # Agar klub topilgan bo'lsa, club_id ni yangilash
#                 player.is_actualized = (club_id_value is not None)  # True agar club_id mavjud bo'lsa
#
#                 player.save()  # O'yinchini saqlash
#                 if club_id_value:
#                     print(f"Updated player: {player_name} with club_id: {club_id_value}")
#                 else:
#                     print(f"No matching club found for player: {player_name}, club_id set to None")
#             except Player.DoesNotExist:
#                 print(f"No matching player found for: {player_name}")

# club_links=Club.objects.all()
#
# for club in club_links:
#     if club.club_link==:
import requests
from bs4 import BeautifulSoup
from time import sleep
# from yourapp.models import Player  # O'z modelingizga mos ravishda yo'lni yangilang

def get_club_link(player_url):
    """
    Berilgan o'yinchi URL orqali o'yinchining klub linkini qaytaradi.

    Args:
        player_url (str): O'yinchi sahifasining URL manzili.

    Returns:
        tuple: Klub URL manzili va klub nomi, yoki (None, None).
    """
    try:
        # O'yinchi sahifasiga HTTP so'rovini yuborish
        response = requests.get(player_url)
        response.raise_for_status()  # So'rov muvaffaqiyatli bo'lganini tekshirish

        # HTML ni tahlil qilish
        soup = BeautifulSoup(response.text, 'html.parser')

        # 'td' taglarini topish
        td_tags = soup.find_all('td')  # Barcha 'td' teglarini olish

        for td in td_tags:
            # Klub linkini topish
            club_link_tag = td.find('a', href=True)  # 'a' tegini topish
            if club_link_tag:
                club_url = club_link_tag['href']  # Klub linkini olish
                club_name = club_link_tag.text.strip()  # Klub nomini olish
                return club_url, club_name  # URL va klub nomini qaytarish

        return None, None

    except requests.exceptions.RequestException as e:
        print(f"HTTP xatosi: {e}")
        return None, None
    except Exception as e:
        print(f"Xato: {e}")
        return None, None

def update_player_club_id(player_url, club_url):
    try:
        # O'yinchini topish
        player = Player.objects.get(player_link=player_url)

        if club_url:
            # Klub URL'ni Club jadvalidagi club_link bilan solishtirish
            try:
                club = Club.objects.get(club_link=club_url)  # Klubni topish

                # Agar klub topilsa, o'yinchining club_id ni yangilash
                player.club_id = club.id
                player.save()  # O'zgarishlarni saqlash
                print(f"O'yinchi: {player.name}, Club ID yangilandi: {club.id}  with {player_url}")

            except Club.DoesNotExist:
                # Agar klub topilmasa, club_id ni null qilish
                # player.club_id = 0
                player.save()  # O'zgarishlarni saqlash
                print(f"Klub topilmadi: {club_url}, club_id null qilindi.with {player_url}")

        else:
            # Agar club_url topilmasa, club_id ni null qilish
            player.club_id = None
            player.save()
            print(f"Klub URL topilmadi, club_id null qilindi: {player_url}")

    except Player.DoesNotExist:
        print(f"O'yinchi topilmadi: {player_url}")
    except Exception as e:
        print(f"Xato: {e}")

# Barcha o'yinchilarni olish
player_links = Player.objects.all()
for player in player_links:
    player_link1 = player.player_link  # O'yinchi linkini olish
    club_url, club_name = get_club_link(player_link1)
    update_player_club_id(player_link1, club_url)
    if club_url:
        print(f"O'yinchining klub sahifasining linki: {club_url}")
        print(f"O'yinchining klubi: {club_name}")
    else:
        # player.club_id = 0
        print("Klub linki topilmadi.")

    sleep(1)  # Har bir so'rov orasida 1 soniya kutish


