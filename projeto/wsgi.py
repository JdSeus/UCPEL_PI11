"""
WSGI config for projeto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Setting the environment variable DJANGO_SETTINGS_MODULE to the value of projeto.settings.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

application = get_wsgi_application()
