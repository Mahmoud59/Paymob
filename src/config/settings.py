import os
from pathlib import Path

import environ

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('src')
ENV_PATH = str(APPS_DIR.path('.env'))

env = environ.Env()
if env.bool('READ_ENVFILE', default=True):
    env.read_env(ENV_PATH)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', False)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=['localhost'])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_filters',
    'django_extensions',
    'rest_framework',
    'dry_rest_permissions',
    'rest_framework_swagger',
    'corsheaders',
    'analytics',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = env.str("DJANGO_STATIC_ROOT", default=str(ROOT_DIR.path('static')))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = env.str("DJANGO_STATIC_URL", default='/static/')

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = env.str("DJANGO_MEDIA_ROOT", default=str(APPS_DIR.path('media')))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = env.str("DJANGO_MEDIA_URL", default='/media/')


WSGI_APPLICATION = 'config.wsgi.application'

FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASE_URL = 'sqlite:///wp-api.db'
POSTGRES_DB = env('POSTGRES_DB', default=None)
POSTGRES_USER = env('POSTGRES_USER', default=None)
POSTGRES_PASSWORD = env('POSTGRES_PASSWORD', default=None)
POSTGRES_SERVICE = env('POSTGRES_SERVICE', default=None)
if POSTGRES_DB and POSTGRES_USER and POSTGRES_PASSWORD and POSTGRES_SERVICE:
    DATABASE_URL = 'postgres://' + POSTGRES_USER + ':' + POSTGRES_PASSWORD + POSTGRES_SERVICE + POSTGRES_DB

DATABASES = {
    'default': env.db('DATABASE_URL', default=DATABASE_URL),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['CONN_MAX_AGE'] = 600


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Cairo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

BASE_URL = env.str("BASE_URL", default="")

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/day',
        'user': '100/day'
    }
}
