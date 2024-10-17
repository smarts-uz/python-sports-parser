# orm/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

# DJANGO_SETTINGS_MODULE'ni to'g'ri yuklayapmizmi?
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')

application = get_wsgi_application()