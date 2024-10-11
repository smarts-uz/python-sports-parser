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
base_path = os.getenv('base_path_player')

from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from orm.db.models import Player
from orm.db.models import Club



