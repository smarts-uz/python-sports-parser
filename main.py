import os
import click
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import django
import subprocess
from deep_translator import GoogleTranslator
from django.utils import timezone  # timezone ni import qiling

# .env faylidan yuklang
load_dotenv()

# Django maxsus sozlamalari
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
django.setup()

from orm.db.models import Competition, Club  # Club modelini import qildik

# Calling cmd functions
from cmd_lines.competition import save_club_htmls_by_competition_id
from cmd_lines.Club import club_parse
from cmd_lines.players_main import parse_players

@click.group()
def main():
    pass
#working with click cmd line arguments
# Competition command with competition id
@click.command()
@click.argument('competition_id', type=int)
def competition(competition_id):
    """Parses clubs and saves HTML by competition ID."""
    save_club_htmls_by_competition_id(competition_id)
    print(f"Clubs saved for competition ID: {competition_id}")


# Club parsing command
@click.command()
@click.argument('competition_id', type=int)
def club(competition_id):
    """Parses players from clubs for the given competition ID."""
    club_parse(competition_id)
    print(f"Club parsing completed for competition ID: {competition_id}")

# Player parsing command
@click.command()
@click.argument('competition_id', type=int)
def player(competition_id):
    parse_players(competition_id)
    print(f"Players parsed for competition ID: {competition_id}")

# Adding commands to the main group
main.add_command(competition)
main.add_command(club)
main.add_command(player)

if __name__ == '__main__':
    main()
