import os
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MELDR_URL = os.environ.get("MELDR_URL", "https://meldr.rotterdam.nl")
MELDR_DOWNLOADS_PATH = os.environ.get("MELDR_DOWNLOADS_PATH", "link/downloads")
QRCODE_SOURCE_PARAM = os.environ.get("QRCODE_SOURCE_PARAM", "source")
UNPREDICTABLE_SLUG = os.environ.get("UNPREDICTABLE_SLUG", "bbbwknfjhjkhrniuydrksyefgtfy")
COOLDOWN_INTERVAL = int(os.environ.get("COOLDOWN_INTERVAL", 0))
VALID_SOURCE_VALUES = os.environ.get("VALID_SOURCE_VALUES", "a0-2-3-signs,avenues,digitale-mupis,digitale-schermen-metronetwerk,flyers,free-cards,havenloods,hoekse-krant,meldr-downloads,mupis,promo-containers,rozenburgse-courant").split(",")
MELDR_PLAYSTORE = os.environ.get("MELDR_PLAYSTORE", "https://play.google.com/store/apps/details?id=nl.rotterdam.meldr&gl=NL")
MELDR_APPSTORE = os.environ.get("MELDR_APPSTORE", "itms-apps://apps.apple.com/nl/app/meldr/id1524929423")

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

ENVIRONMENT = os.getenv("ENVIRONMENT")
DEBUG = ENVIRONMENT == "development"

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

USE_TZ = True
TIME_ZONE = "Europe/Amsterdam"

DEFAULT_ALLOWED_HOSTS = '*.forzamor.nl,localhost,127.0.0.1'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', DEFAULT_ALLOWED_HOSTS).split(',')

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "rest_framework",

    # Apps
    "campagne",
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
        "HOST": os.environ.get("DATABASE_HOST"),
        "PORT": os.environ.get("DATABASE_PORT"),
    },
}

MIDDLEWARE = (
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

STATIC_URL = "/static/"
STATIC_ROOT = os.path.normpath(join(os.path.dirname(BASE_DIR), "static"))

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.normpath(join(os.path.dirname(BASE_DIR), "media"))

CORS_ORIGIN_WHITELIST = (
    MELDR_URL,
    "https://mor-test.mendixcloud.com",
    "http://127.0.0.1",
    "http://0.0.0.0",
    "http://localhost",
)
CORS_ORIGIN_ALLOW_ALL = False

USE_X_FORWARDED_HOST = True

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
    }
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'default_cache_table',
    }
}

SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True