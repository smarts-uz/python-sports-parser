import os
import requests
from bs4 import BeautifulSoup
from click import command
from dotenv import load_dotenv
import subprocess

from django.utils import timezone

from parsing_comp_id import base_path_club

load_dotenv()
# Django specific settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django

django.setup()



from orm.db.models import Club

clubs=Club.objects.all()
i=0
for club in clubs:
    i+=1
    # print(f"{club.name}:{club.club_link}")


def html_run():
    for club in clubs:
        print(f"{club.name}: {club.club_link}")

        # Build the path using os.path.join for cross-platform compatibility
        path = os.path.join(os.getenv('base_path_club'), club.name)

        try:
            # Create the directory if it doesn't exist
            os.makedirs(path, exist_ok=True)  # 'exist_ok=True' will not raise an error if the folder exists
            print(f"Saving to directory: '{path}'")

            # Run the 'monolith' command to save the webpage as HTML
            command = ['monolith', club.club_link, '-o', os.path.join(path, f'{club.name}.html')]
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

            stdout, stderr = process.communicate()  # Get output and errors (if any)
            if process.returncode == 0:
                print(f"'{club.name}.html' saved successfully in '{path}'.")
            else:
                print(f"Error saving '{club.name}.html': {stderr}")

        except PermissionError:
            print(f"Permission denied: Unable to save in '{path}'.")
        except Exception as e:
            print(f"An error occurred: {e}")


html_run()





# execute=subprocess.Popen(
#     [f'D:\Python projects\monolith.exe' ]
#
# )





