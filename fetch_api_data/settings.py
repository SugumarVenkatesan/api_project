"""
Django settings for fetch_api_data project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sgmfhp#+k1y!t_&h!h4h1tf5+tgavaxo!$z=seoa0%xl0d_dw)'
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost','pysuguvenk.pythonanywhere.com']

APPEND_SLASH = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'f1_api_app',
    'sound_cloud_api_app',
    'identity_app',
    'djangular',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)



ROOT_URLCONF = 'fetch_api_data.urls'

WSGI_APPLICATION = 'fetch_api_data.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
import socket
if socket.gethostname().__contains__('tringapps'):
    DOMAIN_URL = 'http://127.0.0.1:8000'
    DATABASES = {
        'default': {
            # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or
            # 'oracle'.
            'ENGINE': 'django.db.backends.mysql',
            # Or path to database file if using sqlite3.
            'NAME': 'Identity',
            'USER': 'root',                      # Not used with sqlite3.
            'PASSWORD': 'root',                  # Not used with sqlite3.
            # Set to empty string for localhost. Not used with sqlite3.
            'HOST': '',
            # Set to empty string for default. Not used with sqlite3.         # set
            # the connection timeout for
            'PORT': '',
        }
    }
else:
    DOMAIN_URL = 'http://pysuguvenk.pythonanywhere.com'
    DATABASES = {
        'default': {
            # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or
            # 'oracle'.
            'ENGINE': 'django.db.backends.mysql',
            # Or path to database file if using sqlite3.
            'NAME': 'pysuguvenk$Identity',
            'USER': 'pysuguvenk',                      # Not used with sqlite3.
            'PORT': '',
            'PASSWORD': 'root',                  # Not used with sqlite3.
            # Set to empty string for localhost. Not used with sqlite3.
            'HOST': 'pysuguvenk.mysql.pythonanywhere-services.com',
            # Set to empty string for default. Not used with sqlite3.         # set
            # the connection timeout for
        }
    }
 


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "mystatic")

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'f1_api_app', 'templates'),
    os.path.join(BASE_DIR, 'identity_app', 'templates'),
    os.path.join(BASE_DIR, 'templates'),
)

STATICFILES_DIRS = (
                    os.path.join(BASE_DIR, 'f1_api_app','static'),
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

import base64
secret_key = os.environ.get('some_secret_key','None') + '_' + base64.b64decode('')

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = secret_key.split('_')[1]
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

USER_ACTIVATION_MAIL_EXPIRY_PERIOD = 2
