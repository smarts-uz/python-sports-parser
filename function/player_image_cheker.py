import django
import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

# Set the Django settings module environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')

# Initialize Django
django.setup()  # This ensures that all apps and models are loaded

# Import Django models after setting up Django
from orm.db.models import Player
base_path_player = os.getenv('base_path_player')

def get_player_image_url(player_page_url):
    try:
        # Sahifani yuklab olamiz
        response = requests.get(player_page_url)
        response.raise_for_status()

        # Sahifani parslash uchun BeautifulSoup dan foydalanamiz
        soup = BeautifulSoup(response.content, 'html.parser')

        # Sahifadagi rasmni <img> tegi ichidan qidiramiz, masalan, alt atributiga qarab
        image_tag = soup.find('img', alt=True)  # Sahifada alt atributiga ega bo'lgan rasmni olamiz
        if image_tag and 'src' in image_tag.attrs:
            # Rasm URL'sini qaytaramiz
            return image_tag['src']
        else:
            print("Image not found on the player page.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching player page: {e}")
        return None


def download_player_image(player_image_url, player_name, player_slug, base_path_player):
    try:
        # Rasmni yuklab olish
        response = requests.get(player_image_url)
        response.raise_for_status()

        # URL dan fayl kengaytmasini olish (masalan: .png, .jpg)
        parsed_url = urlparse(player_image_url)
        file_extension = os.path.splitext(parsed_url.path)[1]  # Fayl kengaytmasini olamiz

        # Fayl nomini futbolchining to'liq ismi bo'yicha yaratamiz
        file_name = f"app{file_extension}"  # Fayl nomi: "Arsen_Zakharyan.png"

        # Rasmni saqlash uchun slug nomiga asoslangan papkani yaratamiz
        player_folder = os.path.join(base_path_player, player_slug)

        os.makedirs(player_folder, exist_ok=True)
        full_image_path = os.path.join(player_folder, file_name)
        if os.path.exists(full_image_path):
            print(f"Image {file_name} already downloaded at this path: {full_image_path}")

        else:
            # Rasm faylini saqlash
            with open(full_image_path, 'wb') as file:
                file.write(response.content)

            print(f"Image successfully downloaded: {full_image_path}")

        # Nisbiy manzilni yaratamiz
        relative_image_path = os.path.join('player', player_slug, file_name)

        print(f"Relative image path: {relative_image_path}")
        return relative_image_path

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return None

def create_player_image(player):
    # Rasm manzilini sahifadan olamiz
    player_image_url = get_player_image_url(player.player_link)

    # Agar rasm manzili mavjud bo'lsa, rasmni yuklab olamiz
    if player_image_url:
        image_path = download_player_image(player_image_url, player.name, player.slug, base_path_player)

        # Rasmni saqlagandan keyin playerning image maydoniga rasm manzilini yozamiz
        if image_path:
            player.image = image_path
            player.save()
            print(f"Player image created: {player.name} with player_image: {player.image}")
    else:
        print(f"Image not found for player: {player.name} (Club ID: {player.club_id}) with link {player.player_link}")


def update_players_images_by_competition(competition_id):
    players = Player.objects.filter(competition_id=competition_id)

    if not players.exists():
        print(f"No players found for competition ID: {competition_id}")
        return

    for player in players:
        create_player_image(player)
        print(f"Processed image for player: {player.name}")


