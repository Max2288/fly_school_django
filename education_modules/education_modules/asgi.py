"""ASGI config for education_modules project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'education_modules.settings')

application = get_asgi_application()
