
# Some settings have to be set, some not... Give it a try.

# Directories:
# media: workdir + /media/
# static: workdir + /static/


# Set DEBUG to False to run in production!
DEBUG = True

#ADMINS = (
#	 ('Mr. Your Name', 'email@example.com'),
#)
#MANAGERS = ADMINS


DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': 'challenge.sqlite3',
	}
}


TIME_ZONE = 'Europe/Oslo'
LANGUAGE_CODE = 'en'


# Make this unique, and don't share it with anybody.
SECRET_KEY = 't+q))2q)e6k6*ggeqw*bl9q3%_t-(e3#%!v$yl-l(s^rtabf!)'
