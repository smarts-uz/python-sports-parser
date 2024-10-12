import os
import django
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from deep_translator import GoogleTranslator


# Load environment variables
load_dotenv()

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
django.setup()
from orm.db.models import  Competition
base_path_html = os.getenv('base_path_club')
competition_url=os.getenv('competition_url')
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


# Function to save HTML content to a file
def save_html_to_file(content, file_path):
    if os.path.exists(file_path):
        print(f"File {file_path} already exists, skipping.")
        return
    with open(file_path, 'wb') as f:
        f.write(content)
    print(f"HTML saved to {file_path}")


# Main logic
def main():
    competitions = Competition.objects.all()

    for competition in competitions:
        # Generate URL for the competition table
        url = f'https://www.sports.ru/football/tournament/{competition.slug}/table/'
        response_content = fetch_content(url)
        if response_content is None:
            print(f"Failed to fetch {url} after retries.")
            continue

        soup = BeautifulSoup(response_content, 'html.parser')
        table = soup.find('div', class_='stat mB6')
        if not table:
            print(f"Table not found for {competition.slug}, skipping.")
            continue

        table_body = table.find('tbody')
        table_rows = table_body.find_all('tr')

        for row in table_rows:
            name_tag = row.find('a', class_="name")
            if not name_tag:
                continue

            # Extract club details
            name_ru = name_tag['title']
            name_en = GoogleTranslator(source='auto', target='en').translate(name_ru)
            club_link = name_tag['href']
            slug = club_link.split('/')[-2]

            # Generate file paths for saving the club HTML

            club_html_folder = os.path.join(base_path_html, slug)
            os.makedirs(club_html_folder, exist_ok=True)
            html_file_path = os.path.join(club_html_folder, f"{slug}.html")
            # chekking club html
            if os.path.exists(html_file_path):
                print(f"File {html_file_path} already exists, skipping.")
                continue

            # Fetch and save the club's HTML page
            club_html_content = fetch_content(club_link)
            if club_html_content:
                save_html_to_file(club_html_content, html_file_path)
            else:
                print(f"Failed to fetch HTML for {name_en}, skipping.")


if __name__ == "__main__":
    main()