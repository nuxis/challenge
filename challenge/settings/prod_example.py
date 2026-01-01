from challenge.settings.base import *  # noqa: F403

# FIXME: Refactor settings structure, using -environ or -decouple or some other solution that is nicer than noqa

DEBUG = False

# Need to set allowed hostnames when running with DEBUG=False.
# See https://docs.djangoproject.com/en/1.7/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["challenge.example.com"]

# These persons will be emailed with exception information when running with DEBUG=False.
# See https://docs.djangoproject.com/en/1.7/ref/settings/#admins
# ADMINS = (
# ('Mr. Your Name', 'email@example.com'),
# )
# MANAGERS = ADMINS

TIME_ZONE = "Europe/Oslo"
LANGUAGE_CODE = "en"


# Make this unique, and don't share it with anybody.
SECRET_KEY = "3lZUOCw$KSq.L56B3tMDVrjF7rGRZDLUK3N1Jk38X6amPWkOQvycehcSLk1uI/CjvjGaIEPrc9zO79PNTvJyAgfx9BSzt."
