"""
Django settings for jatszohaz project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from os import environ
from os.path import dirname, abspath, join

def get_env_variable(var_name, default=None):                                        
    """ Get the environment variable or return exception/default """                 
    try:                                                                             
        return environ[var_name]                                                     
    except KeyError:                                                                 
        if default is None:                                                          
            error_msg = "Set the %s environment variable" % var_name                 
            raise ImproperlyConfigured(error_msg)                                    
        else:                                                                        
            return default

# Build paths inside the project like this: join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^e&6xsn6awyd&xz6&gq47$e7lrum18hrlxjicb_!95ky*r*%o5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

########## HOST CONFIGURATION                                                     
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = get_env_variable('DJANGO_ALLOWED_HOSTS', "*").split(',')          
########## END HOST CONFIGURATION


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'jatszohaz.urls'

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

WSGI_APPLICATION = 'jatszohaz.wsgi.application'


# Travis setup
if get_env_variable('TRAVIS') is not None:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'travisci',
            'USER':     'postgres',
            'PASSWORD': '',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }
else:
    # Database
    # https://docs.djangoproject.com/en/1.11/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.' +
                get_env_variable('DJANG_DB_TYPE', 'postgresql_psycopg2'),
            'NAME':  get_env_variable('DJANGO_DB_NAME'),
            'USER':  get_env_variable('DJANGO_DB_USER'),
            'PASSWORD':  get_env_variable('DJANGO_DB_PASSWORD'),
            'HOST': get_env_variable('DJANGO_DB_HOST', ''),
            'PORT': get_env_variable('DJANGO_DB_PORT', ''),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
