
# Some settings have to be set, some not... Give it a try.

# Directories:
# media: workdir + /media/
# static: workdir + /static/


# Set DEBUG to False to run in production!
DEBUG = True

# Need to set allowed hostnames when running with DEBUG=False.
# See https://docs.djangoproject.com/en/1.7/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# These persons will be emailed with exception information when running with DEBUG=False.
# See https://docs.djangoproject.com/en/1.7/ref/settings/#admins
#ADMINS = (
#	 ('Mr. Your Name', 'email@example.com'),
#)
#MANAGERS = ADMINS

# The project is currently tested with sqlite3 and mysql.
# See https://docs.djangoproject.com/en/1.7/ref/settings/#databases for more information.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'challenge',
        'USER': 'challenge',
        'PASSWORD': 'challenge',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}



TIME_ZONE = 'Europe/Oslo'
LANGUAGE_CODE = 'en'


# Make this unique, and don't share it with anybody.
SECRET_KEY = 't+q))2q)e6k6*ggeqw*bl9q3%_t-(e3#%!v$yl-l(s^rtabf!)'
