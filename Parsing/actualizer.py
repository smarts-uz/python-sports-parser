import os
import django
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from time import sleep
# .env fayldan ma'lumotlarni yuklash
load_dotenv()

# Django sozlamalarini yuklash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
django.setup()

from orm.db.models import Player, Club  # Import after setup
import requests
from bs4 import BeautifulSoup
from time import sleep

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

            club = Club.objects.get(club_link=club_url)  # Klubni topish

                # Agar klub topilsa, o'yinchining club_id ni yangilash
            player.club_id = club.id
            player.is_actualized = True  # is_actualized ni True ga o'zgartirish
            player.save()  # O'zgarishlarni saqlash
            print(f"O'yinchi: {player.name}, Club ID yangilandi: {club.id}  with {player_url}")

            # except Club.DoesNotExist:
            #     # Agar klub topilmasa, club_id ni null qilish
            #     player.club_id = None
            #     player.is_actualized = False
            #     player.save()  # O'zgarishlarni saqlash
            #     print(f"Klub topilmadi: {club_url}, club_id null qilindi.with {player_url}")

        else:
            # Agar club_url topilmasa, club_id ni null qilish
            player.club_id = None
            player.is_actualized = False

            player.save()
            print(f"Klub URL topilmadi, club_id null qilindi: {player_url}")

    except Player.DoesNotExist:
        print(f"O'yinchi topilmadi: {player_url}")
    except Exception as e:
        print(f"Xato: {e}")

# Barcha o'yinchilarni olish
player_links = Player.objects.filter(is_actualized__isnull=True) | Player.objects.filter(is_actualized=False)
for player in player_links:
    player_link1 = player.player_link  # O'yinchi linkini olish
    club_url, club_name = get_club_link(player_link1)
    update_player_club_id(player_link1, club_url)
    if club_url:
        print(f"O'yinchining klub sahifasining linki: {club_url}")
        print(f"O'yinchining klubi: {club_name}")
    else:
        print("Klub linki topilmadi.")

    sleep(1)  # Har bir so'rov orasida 1 soniya kutish