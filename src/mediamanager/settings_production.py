"""
Django settings for mediamanager project.
"""

from __future__ import with_statement

# ================================================================================
# Secret key
# ================================================================================

SECRET_KEY = None


# ================================================================================
# Debug flag
# ================================================================================

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']


# ================================================================================
# Django applications / middlewares
# ================================================================================

ADDITIONAL_INSTALLED_APPS = (
)


# ================================================================================
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# ================================================================================

DATABASES = {
    'default': {
        'ENGINE': None,
        'NAME': None,
        'USER': None,
        'PASSWORD': None,
        'HOST': None,
        'PORT': None,
    }
}


# ================================================================================
# Cache
# https://docs.djangoproject.com/en/1.6/ref/settings/#caches
# ================================================================================

CACHES = {
    'default': {
        'BACKEND': None,
    }
}


# ================================================================================
# Mail
# https://docs.djangoproject.com/en/1.6/topics/email/
# ================================================================================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
