# Django settings for challenge project.

# for dynamic settings
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	 ('Mathias Boehn Grytemark', 'mathias@nuxis.org'),
)

MANAGERS = ADMINS


DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'psychic22',
		'USER': 'psychic22',
		'PASSWORD': 'topsikret22',
		'HOST': '127.0.01',
		'PORT': '',
	}
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Oslo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'no-nb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.getcwd(), "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/amedia/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 't+q))2q)e6k6*ggeqw*bl9q3%_t-(e3#%!v$yl-l(s^rtabf!)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
	 'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'challenge.urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
	 'django.contrib.admin',
	 'django.contrib.staticfiles',
	 'challenge.levels',
	 'challenge.core',
	 'challenge.stats',
)

PROJECT_DIR = os.path.dirname(__file__)
STATICFILES_DIRS = (
   os.path.join(PROJECT_DIR, "../static/"),
	)
TEMPLATE_DIRS = (
	 os.path.join(PROJECT_DIR, "templates"),
)

STATIC_ROOT = os.path.join(PROJECT_DIR, "static/")
STATIC_URL = '/static/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'
