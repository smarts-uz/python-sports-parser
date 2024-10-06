import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django

django.setup()
import requests

load_dotenv()
from orm.db.models import Player
from django.db import models  # models moduli import qilindi
from orm.db.models import Club,Player

# O'yinchilarni bazada takrorlanayotganini tekshirish
duplicate_players = Player.objects.values('slug').annotate(count=models.Count('id')).filter(count__gt=1)

if duplicate_players:
    for player in duplicate_players:
        print(f"Duplicate Player Found: {player['slug']} with count: {player['count']}")
else:
    print("No duplicate players found.")

# duplicate_clubs = Club.objects.values('slug').annotate(count=models.Count('id')).filter(count__gt=1)
#
# if duplicate_clubs:
#     for club in duplicate_clubs:
#         print(f"Duplicate Player Found: {club['slug']} with count: {club['count']}")
# else:
#     print("No duplicate players found.")
