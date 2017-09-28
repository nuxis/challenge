from challenge.settings.base import *

DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = 't+q))2q)e6k6*ggeqw*bl9q3%_t-(e3#%!v$yl-l(s^rtabf!)'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'challenge.sqlite3',
    }
}


MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

INSTALLED_APPS += ('debug_toolbar',)
