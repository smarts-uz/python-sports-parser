############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """


# Seed a few users in the database
# pl = Player.objects.get(id=6)
# pl.name = 'SportsruTEst'
# pl.save()
# print(pl.name)


# a = Player.objects.all().order_by('id')
# for player in a:
#     print(player.name)



