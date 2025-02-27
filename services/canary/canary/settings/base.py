"""
Django settings for canary project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q!w$b=&hqg$9f0==(2#d$wz#2460c%yc!)top!^z7j66*4wp2+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
<<<<<<< HEAD:services/canary/canary/settings.py
=======
    'towers.apps.TowersConfig',
    'jet.dashboard',
    'jet',
>>>>>>> 42d03479639db545cb8a5ad1e4d410abc5abf137:services/canary/canary/settings/base.py
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',
    'guardian',
    'import_export',
    'flashcube'
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

ROOT_URLCONF = 'canary.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'canary.wsgi.application'


# Database
<<<<<<< HEAD:services/canary/canary/settings.py
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
=======
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'flashcube',
            'USER': 'flashcube',
            'PASSWORD': 'flashcube',
            'HOST': 'localhost',
            'PORT': '',
        }
>>>>>>> 42d03479639db545cb8a5ad1e4d410abc5abf137:services/canary/canary/settings/base.py
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

<<<<<<< HEAD:services/canary/canary/settings.py
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
=======
STATIC_URL = '/static/'

# API settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ),
    'DEFAULT_FILTERING_BACKEND': 'flashcube.filters.AllDjangoFilterBackend',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 200
}

AUTHENTICATION_BACKENDS = (
    # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    
    # Google OAuth2
    'social_core.backends.google.GoogleOAuth2',

    # OAuth2 Core
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

# Social Auth Settings
# These are for local DEV
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email, age_range'
}
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.10'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

OAUTH2_PROVIDER = {
    'OAUTH2_BACKEND_CLASS': 'oauth2_provider.oauth2_backends.JSONOAuthLibCore',
}

DATA_UPLOAD_MAX_MEMORY_SIZE = 20971520
>>>>>>> 42d03479639db545cb8a5ad1e4d410abc5abf137:services/canary/canary/settings/base.py
