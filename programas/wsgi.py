"""
WSGI config for programas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from dotenv import load_dotenv
# from pathlib import Path


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programas.settings')

# env_path = Path('.')/'.env'
# load_dotenv(dotenv_path = env_path)

application = get_wsgi_application()
