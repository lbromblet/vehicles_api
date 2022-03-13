import os
from datetime import timedelta
from dotenv import load_dotenv

# Load enviroments variables

load_dotenv()


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ['*']


# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY')


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('MAIN_DATABASE_NAME'),
        'USER': os.environ.get('MAIN_DATABASE_USER'),
        'PASSWORD': os.environ.get('MAIN_DATABASE_PASSWORD'),
        'HOST': os.environ.get('MAIN_DATABASE_HOST'),
        'PORT': os.environ.get('MAIN_DATABASE_PORT'),
    }
}


# Application settings

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = []

ACCESS_TOKEN_LIFETIME = timedelta(minutes=5)
REFRESH_TOKEN_LIFETIME = timedelta(days=90)
SLIDING_TOKEN_LIFETIME = timedelta(minutes=5)
SLIDING_TOKEN_REFRESH_LIFETIME = timedelta(days=1)
