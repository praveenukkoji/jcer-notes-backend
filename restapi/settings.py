"""
Django settings for restapi project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
# imports
from pathlib import Path
import os
import django_heroku


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u5jmxnosq%ycv!n68hbg_zhaydh7ed64105e$4y!g#xgueq&!1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# hosts
ALLOWED_HOSTS = ['https://jcer-notes.herokuapp.com','http://jcer-notes.herokuapp.com','https://jcer-notes-website.herokuapp.com', 'http://jcer-notes-website.herokuapp.com']

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = 'SAMEORIGIN'

# If this is used then 'CORS_ORIGIN_WHITELIST' will not have any effect
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = False

# If this is used then not need to use 'CORS_ORIGIN_ALLOW_ALL = True'

UI_URL = 'http://jcer-notes.herokuapp.com'
UI_URL1 = 'https://jcer-notes.herokuapp.com'
UI_URL2 = 'http://jcer-notes-website.herokuapp.com'
UI_URL3 = 'https://jcer-notes-website.herokuapp.com'
CORS_ORIGIN_WHITELIST = [UI_URL, UI_URL1, UI_URL2, UI_URL3]
CORS_ORIGIN_REGEX_WHITELIST = [UI_URL, UI_URL1, UI_URL2, UI_URL3]

CORS_ALLOWED_ORIGINS = [UI_URL, UI_URL1, UI_URL2, UI_URL3]
CORS_ALLOW_METHODS = ['GET', 'OPTIONS', 'POST']
CORS_ALLOW_HEADERS = ['accept', 'accept-encoding', 'authorization', 'content-type', 'dnt', 'origin', 'user-agent',
                      'x-crsftoken', 'x-requested-with']

# 20 minutes
CORS_PREFLIGHT_MAX_AGE = 1200

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'user',
    'branch',
    'subject',
    'document',
    'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'restapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'restapi.wsgi.application'


# Database

# db_settings = {
#     'dbname': 'Jcer',
#     'dbhost': '127.0.0.1:5432',
#     'dbuser': 'postgres',
#     'dbpass': 'postgres',
#     'dbschema': 'public',
# }

db_settings = {
    'dbname': 'dd4jf652ih05mi',
    'dbhost': 'ec2-52-71-153-228.compute-1.amazonaws.com',
    'dbuser': 'airnemdsuxeeny',
    'dbpass': '398932b05bc631960cc63b5dcf4430bc9b94bdb567b6d3332be8bca1cd32c718',
    'dbschema': 'public',
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_TMP = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

# Media

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

django_heroku.settings(locals())
