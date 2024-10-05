# Django settings for the hairdresser project.

from pathlib import Path
from decouple import config
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Media file settings
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Static file settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Директория для дополнительных статических файлов
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Директория для собранных статических файлов

# WhiteNoise settings for serving static files in production
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Security settings
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost',
                       cast=lambda v: [s.strip() for s in v.split(',')])

# Redirect after successful login
LOGIN_REDIRECT_URL = 'custom_login_redirect'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

# Cookie security settings
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=False, cast=bool)
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=False, cast=bool)

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'clients',
    'hairdressers',
    'appointments',
    'reviews',
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hairdresser.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'hairdresser.context_processors.user_role',
            ],
        },
    },
]

WSGI_APPLICATION = "hairdresser.wsgi.application"

# Database configuration
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files
# Дублирующие настройки убраны
# STATIC_URL и STATIC_ROOT уже были определены выше, так что их не нужно дублировать.

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
