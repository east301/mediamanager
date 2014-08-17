"""
Django settings for mediamanager project.
"""

import os


# ================================================================================
# Project path
# ================================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ================================================================================
# Secret key
# ================================================================================

SECRET_KEY = 'd#krurndyx9^rq^nv#cry0*45gd9^q#88$5b$yoz=@q2z5s#)*'


# ================================================================================
# Debug flag
# ================================================================================

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']


# ================================================================================
# Django applications / middlewares
# ================================================================================

ADDITIONAL_INSTALLED_APPS = (
    'django.contrib.admin',
    'debug_toolbar',
)


# ================================================================================
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# ================================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# ================================================================================
# Cache
# https://docs.djangoproject.com/en/1.6/ref/settings/#caches
# ================================================================================

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


# ================================================================================
# Mail
# https://docs.djangoproject.com/en/1.6/topics/email/
# ================================================================================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
