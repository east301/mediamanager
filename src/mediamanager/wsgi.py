"""
WSGI config for mediamanager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

# ================================================================================
# Sets python path, and change current directory
# ================================================================================

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)


# ================================================================================
# Loads WSGI application
# ================================================================================

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mediamanager.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
