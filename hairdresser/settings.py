import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
import sys

# Загрузка переменных окружения из файла .env
load_dotenv()

# Настройки проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Безопасность
SECRET_KEY = os.getenv('SECRET_KEY')  # Загрузка секретного ключа из .env

# Режим отладки (Debug)
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Разрешенные хосты
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Ваши приложения
    'clients',
    'hairdressers',
    'appointments',
    'reviews',
]

# Middleware
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise для обслуживания статики
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL для проекта
ROOT_URLCONF = 'hairdresser.urls'

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# WSGI приложение
WSGI_APPLICATION = 'hairdresser.wsgi.application'

# Настройки базы данных PostgreSQL через переменную окружения
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# Статические файлы (CSS, JavaScript)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Директория для статики
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Локальные файлы статики

# WhiteNoise для обслуживания статики в продакшене
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Медиа файлы (файлы, загружаемые пользователями)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Путь для медиафайлов

# Локализация
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Конфигурация для автоматической установки первичных ключей в моделях
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Отключение перенаправления на HTTPS и других безопасных настроек во время тестов
if 'test' in sys.argv:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_HSTS_SECONDS = 0
else:
    # Настройки для работы в продакшене
    if not DEBUG:
        SECURE_SSL_REDIRECT = True  # Перенаправление на HTTPS
        SESSION_COOKIE_SECURE = True
        CSRF_COOKIE_SECURE = True
        SECURE_HSTS_SECONDS = 31536000
        SECURE_HSTS_INCLUDE_SUBDOMAINS = True
        SECURE_HSTS_PRELOAD = True

# Дополнительно
# Убедитесь, что .env файл содержит переменные SECRET_KEY, DEBUG, DATABASE_URL, ALLOWED_HOSTS и другие важные настройки.
