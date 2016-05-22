# Django settings for challenge project.

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'challenge.sqlite3',
    }
}


TIME_ZONE = 'Europe/Oslo'

LANGUAGE_CODE = 'en'

from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    ('nb', _('Norwegian bokmål')),
    ('en', _('English')),
)

SITE_ID = 1

USE_I18N = True

MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/amedia/'

SECRET_KEY = 't+q))2q)e6k6*ggeqw*bl9q3%_t-(e3#%!v$yl-l(s^rtabf!)'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale/"),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'core.middleware.ClosedMiddleware',
)

ROOT_URLCONF = 'challenge.urls'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'bootstrap3',
    'solo',
    'levels',
    'core',
    'stats',
    'debug_toolbar', # for debugging
)


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

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

STATIC_URL = '/static/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

BOOTSTRAP3 = {
    'css_url': 'https://maxcdn.bootstrapcdn.com/bootswatch/3.3.6/superhero/bootstrap.min.css',
}

try:
    from challenge.settings_local import *
except ImportError as exc:
    print(exc)
