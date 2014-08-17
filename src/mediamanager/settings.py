"""
Django settings for mediamanager project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/

TODO list is available here:
https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
"""

import os


# ================================================================================
# Project path
# ================================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ================================================================================
# Local settings
# ================================================================================

from .settings_local import *


# ================================================================================
# Django applications / middlewares
# ================================================================================

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.lib',
    'apps.repository',
    'apps.system',
) + ADDITIONAL_INSTALLED_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mediamanager.urls'
WSGI_APPLICATION = 'mediamanager.wsgi.application'


# ================================================================================
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
# ================================================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# ================================================================================
# Common static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# ================================================================================

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static-dev'),
)


# ================================================================================
# Common template files
# ================================================================================

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
